import cv2 as cv
from cv2 import INTER_AREA
from cv2 import INTER_LINEAR
from cv2 import INTER_CUBIC
from matplotlib.pyplot import sca
import numpy as np


video = input("Type either 'livefeed' or 'file': ")
scale = input("Please enter a scale factor (value from 0-1: ")
interpolation = input("Type one digit of the following, 1 = Inter_Area, 2 = Linear, 3 = Cubic: ")

def scale_frame(frame, scale):
    # read the actual height and weight, scale it and store
    height = (frame.shape[0]*scale)
    width = (frame.shape[1]*scale)
    

    #return the scaled frame
    
    if interpolation == '1':
        return cv.resize(frame, (150, 150), (255,255),  fx = 250, fy=250, interpolation=cv.INTER_AREA) # performs rescaling by area interpolation
    elif interpolation == '2':
        return cv.resize(frame, (150, 150), (255,255),  fx = 250, fy=250, interpolation=cv.INTER_LINEAR) # performs rescaling by linear interpolation
    elif interpolation == '3':
        return cv.resize(frame, (150, 150), (255,255),  fx = 250, fy=250, interpolation=cv.INTER_CUBIC) # performs rescaling by cubic interpolation

if video == 'livefeed':
    video_location = 0
    def read_video(video_location, scale, side_by_side=False):
        
        if scale != 1 and scale != 0:   
            try:
                capture = cv.VideoCapture(video_location)
                while True:
                    isTrue, frame = capture.read()
                    scaled_frame = scale_frame(frame, scale)  # calls the scale_frame function to scale each frame 
                    
                    cv.imshow('scaled video', scaled_frame)
                    if side_by_side:
                        cv.imshow('original video', frame)
                    
                    if cv.waitKey(20) & 0XFF == ord('d'):
                        break
                capture.release()
            
            
            finally:
                cv.destroyAllWindows()
        else:
            print(f'The scale factor {scale} is not valid !!')
    read_video(video_location=0,scale=scale,side_by_side=False)

elif(video == 'file'):
    video_location = input("Please enter the location of your video file: ")
    def read_video(source, scale, side_by_side=False):
        if scale != 1 and scale > 0:   
            try:
                capture = cv.VideoCapture(source)
                while True:
                    isTrue, frame = capture.read()
                    scaled_frame = scale_frame(frame, scale)  # calls the scale_frame function to scale each frame 
                    
                    cv.imshow('scaled video', scaled_frame)
                    if side_by_side:
                        cv.imshow('original video', frame)
                    
                    if cv.waitKey(20) & 0XFF == ord('d'):
                        break
                capture.release()
            except:
                print('error')
            finally:
                cv.destroyAllWindows()
        else:
            print(f'The scale factor {scale} is not valid !!')