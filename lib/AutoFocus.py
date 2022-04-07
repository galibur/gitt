#!/usr/bin/env python3

# Name      : AutoFocus.py
# Author    : galibur
# Version   : 0.1
# Date      : 2022-02-14
# Decription: Control focus motor until picture / frame is at maximum sharpness (laplace ?)


class AutoFocus:

    def __init__(self, camera):
        self.version = 0.1

        self.camera = camera
        self.log = self.camera.telecam.log.log

        self.log('AutoFocus initialized', 5)
        