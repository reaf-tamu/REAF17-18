import numpy as np
#import argparse
import cv2

cap = cv2.VideoCapture(0)

# define the list of boundaries
boundaries = [
	([120, 200, 90], [210, 255, 135]),  #GREEN in hotel room
    ([150,120,210], [255,210,255]) #RED in hotel room
]

ret, frame = cap.read()

# Our operations on the frame come here
#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
# create NumPy arrays from the boundaries
lower = np.array([150,120,210], dtype = "uint8")
upper = np.array([255,210,255], dtype = "uint8")



# find the colors within the specified boundaries and apply
# the mask
mask = cv2.inRange(frame, lower, upper)
#output = cv2.bitwise_and(frame, frame, mask = mask)

# show the images
#cv2.imshow("images", np.hstack([frame, output]))
#cv2.imshow("mask", mask)
  
#try to find edges of object with contours
#ret2, thresh = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
#im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#print(len(contours))
#im2 = cv2.drawContours(mask, contours, -1, (0,255,0), 3)
#cv2.imshow("Contours", im2)
#imgray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(mask, 127,255,cv2.THRESH_BINARY)
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(frame,contours,-1,(0,255,0),3)
# Display the resulting frame
#cv2.imshow("frame",frame)
cv2.imshow("frame", frame)
cv2.imshow("mask", mask)  
    
        
cv2.waitKey(0)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()