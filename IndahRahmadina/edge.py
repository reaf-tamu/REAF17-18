import cv2
import numpy as np
from matplotlib import pyplot as plt


cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    edges = cv2.Canny(frame,100,200)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #blur= cv2.blur(frame,1) idk how to use blur
    
    cv2.imshow('original',frame)
    cv2.imshow('canny',edges)
    cv2.imshow('grayscale',gray)
    #cv2.imshow('blur',blur)
    
    #plt.imshow(edges,cmap = 'gray')
    #plt.xticks([]), plt.yticks([]) 
    #plt.show([])
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


