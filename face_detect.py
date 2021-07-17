
import cv2 as cv

img = cv.imread('photos/gabe.jpg')
cv.imshow('Gabe', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray People', gray)

# Haar cascades looks at the edges to determine the image.
# parse the xml file.
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# We see that we have two boxes, one that highlights part of Gabe's face.
# The other is on the side of his face.
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)

# It's not consistent as haar cascades are sensitive to the noise of an image.
cv.waitKey(0)