#!/usr/bin/env python3

# Name      : Config.py
# Author    : galibur
# Version   : 0.1
# Date      : 2022-02-14
# Decription: Handle and process config files

import json
import sys

class Config:
    def __init__(self, telecam, config_file='config.conf'):

        self.telecam = telecam
        self.log = self.telecam.log.log

        self.config_dir = 'config/'
        self.config_file = config_file        
        
        # Load general config
        self.general = self.load_config(self.config_file)

        # Load config for USB gamepad
        #self.gamepad = self.load_config('gamepad.conf')

        # Load config for turntable (e.g. speed)
        #self.turntable = self.load_config('turntable.conf')

        # Load config for tripod (e.g. speed)
        #self.tripod = self.load_config('tripod.conf')
    
        # Load config for camera focus (e. g. speed)
        #self.focus = self.load_config('camera_focus.conf')

        # Load config for camera zoom (e. g. speed)
        #self.zoom = self.load_config('camera_zoom.conf')

        # Load config for camera brigthness (e. g. speed)
        #self.brightness = self.load_config('camera_brightness.conf')

        # Load list of German Ortskennzeichen
        self.german_ortskennzeichen = self.load_config('orts_kennzeichen_liste.json')

        self.log('Config initilized',6)


    def load_config(self, config_file):
        self.log('LOAD CONFIG ' + str(config_file), 8)
        try:
            with open(str(self.config_dir) + str(config_file)) as f:
                try: 
                    return json.load(f)
                except:
                    self.log('Invalid config file ' + str(self.config_dir) + str(config_file), 2)
                    sys.exit() # Terminate program
                    
        except:
            self.log('Cannot open config file ' + str(self.config_dir) + str(config_file), 2)
            sys.exit() # Terminate program
            
        