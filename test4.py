from os import name
import cv2 as cv
import numpy as np

def split_video_channels(mirror=False):
    cap = cv.VideoCapture(-1)
    while True:
        ret_val, frame = cap.read()
        if ret_val == True:
            if mirror:
                #flips the image
                frame= cv.flip(frame, 1)

            height, width, layers = frame.shape 

            (B, G, R) = cv.split(frame) # split into RGB channels

            # merging
            zeroImgMatrix = np.zeros(frame.shape[:2], dtype="uint8")
            B = cv.merge([B, zeroImgMatrix, zeroImgMatrix])
            G = cv.merge([zeroImgMatrix, G, zeroImgMatrix])
            R = cv.merge([zeroImgMatrix, zeroImgMatrix, R])

            # double the image size
            final = np.zeros((height * 2, width * 2, 3), dtype="uint8")
            final[0:height, 0:width] = frame # 1st = Original
            final[0:height, width:width * 2] = R # 2nd = Red
            final[height:height * 2, 0:width] = G   # 3rd = Green
            final[height:height * 2, width:width * 2] = B  # 4th = Blue
            cv.imshow('Test', final)
        else:
            break
        if cv.waitKey(1) & 0xFF == ord('x'):  # 'x' key closes the window
            break
    cap.release()
    cv.destroyAllWindows()
def main():
    split_video_channels(mirror=True)
if name == 'main':
    main()

























