#!/usr/bin/env python3

# Name      : Gyroscope.py
# Author    : galibur
# Version   : 0.1
# Date      : 2022-02-14
# Decription: Aquire and process gyroscope data


class Gyroscope:

    def __init__(self, telecam):
        self.version = 0.1
        self.telecam = telecam
        self.log = self.telecam.log.log

        self.log('Gyroscope inititalized', 5)