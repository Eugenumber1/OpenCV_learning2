import cv2 as cv
import numpy as np

#gradients and edges

img = cv.imread('/Users/zhenyabudnyk/PycharmProjects/OpenCV_learning2/images/man.jpg')
cv.imshow("man", img)

blank = np.zeros((400,400), dtype='uint8')

#laplace

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('gray', gray)

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow(' Laplacian', lap)

# Sobel computes gradients in x and y directions

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('sobel x', sobelx)
cv.imshow('sobel y', sobely)
cv.imshow('combined', combined_sobel)


canny = cv.Canny(gray, 150, 175)
cv.imshow('canny', canny)



cv.waitKey(0)
