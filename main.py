import cv2
import numpy as np
def getmean(img):
    x,y = (img > 200).nonzero()
    return x.mean(), y.mean()
cap = cv2.VideoCapture(0)
flag = 0
while(1):

    # Take each frame
    i = 0
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    ret,thresh = cv2.threshold(mask,50,255,0)
    thresh1 = thresh
    if flag == 0:
        x1,y1 = getmean(thresh)
        x,y = getmean(thresh)
    else:
        x,y = getmean(thresh)
    flag = 1
    print(x-x1)
    if (x-x1) < 0:
        print("Right")
    elif (x-x1) > 0:
        print("Left")
    cv2.imshow('res',mask)
    cv2.imshow('contours', thresh)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()