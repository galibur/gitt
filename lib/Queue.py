#!/usr/bin/env python3

# Name      : Queue.py
# Author    : galibur
# Version   : 0.1
# Date      : 2022-02-14
# Decription: Queue used for ROS publisher (message queue)


class Queue:

    def __init__(self, telecam):
        
        self.telecam = telecam
        self.log = self.telecam.log.log

        self.log('Queue initialized', 5)