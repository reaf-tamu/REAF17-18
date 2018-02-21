import cv2
import numpy as np
from matplotlib import pyplot as plt


cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    edges = cv2.Canny(frame,100,200)
    
    cv2.imshow('frame1',frame)
    cv2.imshow('frame2',edges)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


