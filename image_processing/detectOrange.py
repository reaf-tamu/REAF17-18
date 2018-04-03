import numpy as np
import argparse
import cv2

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
    
    #edge = cv2.Canny(frame,200,100)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    for (lower, upper) in boundaries:
	    # create NumPy arrays from the boundaries
	    lower = np.array(lower, dtype = "uint8")
	    upper = np.array(upper, dtype = "uint8")
     
	    # find the colors within the specified boundaries and apply
	    # the mask
	    mask = cv2.inRange(frame, lower, upper)
	    output = cv2.bitwise_and(frame, frame, mask = mask)
     
	    # show the images
	      
    cv2.imshow("original", frame)
    cv2.imshow("orange and the new black", output)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

