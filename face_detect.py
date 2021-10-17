import cv2 as cv
import numpy as np

#face detection

img = cv.imread('/Users/zhenyabudnyk/PycharmProjects/OpenCV_learning2/images/group3.jpg')
cv.imshow("man", img)

#first step to transfer to gray, haar cascades looking for edges on the picture
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# to change the sensitivity we need to change scale factor and min neighbors

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f'Number of faces found = {len(faces_rect)}')

for(x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255), thickness=2)

cv.imshow('detected faces', img)

blank = np.zeros((400,400), dtype='uint8')

cv.waitKey(0)