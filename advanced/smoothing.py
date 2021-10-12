import cv2 as cv
import numpy as np

#reduce the noise on the image
#reduces the pixel intensity of the window
#it takes average pixel intensity from the pixels around

img = cv.imread('/Users/zhenyabudnyk/PycharmProjects/OpenCV_learning2/images/man.jpg')
cv.imshow("man", img)

#averaging
#it takes average pixel intensity from the pixels around
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

#gaussian blur
#each pixel gets blur weights, it is more natural

gauss_b = cv.GaussianBlur(img, (3,3), 5)
cv.imshow('Gaussian Blur', gauss_b)

#median blur
median = cv.medianBlur(img, 5)
cv.imshow('median Blur', median)

#bilateral blurring - very effective, used in advanced
bilateral = cv.bilateralFilter(img, 5, 100, 100)
cv.imshow('bilat', bilateral)






cv.waitKey(0)
