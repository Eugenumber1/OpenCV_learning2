import cv2 as cv

#videos and images has different unuseful information so when we resize/rescale them we get rid of this info
#we can also change the height and width of the video
#the reason for

img = cv.imread('/images/woman.jpg')
cv.imshow('Woman', img)

#rescaling photos
def changeRes(width, height):
    #live videos only
    video.set(3,width)
    video.set(4, height)


def rescaleFrame(frame, scale=0.75):
    #images, videos and live videos
    width = int(frame.shape[1] * scale) #we change the width due to scale
    height = int(frame.shape[0] * scale)
    dimensions = (width, height) #making a tuple
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)# resize the frame to particular dimension


#Reading videos, rescaling them
video = cv.VideoCapture('/Users/zhenyabudnyk/PycharmProjects/OpenCV_learning2/videos/'
                        'Funny Cat Vines - Short Funny Cats Videos.mp4') #to read the video
#if we have a number as the argument here, we indicate the camera which is capturing the video
while True:
    isTrue, frame = video.read() #make a frame, to grab video frame by frame in the loop
    video_resized = rescaleFrame(frame, 0.2)#resize each frame from the video

    cv.imshow('Video Resized', video_resized)
    if cv.waitKey(20) & 0xFF==ord('d'): #if they have waitkey 20 we terminate the loop not to make the video playing indefinetely
        #or if the letter D is pressed
        break

video.release() # we release the capture device
cv.destroyAllWindows() #close the window


cv.waitKey(0)

