import cv2 as cv

img = cv.imread('/Users/zhenyabudnyk/PycharmProjects/OpenCV_learning2/images/w_sexy_gr.jpg') #returns an image as a matrix of pixels
cv.imshow('Cat', img) #displays an image in a new window, first parameter is a name of the window and the second is a a matrix
cv.waitKey(0) #keyboard binding function, waits for some mili0seconds until image is shown