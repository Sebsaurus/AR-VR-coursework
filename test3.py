from turtle import width
from IPython.display import clear_output
import cv2
import cv2 as cv
from matplotlib.pyplot import close









def show_details(capture):   # prints the basic attributes 
    clear_output(wait=True)  # clear the notebook cell after printing 
    print(f"CAP_PROP_FPS        \t: {capture.get(cv.CAP_PROP_FPS)}")
    print(f"CAP_PROP_BRIGHTNESS \t: {capture.get(cv.CAP_PROP_BRIGHTNESS)}")
    print(f"CAP_PROP_CONTRAST   \t: {capture.get(cv.CAP_PROP_CONTRAST)}")
    print(f"CAP_PROP_SATURATION \t: {capture.get(cv.CAP_PROP_SATURATION)}")
    



def alter_params(capture, alter_param):   # alters the parameters 

    capture.set(cv.CAP_PROP_FPS, alter_param['fps'])
    capture.set(cv.CAP_PROP_BRIGHTNESS, alter_param['brightness'])
    capture.set(cv.CAP_PROP_CONTRAST, alter_param['contrast'])
    capture.set(cv.CAP_PROP_SATURATION, alter_param['saturation'])

    return capture

def show_alteredVideo(source):    # renders the video stream 
    print('Preparing capture... ')
    try:
        capture = cv.VideoCapture(source)
        capture = alter_params(capture, alter_param) # calling to alter the params
        print('Displaying... ')
        while True:
            isTrue, frame = capture.read()
            show_details(capture)   # calling the capture details 
            cv.imshow('Window', frame)
            if cv.waitKey(20) & 0xFF == ord('d'): # press 'd' to exit
                break
        capture.release()
    except:
        print('Error')
    finally:
        cv.destroyAllWindows()

def show_originalVideo(source):    # renders the video stream 
    print('Preparing capture... ')
    try:
        capture = cv.VideoCapture(source)
        capture = alter_params(capture, alter_param) # calling to alter the params
        print('Displaying... ')
        while True:
            isTrue, frame = capture.read()
            show_details(capture)   # calling the capture details 
            cv.imshow('Window', frame)
            if cv.waitKey(20) & 0xFF == ord('d'): # press 'd' to exit
                break
        capture.release()
    except:
        print('Error')
    finally:
        cv.destroyAllWindows()


show_details(0)
# here is where the user assigns which values they'd like to assign to each variable
fps = input("\n What fps would you like to use?: \n")
brightness = input("What brightness would you like to use?: \n")
contrast = input("What brightness would you like to use?: \n")
saturation = input("What saturation would you like to use: \n")
## set params to the user's input
alter_param = {
        
        'fps' : fps, 
        'brightness' : brightness,
        'contrast' : contrast,
        'saturation' : saturation,
    
    }

alter_param(0, alter_param)
# final code to show the video with new attributes applied 
show_alteredVideo(0)




