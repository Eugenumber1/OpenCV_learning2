import cv2 as cv
import numpy as np

img = cv.imread('/Users/zhenyabudnyk/PycharmProjects/OpenCV_learning2/images/cat.jpg')

cv.imshow("woman", img)

cap = cv.VideoCapture(0)
ret, imgOriginalScene = cap.read()


#translation - shifting the immage via x or y axes
#function to transform, we make the trans matrix first, where we input x and y
#then extract the shapes of the image to know its dimesnions
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0,1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# negative x - left, positive x - right
# positive y - down, negative y - up

translated = translate(img, 100, 100)
cv.imshow('translated', translated)

# Rotating images

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (height, width)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 30)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, 50) #you rotate the image with the black angles it has
cv.imshow('2rotated', rotated_rotated)

#resize the image

resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#flipping the image

flip = cv.flip(img, -1)
# 0 flips vertically, 1 horizontally, -1 does both
cv.imshow('flipped', flip)

#cropping - cut an image
cropped = img[200:400, 300:400]
cv.imshow('cropped', cropped)





cv.waitKey(0)