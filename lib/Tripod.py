#!/usr/bin/env python3

# Name      : Tripod.py
# Author    : galibur
# Version   : 0.1
# Date      : 2022-02-14
# Decription: Control tripod motor; tilt cam / y-axis

class Tripod:
    
    def __init__(self, telecam):

        self.telecam = telecam
        self.log = self.telecam.log.log

        self.min_pos = False
        self.max_pos = False
        self.pos = False

        self.calibration_in_grogress = False

        self.log('Tripod inititalized', 5)


    def calibrate(self):
        
        self.log('Send Tripod calibration ROS command to channel "user_input" ; arduinos receive it.', 8)

        self.calibration_in_grogress = True

        self.status()

        # Reset min_pos and max_pos
        self.min_pos = False
        self.max_pos = False

        # Turn left, until min_pos != False
        #if self.pos == 0:
        #    self.min_pos = 0
        #else:
        self.tilt(-1)
       
        # Rest of calibration is done / controlled by ROSMessageProcessor on /pan_tilt input messages (min_pos_x, max_pos_x, min_pos_y, max_pos_y)


    # Tilt the Tripod
    def tilt(self, direction):

        self.log('do the tilt', 2)
        # Turn left
        if direction == -1:
            msg = '{"user_input":"gamepad","ABS_HAT0Y": -1}'
            self.telecam.node.publish(msg)

        # Turn  right
        elif direction == 1:
            msg = '{"user_input":"gamepad","ABS_HAT0Y": 1}'
            self.telecam.node.publish(msg)
            
        # Stop Tripod
        elif direction == 1:
            msg = '{"user_input":"gamepad","ABS_HAT0Y": 0}'
            self.telecam.node.publish(msg)
            


    def status(self):
        self.log('pos: ' + str(self.pos), 8)
        self.log('min_pos: ' + str(self.min_pos), 8)
        self.log('max_pos: ' + str(self.max_pos), 8)
