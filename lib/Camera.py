#!/usr/bin/env python3

# Name      : Camera.py
# Author    : galibur
# Version   : 0.1
# Date      : 2022-02-14
# Decription: Camera object; zoom, autofocus, get frames, manipulate video, object detection playgound

# Provides high speed array processing functionality for image manipulation
import numpy as np

# Used for image processing
import cv2

# Used for processed FPS (frames per second) calculation
import time

# Terminate script
import sys

# Used for threading
#from threading import Thread

# Create virtual video output device (e.g. /dev/video10)
#from lib.VideoOutputSource import VideoOutputSource

# Autofocus functionality
from lib.AutoFocus import AutoFocus

# Zoom functionality
from lib.Zoom import Zoom

# Store multiple frames in one Frames object for easy access
from lib.Frames import Frames

# Process frames with open cv
from lib.FrameProcessor import FrameProcessor

class Camera:

    def __init__(self, gitt, device):
        self.version = 0.1

        # Gitt (main) object
        self.gitt = gitt

        # Video input device
        self.device = device

        # Frames per second
        self.fps = False
        self.fps_counter = 0
        self.fps_start_time = False        

        # Make global log available
        self.log = self.gitt.log.log

        self.log('Camera inititalized: ' + str(self.device), 5)
        
        # Holts multiple frames, can crete multi frames
        self.frames = Frames()

        # Process frames with cv2, e.g. object detection
        self.frameprocessor = FrameProcessor(self)



    def open(self):

        #self.cap = cv2.VideoCapture('/dev/video2') # video source 2 (4k usb3 cam)
        self.cap = cv2.VideoCapture(str(self.device)) # video source 0 (1080p usb cam)

        if not self.cap.isOpened():
            self.log("Cannot open camera", 3)
            sys.exit()


    def close(self):

        # Close the video input device
        try: 
            self.cap.release()
            self.log('Release video input device: ' + str(self.device), 0)
        except:
            self.log('Cannot release video input device: ' + str(self.device), 3)


    def get_frame(self):

        # Capture frame
        ret, frame = self.cap.read()

        return frame
        

    def stream(self):

        # Open camera source
        self.open()

        while True:

            # Get frame
            original = self.get_frame()

            # Make original frame globally available (as of now only used by VideoOutPutSource.start())            
            self.frames.original = original

            # Calculate FPS (frames per second) and save  it to frame showing FPS in upper right corner                        
            if self.fps_start_time == False:
                self.fps_counter = 0
                self.fps_start_time = time.time()

            else:                
                self.fps_counter += 1
                time_diff = time.time() - self.fps_start_time
                
                if time_diff > 1:
                    self.fps_start_time = False                    
                    self.fps = self.fps_counter

            # Create font for puttin text into frame            
            font = cv2.FONT_HERSHEY_COMPLEX            
            self.frames.fps = original
            cv2.putText(self.frames.fps, str(self.fps),(540,60),font,2,(255,255,255),3)  #text,coordinate,font,size of text,color,thickness of font

            # Do some cv2 frame processing -> Target: object detection 
            self.frameprocessor.process()

            # Show manipulaoriginalted frame in popup window
            #cv2.imshow('frame', self.frames.lpd_car)
            cv2.imshow('frame', self.frames.multiframe)
            
            #cv2.imshow('frame', self.frames.edges)
            

            # Set streaming frame for virtual video device
            self.frames.stream = self.frames.multiframe

            # Close window on button press 'q' -> optional. will only terminate this loop,
            if cv2.waitKey(1) == ord('q'):
                #sys.exit() # does not work
                break

            