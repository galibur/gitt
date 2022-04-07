#!/usr/bin/env python3

# Name      : Compass.py
# Author    : galibur
# Version   : 0.1
# Date      : 2022-02-14
# Decription: Aquire and process compass data


class Compass:

    def __init__(self, telecam):
        self.version = 0.1

        self.telecam = telecam
        self.log = self.telecam.log.log

        self.log('Compass inititalized',5)