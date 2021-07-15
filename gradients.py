import cv2 as cv
import numpy as np

img = cv.imread('/home/verne/Documents/photos/belle.jpg')
cv.imshow('Belle', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# three highpass filters by opencv
# https://docs.opencv.org/4.5.2/d5/d0f/tutorial_py_gradients.html

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel 
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

#Scharr
scharrx = cv.Scharr(gray, cv.CV_64F, 1, 0)
scharry = cv.Scharr(gray, cv.CV_64F, 0, 1)
combined_scharr = cv.bitwise_or(scharrx, scharry)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)
cv.imshow('Scharr X', scharrx)
cv.imshow('Scharr Y', scharry)
cv.imshow('Combined Scharr', combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)
cv.waitKey(0)