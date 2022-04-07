#!/usr/bin/env python3

# Name      : PlateList.py
# Author    : galibur
# Version   : 0.1
# Date      : 2022-04-07
# Decription: List of scanned plates

from collections import Counter


class PlateList:

    def __init__(self, gitt):
        self.version = 0.1

        self.gitt = gitt

        self.log = self.gitt.log

        self.log('PlateList initialized', 6)

        self.list = []


    def addPlate(self, plate):

        self.list.append(plate)


    def most_frequent(self, list):
        occurence_count = Counter(list)
        return occurence_count.most_common(1)[0][0]


    def print(self):

        #print(str(self.list))

        self.log('Print plate list')

        # Get most frequent plate
        list = dict(Counter(self.list))
        self.log('Most frequent: ' + str(self.most_frequent(self.list)), 8)

