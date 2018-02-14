##### BGR NOT RGB #####

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# define the list of boundaries
boundaries = [
	([120, 200, 90], [210, 255, 135]),  #GREEN in hotel room
    ([130,120,200], [255,210,255]) #RED in hotel room
]

KNOWN_DISTANCE = 29.0 #inches
KNOWN_WIDTH = 9.54 #inches
PIXELS = 169
FOCAL_LENGTH = 513.7

def distance_to_camera(knownWidth, focalLength, perWidth):
    return(knownWidth * focalLength) / perWidth


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # create NumPy arrays from the boundaries
    lower = np.array([130,120,210], dtype = "uint8")
    upper = np.array([255,230,255], dtype = "uint8")
 
    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(frame, lower, upper)
    output = cv2.bitwise_and(frame, frame, mask = mask)
 
    #trying to blur the image to remove some noise
    blur = cv2.GaussianBlur(mask, (5,5), 0)
    cv2.imshow("Blur", blur)
    
    #try to find edges of object with contours
    ret2, thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    
    #attempt to find largest contour
    areaArray = []
    for i, c in enumerate(contours):
        area = cv2.contourArea(c)
        areaArray.append(area)
        areaLargest = np.argmax(areaArray)
        areaLargestMax = max(areaArray)
        areaLargestCnt = contours[areaLargest]
        x, y, w, h = cv2.boundingRect(areaLargestCnt)   
        if area == areaLargestMax and area > 100:
            im2 = cv2.drawContours(frame, contours, i, (0,255,0), 3)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
            centerx = x+(w/2)
            centery = y+(h/2)
            center = [centerx, centery]
            distance = distance_to_camera(KNOWN_WIDTH, FOCAL_LENGTH, w)
            #print(w)
            print(distance)
    cv2.imshow("Contours", im2)
    
    
    # Display the resulting frame
    #cv2.imshow("frame",frame)
     # show the images
    cv2.imshow("images", np.hstack([frame, output]))
    cv2.imshow("mask", mask)
    
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()