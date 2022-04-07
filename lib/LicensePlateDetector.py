##!/usr/bin/env python3

# Name      : LicencePlateDetector.py
# Author    : scr1ptard, galibur
# Version   : 0.3
# Date      : 2022-04-07
# Decription: This script will recognize numplates 
# Sources   : https://medium.com/programming-fever/license-plate-recognition-using-opencv-python-7611f85cdd6c
#
#               sudo apt-get update
#               sudo apt-get install libleptonica-dev 
#               sudo apt-get install tesseract-ocr tesseract-ocr-dev
#               sudo apt-get install libtesseract-dev
#               pip install --upgrade imutils
#               pip install opencv-python
#for further information > official documentation https://tesseract-ocr.github.io/tessdoc/Installation.html

# Used for image processing
import cv2
import imutils
# Provides high speed array processing functionality for image manipulation
import numpy as np
# OCR for license plate character recognition
import pytesseract
from lib.Log import Log

from lib.PlateList import PlateList

import re

class LicensePlateDetector:

    def __init__(self, gitt):
        self.version = 0.2

        self.gitt = gitt

        self.log = Log().log

        self.log('LicensePlateDetector initialized', 6)

        # Start endless detection loop

        self.plates = PlateList(self)

    def detect(self, frame):

        # Read the image file
        #image = cv2.imread('ss5.jpeg')
        #cv2.imshow("Original", image)
        # Convert to Grayscale Image
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Canny Edge Detection
        canny_edge = cv2.Canny(gray_image, 170, 200)

        # Find contours based on Edges
        contours, new = cv2.findContours(canny_edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:30]

        # Initialize license Plate contour and x,y,w,h coordinates
        contour_with_license_plate = None
        license_plate = None
        x = None
        y = None
        w = None
        h = None

        # Find the contour with 4 potential corners and create ROI around it
        for contour in contours:
            # Find Perimeter of contour and it should be a closed contour
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.01 * perimeter, True)
            if len(approx) == 4:  # see whether it is a Rect
                contour_with_license_plate = approx
                x, y, w, h = cv2.boundingRect(contour)
                license_plate = gray_image[y:y + h, x:x + w]
                break
        (thresh, license_plate) = cv2.threshold(license_plate, 127, 255, cv2.THRESH_BINARY)
        #cv2.imshow("plate", license_plate)
        self.gitt.camera.frames.lpd_plate = license_plate

        # Removing Noise from the detected image, before sending to Tesseract
        try:
            license_plate = cv2.bilateralFilter(license_plate, 11, 17, 17)

            #cv2.imshow("License Plate Detection", license_plate)

            (thresh, license_plate) = cv2.threshold(license_plate, 150, 180, cv2.THRESH_BINARY)

            # Text Recognition
            text = pytesseract.image_to_string(license_plate)
            # Draw License Plate and write the Text
            image = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
            image = cv2.putText(image, text, (x - 100, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,
                                cv2.LINE_AA)

            # TODO, only show if txt not empty
            self.checkPlateText(text)

            # cv2.imshow("License Plate Detection", image)
            # cv2.waitKey(0)
            self.gitt.camera.frames.lpd_car = image

        except:
            license_plate = False

        self.gitt.camera.frames.lpd_plate = license_plate
        #self.gitt.camera.frames.lpd_plate_clean = license_plate

    def checkGermanOrtskennzeichen(self, plate):

        ort = False
        try:
            ort = str(self.gitt.config.german_ortskennzeichen[str(plate)])
        except:
            ''

        return ort


    def checkPlateText(self, text):

        # Remove trailing spaces / tabs
        text = text.strip()

        if text != "":

            # Only keep A-Z, 0-9, '-', ' ', ä, ö, ü
            clean = re.sub('[^ \-A-Z0-9äöüAÖÜ]', '', text)

            # Replace '-' with ' '
            clean = clean.replace('-', ' ')

            # Check if plate begins with A-Z
            if ord(clean[0]) >= 65 and ord(clean[0]) <= 90:
                ''
                #self.log('OK, normal plate', 6)

            # Check if plate begins with 0 (zero)
            elif ord(clean[0]) == 48:
                ''
                #self.log('OK, government', 6)

            else:
                # Non valid plate
                #self.log('Non valid', 6)
                return False

            # Split plate into parts
            parts = re.findall(r'\S+', clean)
            #print(str(len(parts)) + " parts : " + str(parts))


            # If 3 parts -> perfect , e.g. [B, CE, 1234]
            if len(parts) == 3:
                ''
                #self.log('3 parts = perfect', 1)

            # If 2 parts -> iterate over 2nd part, until number is hit (index > 0!)
            elif len(parts) == 2:
                #self.log('Part 2: ' + str(parts[1]), 2)

                tmp_part_1 = ''
                tmp_part_2 = ''

                for element in range(0, len(parts[1])):
                    #print(parts[1][element])

                    # Check if element is number
                    if ord(parts[1][element]) <= 57:

                        if tmp_part_1 == '':
                            break
                        else:
                            tmp_part_2 += parts[1][element]
                    else:
                        tmp_part_1 += parts[1][element]



            # If 4 parts -> E for electro, H for historical
            elif len(parts) == 4 and (parts[3] == 'E' or parts[3] == 'H'):
                ''
                # ok

            # Else: non valid!
            else:
                return False

            # Check part 1 for ortskennzeichen
            ort = self.checkGermanOrtskennzeichen(parts[0])

            if not ort:
                return False




            self.log("License Plate :" + str(ort) + ', ' + str(clean), 6)

            self.plates.addPlate(clean)

            self.plates.print()

            #print(str(len(self.plates)))

            #print(str(self.plates))
            #self.log("first letter ord number: " + str(ord(clean[0])), 6)

        result = False


        return result