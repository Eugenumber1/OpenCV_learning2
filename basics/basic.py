import cv2 as cv

img = cv.imread('/Users/zhenyabudnyk/PycharmProjects/OpenCV_learning2/images/cat.jpg')
cv.imshow("Cat", img)

#converting to grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #TRANSFORM THE SOURCE IMG TO GRAY color
cv.imshow('gray', gray)

# how to blur an image
# removes noise from the picture which is not needed
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) #source, then kernel size(ODD) which defines the intensity, then default
cv.imshow('blurred man', blur)

#edge cascade
#finds edges on the picture
canny = cv.Canny(blur, 125, 175) #finds all edges and shows the black-white picture with edges only
#we can reduce some edges if we blur the image
cv.imshow('canny', canny)

#Dilating the image
dilated = cv.dilate(canny, (5,5), iterations=3)
cv.imshow('dil', dilated)

#eroding the image
eroded = cv.erode(dilated, (3,3), iterations=1) #subtle changes in the edges thickness
cv.imshow('eroded', eroded)

#resize the picture
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)

#cropping
cropped = img[50:200, 200:400]
cv.imshow("cropped", cropped)


cv.waitKey(0)