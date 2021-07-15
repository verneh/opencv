import cv2 as cv
import numpy as np

img = cv.imread('/home/verne/Documents/photos/belle.jpg')
cv.imshow('Belle', img)

# Translation
def translate(img, x, y):
    # two list. one list for x, one for y
    transMat = np.float32([[1,0,x],[0,1,y]])
    # get the dimension which is a tuple of img.shape
    dimensions = (img.shape[1], img.shape[0])
    # warpAffine applies affine tranformation to the image
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

rotation_rotated = rotate(img, -90)
cv.imshow('Rotation of Rotated', rotation_rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)