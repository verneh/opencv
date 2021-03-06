# import libaries.
import cv2 as cv
import numpy as np

img = cv.imread('photos/belle.jpg')
cv.imshow('Belle', img)

# why does the value have to be uint8?
# https://stackoverflow.com/questions/23749968/why-datatype-has-to-be-uint8-in-opencv-python-wrapper
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html
# multistage edge detection algorithm in order to get the strong edges of the image.
# edge cascade   
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# dilate the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# erode the image.
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

# resize image
# resized = cv.resize(img, (400, 400), interpolation=cv.INTER_AREA)
# you can use cv.INTER_CUBIC and it will give you a better quality image
# compared to INTER_AREA.
# cv.imshow('Resized', resized)

# crop image. images are similar to array and this is similar to array slicing.
# cropped = img[50:200, 200:400]
# cv.imshow('Cropped', cropped)

cv.waitKey(0)
