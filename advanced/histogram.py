import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

#historgram - a layer to visualize the pixel intensity distribution
#for grayscale, for rgb
img = cv.imread('/Users/zhenyabudnyk/PycharmProjects/OpenCV_learning2/images/cat.jpg')
cv.imshow("man", img)

#to gray
gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow(' gray ', gray)

blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
#cv.imshow('circle', circle)

masked = cv.bitwise_and(gray, gray, mask=mask)#make the mask
cv.imshow('Mask', masked)

#grayscale histogram
#gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])
#plt.figure()
#plt.title('Grayscale Histogram')
#plt.xlabel('Bins')
#plt.ylabel('# of bins')
#plt.plot(gray_hist)
#plt.xlim([0, 256])
#plt.show()


# color histogram
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], masked, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()



cv.waitKey(0)