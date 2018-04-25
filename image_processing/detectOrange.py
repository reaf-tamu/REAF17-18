import numpy as np
import imutils
import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args=vars(ap.parse_args())

#boundaries of what the program will consider "orange"
#(BGR format)
boundaries = [
	([0, 50, 145], [130, 220, 255]),
]

cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    #edge = cv2.Canny(frame,200,100)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized = imutils.resize(frame, width=300)
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
	    # show the images
	      
    cv2.imshow("original", frame)
    #cv2.imshow("orange and the new black", output)
    cv2.imshow("thresh", fram)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

