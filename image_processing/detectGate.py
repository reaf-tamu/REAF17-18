import numpy as np
import imutils
import argparse
import cv2
from ShapeDetector import ShapeDetector

#this is detectOrange + shapeDetection

ap=argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args=vars(ap.parse_args())

boundaries = [
	([0, 50, 145], [130, 220, 255]),
]

cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    resized = imutils.resize(frame, width=300)
    ratio = frame.shape[0] / float(resized.shape[0])
    
    frame2 = cv2.GaussianBlur(resized, (5, 5), 0)
    
    for (lower, upper) in boundaries:
	    # create NumPy arrays from the boundaries
	    lower = np.array(lower, dtype = "uint8")
	    upper = np.array(upper, dtype = "uint8")
     
	    # find the colors within the specified boundaries and apply
	    # the mask
	    mask = cv2.inRange(frame2, lower, upper)
	    output = cv2.bitwise_and(frame2, frame2, mask = mask)
	    
	    gray=cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
	    retval,fram=cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
	    
	     
	    	    
	      
    # find contours in the thresholded image and initialize the
    # shape detector
    cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    sd = ShapeDetector()	    
	    
    for c in cnts:
	    # compute the center of the contour, then detect the name of the
	    # shape using only the contour
	    shape = sd.detect(c)
	     
	    # multiply the contour (x, y)-coordinates by the resize ratio,
	    # then draw the contours and the name of the shape on the image
	    c = c.astype("float")
	    c *= ratio
	    c = c.astype("int")
	    cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
	    
	    cv2.imshow("original", frame)    
	    
    #cv2.imshow("orange and the new black", output)
    cv2.imshow("thresh", fram)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

