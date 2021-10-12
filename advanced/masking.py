import cv2 as cv
import numpy as np

#with bitwise operations we can use masking
#masking is making it possible to concetrate on some specific objects on the picture


img = cv.imread('/Users/zhenyabudnyk/PycharmProjects/OpenCV_learning2/images/man.jpg')
cv.imshow("man", img)

blank = np.zeros(img.shape[:2], dtype='uint8') #size of the mask MUST BE the same as the size of the immage
cv.imshow('black', blank)

mask = cv.rectangle(blank, (img.shape[1]//2 + 45, img.shape[0]//2), (img.shape[1]//2, img.shape[0]//2 + 100), 100, 255, -1)
cv.imshow('mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('masked', masked)



cv.waitKey(0)