#!/usr/bin/env python3

# Name      : Sensors.py
# Author    : galibur
# Version   : 0.1
# Date      : 2022-02-15
# Decription: Provide data from multiple sensors

# Aquire GPS data
from lib.GPS import GPS

# Aquire compass data
from lib.Compass import Compass

# Aquire gyroscope data
from lib.Gyroscope import Gyroscope

class Sensors:

    def __init__(self, telecam):
        
        self.telecam = telecam
        self.log = self.telecam.log.log

        self.gps = GPS(self.telecam)
        self.compass = Compass(self.telecam)
        self.gyroscope = Gyroscope(self.telecam)

        self.log('Sensors inizialized', 5)
