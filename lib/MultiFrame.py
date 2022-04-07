#!/usr/bin/env python3

# Name      : MultiFrame.py
# Author    : galibur
# Version   : 0.1
# Date      : 2022-02-18
# Decription: Creates a new frame with given width and height including all given frames

import cv2

import numpy as np

class MultiFrame:

    # __new__ instead of __init__ to return a arbitrary data type (here: numpy array / frame)
    def __new__(self, width, height, frames):

        self.width = width
        self.height = height
        self.frames = frames

        self.multiframe = self.create(self)
        
        return self.multiframe

    
    # Create one frame containing multiple smaller frames (a of now, 4 in 1)
    def create(self):

        multiframe = False

        #print(len(self.frames))
        #print(self.frames[0].shape)

        frame_count = len(self.frames)

        frame_width = 0
        frame_height = 0
        

        if frame_count > 64:
            print('ERROR: cannot create MultiFrame from more than 64 frames')
            return False

        if frame_count == 1:
            return self.frames[0]

        for i in range(2,9):
            
            max_frames = i * i
            
            if frame_count <= max_frames:
                                
                empty_frames = max_frames - frame_count

                #print(str(i) + 'x' + str(i) + ' : frame_count = ' + str(frame_count) + ', max_frames = ' + str(max_frames) + ', empty_frames = ' + str(empty_frames))

                width_sub_frame = int(self.width / i)
                height_sub_frame = int(self.height / i)

                frame_width += width_sub_frame
                frame_height += height_sub_frame

                #print('WIDTH_SUB_FRAME = ' + str(width_sub_frame))
                #print('HEIGHT_SUB_FRAME = ' + str(height_sub_frame))

                blank_image = np.zeros((height_sub_frame,width_sub_frame,3), np.uint8)

                # Create rows
                rows = list()

                frame_counter = 0

                for row_number in range(0, i):
                    #print('ROW: ' + str(row_number))

                    row = list()                    
                    for col_number in range(0, i):
                        
                        sub_frame = False

                        if frame_counter >= frame_count:
                            #row.append(blank_image)     
                            #self.frames[frame_counter] = blank_image
                            sub_frame = blank_image

                        else:
                            # Resize frame to sub frame size
                            tmp = self.frames[frame_counter]
                            
                            tmp = cv2.resize(tmp, (width_sub_frame, height_sub_frame))
                            
                            # TODO Check if imege is BGR color space; if not, convert it
                            #print('TYPE_TMP = ' + str(type(tmp)))
                            #print('SHAPE_TMP = ' + str(tmp.shape))
                            
                            try:
                                shape = tmp.shape[2]

                            except:
                                try:
                                    tmp = cv2.cvtColor(tmp,cv2.COLOR_GRAY2RGB)  
                                except:
                                    tmp = blank_image

                            #print('DIMENSION_TMP = ' + str(tmp.shape[2]))
                            

                            sub_frame = tmp
                            #row.append(tmp)

                        # Append sub_frame to row
                        row.append(sub_frame)

                        
                        #print('SHAPE of frame ' + str(frame_counter) + ' : ' + str(self.frames[frame_counter].shape))
                        #print('SHAPE of frame ' + str(frame_counter) + ' : ' + str(sub_frame.shape))
                        
                        frame_counter += 1
                        
                    # create row by concatenating all frames of the row                        
                    rows.append(np.concatenate((row), axis=1))
                    
                # Concat all created rows vertically
                multiframe = cv2.resize(np.concatenate((rows), axis=0), (self.width, self.height))
        
                break

        #print('SHAPE OF MULTIFRAME: ' + str(multiframe.shape))
        #cv2.imshow('Multiframe', multiframe)

        #return self.frames[0]
        return multiframe      