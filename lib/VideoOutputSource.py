#!/usr/bin/env python3

# Name      : VirtualVideo.py
# Author    : galibur
# Version   : 0.1
# Date      : 2022-02-14
# Decription: Provide virtual video source with processed video stream

import pyvirtualcam
import numpy as np
import cv2

# Used for threading
from threading import Thread

# Used for error handling
import sys

# Used for sleep function
import time

class VideoOutputSource:

    def __init__(self, camera):
        self.version = 0.1

        self.camera = camera
        self.log = self.camera.telecam.log.log

        self.width = 640
        self.height = 480

        print('VideoOutputSource inititalized')

        # Create video streaming thread
        self.streaming_thread = Thread(target=self.start,args=())

        # Start video streaming
        self.streaming_thread.start()
        

        # Start streaming
        #self.start()


    # Need to create virtual video device before with following command:
    #sudo modprobe -r v4l2loopback && sudo modprobe v4l2loopback devices=1 video_nr=10 card_label="RANDOM_CAM_NAME" max_buffers=2

    def make_multi_frame(self, frames):
        ''
        #self.log('Create one frame from multiple input frames. (e.g. 4 in 1')

    def start(self):
                
        with pyvirtualcam.Camera(width=self.width, height=self.height, device="/dev/video10", fps=20) as cam:
            print(f'Using virtual camera: {cam.device}')
            #frame = np.zeros((cam.height, cam.width, 3), np.uint8)  # RGB

            # TODO: Outsource the virtualvideo thingy while true desaster to some processy thingy!
            while True:
                #frame = self.camera.get_frame()
            

                #self.log('Stream to virtual device ...')
                #time.sleep(1)

                # Select frame to show (original b/w, contours, blur, etc)
                try:
                    frame = self.camera.frames.stream
                    flipped = cv2.flip(frame, 1)

                    # TODO MIRROR frame for video output

                    if type(frame) == bool:
                        ''
                        #self.log('No frame available.', 2) # Potentially creates heavy load!

                    else:

                    
                        try:
                            cam.send(frame)

                            try:
                                cam.sleep_until_next_frame()        
                            except:
                                self.log('cam.sleepuntil_next_frame()) failed', 2)
                            
                        
                        except OSError as err:
                            print("OS error: {0}".format(err))
                            self.log('cam.send(frame) failed', 2)

                except:        
                    ''
                    #self.log('No frame available.', 2)