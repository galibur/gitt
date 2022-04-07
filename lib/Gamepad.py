#!/usr/bin/env python3

# Name      : Gamepad.py
# Author    : galibur
# Version   : 0.1
# Date      : 2022-02-15
# Decription: Subscribe USB GAMEPAD input (pressed/released buttons) from ROS (channel: 'user_input')

import json

class Gamepad:

    def __init__(self, telecam):
        
        self.telecam = telecam
        self.log = self.telecam.log.log

        self.log('Gamepad initialized', 5)

        #self.process()

    # Process incoming ROS message from topic "/user_input" (USB gamepad)
    def process(self, data):
        self.log('No functionality! Moved to ROSMessageprocessor.process(data)', 3)
        