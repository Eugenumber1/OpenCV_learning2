import cv2 as cv
import numpy as np
import os

people = ['Zelenskiy', 'Poroshenko']
DIR = r'/Users/zhenyabudnyk/PycharmProjects/OpenCV_learning2/images/faces'
haar_cascade = cv.CascadeClassifier('/Users/zhenyabudnyk/PycharmProjects/OpenCV_learning2/haar_face.xml')
print(os.listdir(DIR))


features = []
labels = []
def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        print(path)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            cv.imshow(f'{img}', gray)
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()

#print(f'Length of the features is {len(features)}')
#print(f'Length of the labels is {len(labels)}')

face_recognizer = cv.face.LBPHFaceRecognizer_create()

#TRAIN recognizer on features and labels

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')
np.save('labels.npy', labels)
np.save('features.npy', features)
