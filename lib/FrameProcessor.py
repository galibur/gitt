#!/usr/bin/env python3

# Name      : FrameProcessor.py
# Author    : galibur
# Version   : 0.2
# Date      : 2022-04-06
# Decription: Process Frames.

# Provides high speed array processing functionality for image manipulation
import numpy as np

# Used for image processing
import cv2

# Used for edge detection dev
from matplotlib import pyplot as plt

from lib.MultiFrame import MultiFrame

# License plate detection
     
from lib.LicensePlateDetector import LicensePlateDetector

class FrameProcessor:

    def __init__(self, camera):        
        self.version = 0.1
        
        self.gitt = camera.gitt
        self.log = self.gitt.log.log

        self.frames = camera.frames

        self.lpd = LicensePlateDetector(self.gitt)

        self.log('FrameProcessor initialized.', 8)


    # Process all incoming frames, e.g. conversion, object detection, etc.
    def process(self):

        # TODO Still needed?
        self.gitt.camera.frames.stream = self.frames.original
                          
        # Tempo tissue package detection
        self.frames.tempo = self.tempo_detection()

        self.frames.edges = self.edges(self.frames.original)

        # License plate detection
        self.lpd.detect(self.frames.original)


        #self.gitt.camera.frames.multiframe = False

        # Create multi frame     
        self.gitt.camera.frames.multiframe = MultiFrame(1280, 720, (
            self.frames.original,
            self.frames.fps,
            self.frames.hsv,
            self.frames.edges,
            self.frames.lpd_plate,
            #self.frames.lpd_plate_clean,
            #self.frames.contours,
            #self.frames.mask,
            #self.frames.tempo,
            #self.frames.lpd_car,
            #self.frames.lpd_plate
        ))


    def get_sharpness(self, frame):

        sharpness = 0

        return sharpness



    # Canny edge detection
    def edges(self, frame):

        edges = cv2.Canny(frame,100,200)
        #self.log('EDGE FRAME DIMENSIONS: ' + str(edges.shape))
        return edges                


    # Convert frame from BGR color sprace to HSV
    def bgr_to_hsv(self, frame):

        self.frames.hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        return self.frames.hsv


    # Detect Tempo tissue package
    def tempo_detection(self):

        # Convert BGR to HSV
        hsv = self.bgr_to_hsv(self.frames.original)        

        # Define range of blue color in HSV
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(self.frames.hsv, lower_blue, upper_blue)

        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(self.frames.original,self.frames.original, mask= mask)
        
        self.frames.mask = mask
        self.frames.tempo = res
        
        return self.frames.original

    # Convert frame from BGR to GRAY
    def get_gray(self, frame):
        
        # Make grayscale frame
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        return frame
