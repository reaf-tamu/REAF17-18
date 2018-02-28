import cv2
import numpy as np
from matplotlib import pyplot as plt
import time

cap = cv2.VideoCapture(0)

fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()

    bkgd = fgbg.apply(frame)

    blur = cv2.GaussianBlur(bkgd, (5,5), 0, 0)

    edges = cv2.Canny(blur, 100, 200)  
    
    cv2.imshow('Edges', edges)

    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1.2, 2000)

    if circles is not None:
        circles = np.round(circles[0,:]).astype("int")
        for(x, y, r) in circles:
            cv2.circle(frame, (x,y), r, (0,255,0), 4)
            cv2.rectangle(frame, (x-5, y-5), (x+5, y+5),(0, 128, 255), -1)

    cv2.imshow('Original', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
