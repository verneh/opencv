# import library.
import cv2 as cv

# read image from folder
# note to self: need to run curl to download image in linux.
# curl -o belle.jpg https://pbs.twimg.com/media/Ex-sqMsXAAAvLok?format=jpg&amp;name=medium
img = cv.imread('photos/belle.jpg')

# displays image in a window. keep in mind that this does not
# deal with images that are bigger than your screen.
cv.imshow('Belle', img)

# waiting for a key to be pressed
cv.waitKey(0)

# read video from folder
# reference for downloading yt videos.
# https://ostechnix.com/youtube-dl-tutorial-with-examples-for-beginners/
# run afterwards. chmod a+x /usr/local/bin/youtube-dl
capture = cv.VideoCapture('videos/belle.mp4')

while True:
    isTrue, frame = capture.read()
    
    # if cv.waitKey(20) & 0xFF==ord('d'):
    # This is the preferred way - if `isTrue` is false (the frame could 
    # not be read, or we're at the end of the video), we immediately
    # break from the loop. 
    if isTrue:    
        cv.imshow('Video', frame)
        # pressing the key d. will close the image and the video.
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()