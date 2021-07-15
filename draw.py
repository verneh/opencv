import cv2 as cv
import numpy as np

# create blank image.
# inside np.zeros consist ofheight width and
# channels. 
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# set color of image to green.
# blank[:] = 0,255,0

# set the color of the image at a specific point.
# blank[200:300, 300:400] = 0,255,0
# cv.imshow('Green', blank)

# create a green border within image in a certain position. 
cv.rectangle(blank, (0,0), (100,100), (0,255,0), thickness=2)
cv.imshow('Rectangle', blank)

# fill image with green for a specific area. thickness -1 can be replaced with cv.FILLED
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
# cv.imshow('Rectangle', blank)

# draw a circle.
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=2)
cv.imshow('Circle', blank)
print(blank.shape[1]//2, blank.shape[0]//2)

# draw a line.
cv.line(blank, (100,100), (250,210), (255,255,255), thickness=2)
cv.imshow('Line', blank)

# write some text
cv.putText(blank, 'Hello, Verne here!', (150,450), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)