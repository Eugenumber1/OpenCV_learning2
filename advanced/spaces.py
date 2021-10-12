import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#color spaces - a list of colors which are represented in the pixels

img = cv.imread('/Users/zhenyabudnyk/PycharmProjects/OpenCV_learning2/images/man.jpg')
cv.imshow("man", img)

#matplotlib has no idea if it is a bgr picture
#plt.imshow(img)
#plt.show()

#BGR to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#BGR TO LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('LAB', lab)

#BGR TO RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)
#it makes inversion of colours from bgr to rgb, especially between openCV and plt
#you can not convert grayscale to hsv directly

#HSV TO BGR
bgr1 = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('bgr1', bgr1)

plt.imshow(rgb)
plt.show()


cv.waitKey(0)
