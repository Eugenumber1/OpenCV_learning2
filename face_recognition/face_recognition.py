import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier('/Users/zhenyabudnyk/PycharmProjects/OpenCV_learning2/haar_face.xml')

#features = np.load('/Users/zhenyabudnyk/PycharmProjects/OpenCV_learning2/face_recognition/features.npy')
#labels = np.load('/Users/zhenyabudnyk/PycharmProjects/OpenCV_learning2/face_recognition/labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('/Users/zhenyabudnyk/PycharmProjects/OpenCV_learning2/face_recognition/face_trained.yml')

people = ['Zelenskiy', 'Poroshenko']

img = cv.imread(r'/Users/zhenyabudnyk/PycharmProjects/OpenCV_learning2/images/validation/zelenskiy/zv1.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#detect face on the image

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=2, minNeighbors=1)
for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]
    label, confindence = face_recognizer.predict(faces_roi)
    print(f'label - {label} with confidence of - {confindence}')
    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow('detected face', img)

cv.waitKey(0)

