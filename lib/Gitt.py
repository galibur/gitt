#!/usr/bin/env python3

# Name      : Gitt.py
# Author    : galibur
# Version   : 0.1
# Date      : 2022-04-06
# Decription: KITT main object; called from __main__ in gitt.py

# Log functionality
from lib.Log import Log

# Load config
from lib.Config import Config

# Parse provided command line arguments
from lib.ArgumentParser import ArgumentParser

# Save and play audtio file, create audio file from text (string)
from lib.AudioPlayer import AudioPlayer

# Access sensor data (e.g. GPS, compass, gyroscope)
from lib.Sensors import Sensors

# Full camera control
from lib.Camera import Camera

# Aquire GPS data
from lib.GPS import GPS

class Gitt:

    def __init__(self, device):
        
        self.device = device
        
        self.argument_parser = ArgumentParser()    
        
        self.log = Log()

        self.config = Config(self)

        self.audio = AudioPlayer(self) # Just for testing purpose; not needed so far.

        self.sensors = Sensors(self)

        self.gps = GPS(self)

        self.camera = Camera(self, self.device)

        self.log.log('GITT inititalized', 6)
        

    def start(self):

        self.log.log('GITT started', 6)

        # Start the camera / image processing
        self.camera.stream()
