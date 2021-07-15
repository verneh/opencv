# Rescale the image.
import cv2 as cv

# read image.
image = cv.imread('photos/belle.jpg')


# function to rescale the image or frame of video.
# even live videos.
def rescaleFrame(frame, scale=0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# another way of setting the resolution.
# but it only works for live video.
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

# read video.
capture = cv.VideoCapture('videos/belle.mp4')

while True:

    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame)
    image_resized = rescaleFrame(image)

    cv.imshow('Image', image)
    cv.imshow('Image Resized', image_resized)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
 
    # pressing the key d. will close the image and the video.
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()