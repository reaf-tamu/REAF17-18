import numpy as np
import cv2

cap = cv2.VideoCapture('outputFL.avi')

lower = np.array([1, 48, 100], dtype = "uint8")
upper = np.array([9, 160, 175], dtype = "uint8")

while(cap.isOpened()):
    ret, frame = cap.read()
    
    blurred = cv2.GaussianBlur(frame, (11,11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.erode(mask, None, iterations = 2)
    mask = cv2.dilate(mask, None, iterations=2)
    
        
    im2, contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    
    #if there is more than one contour
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        ((x,y), radius) = cv2.minEnclosingCircle(c)
        
        #if the object is large enough to track
        if radius > 35:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 0), -1)
    
    
    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)

    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()