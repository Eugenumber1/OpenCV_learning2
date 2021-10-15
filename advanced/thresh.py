# thresholding - binarization of the image, pixels are either white or black on the picture
import cv2 as cv
import numpy as np

img = cv.imread('/Users/zhenyabudnyk/PycharmProjects/OpenCV_learning2/images/man.jpg')
cv.imshow("man", img)

blank = np.zeros((400,400), dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('gray', gray)

# simple thresholding

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY) #comapres each pixel with threshold value and changes to the 255 or 0
cv.imshow('simple', thresh)

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV) #comapres each pixel with threshold value and changes to the 255 or 0
cv.imshow('simple dimple', thresh)

#adaptive threshold - different immages with different threshold
#openCV computes the threshold by itself taking into account the kernel size on the basis of the mean or by gaussian distribution

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 1)
cv.imshow('adaptive', adaptive_thresh)


cv.waitKey(0)