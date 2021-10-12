import cv2 as cv
import numpy as np

#bitwise operators XOR, AND, OR, etc
#pixel is turned off if it has a value of 1 and vice versa

img = cv.imread('/Users/zhenyabudnyk/PycharmProjects/OpenCV_learning2/images/man.jpg')
cv.imshow("man", img)

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow("rect", rectangle)
cv.imshow("circle", circle)

#bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('bitwise and', bitwise_and)
#it took two images and showed its intersection (both of them)

#BITWISE OR
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('bitwise or', bitwise_or)
#it takes two imges and showed their union

#bitwise xor
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('bitwise xor', bitwise_xor)

#returns intersecting regions only

#bitwise not - inverts the colour
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('bitwise not', bitwise_not)







cv.waitKey(0)