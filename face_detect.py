
import cv2 as cv

img = cv.imread('/home/verne/Documents/photos/gabe.jpg')
# cv.imshow('Gabe', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray People', gray)

# Haar cascades looks at the edges to determine the image.
# parse the xml file.
haar_cascade = cv.CascadeClassifier('/home/verne/Documents/opencv/haar_face.xml')

# Once the value hits seven for minneighbors, instead of having two boxes
# we only get one box which highlights part of Gabe's face.
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)

# It's not consistent as haar cascades are sensitive to the noise of an image.

cv.waitKey(0)