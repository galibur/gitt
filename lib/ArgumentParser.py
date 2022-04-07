#!/usr/bin/env python3

# Name      : ArgumentParser.py
# Author    : galibur
# Version   : 0.1
# Date      : 2022-02-15
# Decription: Handle and process provided command line arguments

import argparse

class ArgumentParser:

    def __init__(self):

        # Parse arguments
    
        self.parser = argparse.ArgumentParser()
        
        self.parser.add_argument("-i", "--video-input-device", dest="video_input_device", default="/dev/video0",
                        help="Video input device")

        self.parser.add_argument("-o", "--virtual-video-output-device",
                        action="store", dest="virtual_video_output_device", default="/dev/video10",
                        help="Virtual vdeo output device")
        
        self.parser.add_argument("--image-width",
                        action="store", dest="image_width", default=640,
                        help="Images will be processed with this width.")
        
        self.parser.add_argument("--resize-height",
                        action="store", dest="image_height", default=480,
                        help="Images will be processed with this height.")
        

        self.args = self.parser.parse_args()

        # Process arguments
        self.process()

    def process(self):
        print('Process some arguments ...')