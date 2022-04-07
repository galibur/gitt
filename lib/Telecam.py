#!/usr/bin/env python3

# Name      : Telecam.py
# Author    : galibur
# Version   : 0.1
# Date      : 2022-02-14
# Decription: Telecam main object; total control of telecam

# Log functionality
from lib.Log import Log

# Load config
from lib.Config import Config

# Parse provided command line arguments
from lib.ArgumentParser import ArgumentParser

# Receive ROS messages 
#from lib.ROSPublisher import ROSPublisher

# Send and receive ROS messages
from lib.ROSNode import ROSNode

# Process ROS messages
from lib.ROSMessageProcessor import ROSMessageProcessor

# Save and play audtio file, create audio file from text (string)
from lib.AudioPlayer import AudioPlayer

# Access sensor data (e.g. GPS, compass, gyroscope)
from lib.Sensors import Sensors

# Spin the turntable, get current position
from lib.Turntable import Turntable

# Tilt tripod, get current position
from lib.Tripod import Tripod

# Full camera control
from lib.Camera import Camera

# Receive USB Gamepad input from ROS network
from lib.Gamepad import Gamepad

class Telecam:

    def __init__(self, device):
        
        self.device = device
        
        self.argument_parser = ArgumentParser()    
        
        self.log = Log()

        self.config = Config(self)

        self.rmp = ROSMessageProcessor(self)
        
        self.node = ROSNode(self)

        self.audio = AudioPlayer(self) # Just for testing purpose; not needed so far.

        self.sensors = Sensors(self)

        self.turntable = Turntable(self)

        self.tripod = Tripod(self)

        self.camera = Camera(self, self.device)

        self.gamepad = Gamepad(self)

        self.log.log('Telecam inititalized', 6)
        

        # BEGINING of ROS -> Entire program is rostopic subscriber input controlled
        # Start the ROS node -> infinite loop
        #self.node.start() # do this in telecam.py (__main__)
        