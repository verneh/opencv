
import cv2 as cv
import numpy as np

img = cv.imread('photos/belle.jpg')
cv.imshow('Belle', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow('Blank Image', blank)

# manual positioning of the circle for the mask
circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45,img.shape[0]//2 - 60), 100, 255, -1)
cv.imshow('Mask', circle)

# positioning of the rectangle for the mask.
rectangle = cv.rectangle(blank.copy(), (img.shape[1]//2,img.shape[0]//2),(img.shape[1]//2 + 45,img.shape[0]//2 - 60), 100, 255, -1)

# intersecting the circle and rectangle to come up with a new shaped mask
weird_shape = cv.bitwise_and(circle,rectangle)
# cv.imshow('Weird Shape', weird_shape)

# bitwise and for intersecting shapes. creates an oval shaped mask.
masked = cv.bitwise_and(img,img,mask=rectangle)
cv.imshow('Curved Image', masked)

cv.waitKey(0)
