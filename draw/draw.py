import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8') #make an array of zeros which will make a blank picture
cv.imshow('blank picture', blank)

img = cv.imread('/Users/zhenyabudnyk/PycharmProjects/OpenCV_learning2/images/cat.jpg')
cv.imshow("Cat", img)

# 1. paint image with certain color
blank[200:300, 300:400] = 0, 0, 255 #makes a red square in the middle of the picture
cv.imshow('Green', blank)

# 2. draw a rectangle
cv.rectangle(blank, (0,0), (255, 255), (0, 255, 0), thickness=cv.FILLED) #make the square on the picture
# first argument - the place where we start indentation, second argument - the size (where we stop indentation), third - thickness of line
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=-1)
cv.imshow('Rectangle', blank)

# 3.draw a circle
cv.circle(blank, (255,255), 40, (0, 0, 255), thickness=3) #first - picture, second - center of the picture,
# third - radius, 4 - thickness of line
cv.imshow('Circle', blank)

# 4. draw the line on the picture
cv.line(blank, (100,255), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=10)
cv.imshow('LIne image', blank)

# 5. Write a text on an image
cv.putText(blank, 'Hello', (255, 255), cv.FONT_ITALIC, 1.0, (0,255,0), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)