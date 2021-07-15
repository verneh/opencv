# Import libaries.
import cv2 as cv

# Thresholds definition.
# https://docs.opencv.org/3.4/db/d8e/tutorial_threshold.html

# Read image.
img = cv.imread('photos/belle.jpg')
cv.imshow('Belle', img)

# cvt = convert image from one color space to another. in this case set it to gray.
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY )
cv.imshow('Simple Thresholded', thresh)

# For the Inverse, we expect that the pixels brighter than the thresh will turn dark
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV )
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Adaptive Thresholding -> method where the threshold value is calculated for smaller regions and therefore, 
# there will be different threshold values for different regions.
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

# Will remove image once key is pressed.
cv.waitKey(0)
