import matplotlib.pyplot as plt
import matplotlib
import cv2 as cv

image_loc = input("Enter the location of your image file: ") #used to find the file

img = cv.imread(image_loc) #image is recognized
height, width, channels = img.shape[:3] # assign width height & channel to what img has
height = str(height)
width = str(width)
channels = str(channels)

print(f'The resolution of the image is ' + width + ' x ' + height)
img = cv.imread(image_loc) #image is recognized
plt.figure(figsize=(16, 10), dpi=80) # creates figure with size and dpi
image_path = image_loc
ax_grey = plt.subplot(1,2,1)  # row 1, col 1
ax_rgb  = plt.subplot(1,2,2)  # row 1, col 2
image_bgr = cv.imread(image_path)    # default BGR 
image_bgr = cv.resize(image_bgr, (1920//2, 1080//2),cv.INTER_AREA) ## resing to fit 4 pics in screen 
image_grey = cv.cvtColor(image_bgr, cv.COLOR_BGR2GRAY)# BGP --> Grey 
image_rgb = cv.cvtColor(image_bgr, cv.COLOR_BGR2RGB) # BGR --> RGB
        #gray scale histogram 
gray_hist = cv.calcHist(images=[image_grey], channels=[0], mask=None, histSize=[256], ranges=[0,256])
ax_grey.set_title='Gray Scale'
ax_grey.plot(gray_hist, color='black', label='channel grey')
ax_grey.legend()
# bgr histogram 
ax_grey.set_title='RGB Scale'

channels = ('r','g', 'b')
for i, color in enumerate(channels):
        bgr_hist = cv.calcHist(images=[image_bgr], channels=[i], mask=None, histSize=[256], ranges=[0,256])
        ax_rgb.plot(bgr_hist, color=color, label = f'channel {color}')
        ax_rgb.legend()

if(channels == 1): #if statement to see if there is one channel aka, is it grayscaled
        print(f"The image is grayscaled.")
        
else: 
        print(f"image is not grayscaled.")
        
       
        plt.show()

    


