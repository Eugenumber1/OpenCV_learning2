import cv2 as cv
import numpy as np

#how to split and merge colour channels on the picture

img = cv.imread('/Users/zhenyabudnyk/PycharmProjects/OpenCV_learning2/images/man.jpg')
cv.imshow("man", img)

blank = np.zeros(img.shape[:2], dtype='uint8')


b,g,r = cv.split(img)
cv.imshow('blue', b)
cv.imshow('red', r)
cv.imshow('green', g)

print(img.shape)
print(r.shape)
print(g.shape)
print(b.shape)

#how to merge b g r into normal picture

merged_img = cv.merge([b,g,r])
cv.imshow('merged', merged_img)

blue_merged = cv.merge([b, blank, blank])
green_merged = cv.merge([blank, g, blank])
red_merged = cv.merge([blank, blank, r])

cv.imshow('blue', blue_merged)
cv.imshow('red', red_merged)
cv.imshow('green', green_merged)




cv.waitKey(0)