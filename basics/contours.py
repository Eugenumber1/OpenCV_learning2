import cv2 as cv
import numpy as np

img = cv.imread('/Users/zhenyabudnyk/PycharmProjects/OpenCV_learning2/images/man.jpg')
cv.imshow("man", img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray man', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)
#if we blur the photo we reduce the amount of contours we can recognize on it

#canny = cv.Canny(blur, 125, 175)
#cv.imshow('canny gray', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('threshholded', thresh)
#we have more contours if we use this approach
#threshholding makes the image binary - only black and white colors on it

#we find contours here from canny
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
#looks at all contours and returns python list of contours of the immage and hierarchies - hierarchical representation of objects on the picture
#RETR_LIST returns all the contours which it finds on the list, RETR_EXTERNAL - all contours outside, RETR_TREE returns the hierarchical tree of contours
#CHAIN_APPROX_NONE - does nothing, CHAIN_APPROX_SIMPLE - compresses all contours to two dots

print(f'{len(contours)} contours found!')

#first use canny and try to find contours with it

cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow('contours drawn', blank)

cv.waitKey(0)