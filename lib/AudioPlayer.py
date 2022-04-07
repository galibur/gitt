#!/usr/bin/env python3

# Name      : AudioPlayer.py
# Author    : galibur
# Version   : 0.1
# Date      : 2022-02-14
# Decription: Play/Stop audio file, text to speech.

import gtts
from playsound import playsound

class AudioPlayer:

    def __init__(self, telecam):

        self.version = 0.1
        self.telecam = telecam
        self.log = self.telecam.log.log
        self.file = False # Placeholder for audio path to audio file to play
        self.text = False # Placeholder for text to speech input text
        self.tmp_file = 'tmp/tmp.mp3'

        self.log('AudioPlayer initialized', 6)
       
        #self.text_to_speech('There is a rat in the kitchen. Chucka . Chucka . shaw')
        #self.text_to_speech('Hello my friend. Stay a while and listen!')
        #self.text_to_speech('Telle cam! ')


    def play(self, file):
        ''


    def pause(self):
        ''


    def stop(self):
        ''


    def text_to_speech(self, text):
        
         # make request to google to get synthesis
        self.tts = gtts.gTTS(str(text))

        # Save audio file to mp3
        self.tts.save(str(self.tmp_file))

        # Play saved audio file
        playsound(str(self.tmp_file))
