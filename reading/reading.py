import cv2 as cv
import os
print("file exists?", os.path.exists('/Users/zhenyabudnyk/PycharmProjects/OpenCV_learning2/videos/Funny Cat Vines - Short Funny Cats Videos.mp4'))

#img = cv.imread('/Users/zhenyabudnyk/PycharmProjects/OpenCV_learning2/images/dog.jpg') #returns an image as a matrix of pixels
#cv.imshow('Cat', img) #displays an image in a new window, first parameter is a name of the window and the second is a a matrix
#cv.waitKey(0) #keyboard binding function, waits for some mili0seconds until image is shown
#large images might go off screen

video = cv.VideoCapture('/Users/zhenyabudnyk/PycharmProjects/OpenCV_learning2/videos/'
                        'Funny Cat Vines - Short Funny Cats Videos.mp4') #to read the video
#if we have a number as the argument here, we indicate the camera which is capturing the video
while True:
    isTrue, frame = video.read() #make a frame, to grab video frame by frame in the loop
    cv.imshow('Video', frame) #put the frame which is going to be shown (?)
    if cv.waitKey(20) & 0xFF==ord('d'): #if they have waitkey 20 we terminate the loop not to make the video playing indefinetely
        #or if the letter D is pressed
        break

video.release() # we release the capture device
cv.destroyAllWindows() #close the window