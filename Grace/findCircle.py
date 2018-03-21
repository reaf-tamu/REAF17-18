import cv2
import numpy as np
from matplotlib import pyplot as plt
import time

cap = cv2.VideoCapture(0)

#fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()

    thresh = 0
    maxValue = 255

    th, dst = cv2.threshold(frame, thresh, maxValue, cv2.THRESH_BINARY)

    #bkgd = fgbg.apply(frame)

    #blur2 = cv2.medianBlur(frame, 3)

    #blur1 = cv2.GaussianBlur(frame, (31,31), 1, 1)

    #edges = cv2.Canny(blur1, 100, 200)

    cv2.imshow('threshhold', th)
    
    #cv2.imshow('gaussian blur', blur1)

    #cv2.imshow('Gauss Blur', edges)

    '''circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1.2, 2000)

    if circles is not None:
        circles = np.round(circles[0,:]).astype("int")
        for(x, y, r) in circles:
            cv2.circle(frame, (x,y), r, (0,255,0), 4)
            cv2.rectangle(frame, (x-5, y-5), (x+5, y+5),(0, 128, 255), -1)
    '''
    #cv2.imshow('Original', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
