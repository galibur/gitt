#!/usr/bin/env python3

# Name      : telecam.py
# Author    : galibur
# Version   : 0.1
# Date      : 2022-02-14
# Decription: 
# Location  : 

# keyboardInterruptHandler
import signal

# Used to close all opened cv2 windows
import cv2

from lib.Gitt import Gitt

from lib.LicensePlateDetector import LicensePlateDetector



# Main function
if __name__ == '__main__':


    # Clean close of script on CTRL + c
    def keyboardInterruptHandler(signal, frame):
        #telecam.log.log("KeyboardInterrupt (ID: {}) has been caught. Cleaning up...".format(signal))

        # Close camera device
        #telecam.camera.close()

        # Close all opened cv2 windows 
        cv2.destroyAllWindows()

        exit(0)

    # Start the signal handler for CTRL + c
    signal.signal(signal.SIGINT, keyboardInterruptHandler)


    gitt = Gitt("/dev/video4")

    gitt.start()

