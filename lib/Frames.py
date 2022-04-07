#!/usr/bin/env python3

# Name      : Frames.py
# Author    : galibur
# Version   : 0.1
# Date      : 2022-02-17
# Decription: Store multiple frames, combine multiple frames to one new frame

class Frames:

    def __init__(self):
        self.version = 0.1

        self.original = False
        self.gray = False

        self.stream = False

        self.fps = False

        self.hsv = False

        self.multiframe = False

        # Result of Tempo tissue package detection
        self.tempo = False
        self.mask = False

        self.edges = False

        # Used by LicensePlateDetector
        self.lpd_plate = False
        self.lpd_car = False
        