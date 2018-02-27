##### BGR NOT RGB #####

import numpy as np
import cv2
import time
import serial

#set up serial connection
ser = serial.Serial('COM3', 9600)  #if it is not working, check the COM port of the arduino
time.sleep(2)

#CONSTANTS
colorBoundaryLower = [ , , ] #fill this out
colorBoundaryUpper = [ , , ] #fill this out
KNOWN_WIDTH =                #fill this out
FOCAL_LENGTH =               #fill this out
FRAME_WIDTH = 640 #pixels
FRAME_HEIGHT = 480 #pixels
FRAME_CENTERX = FRAME_WIDTH/2
FRAME_CENTERY = FRAME_HEIGHT/2
HOVER_THRESH = 50 #pixels, if center of object is within this number of 
                   #pixels from the center of the frame then we will just hover

cap = cv2.VideoCapture(0)

def turn_direction(objectx, objecty): #Returns command to send to arduino 
    if(abs(objectx-FRAME_CENTERX) < HOVER_THRESH && abs(objecty-FRAME_CENTERY) < HOVER_THRESH):
        return 'HOV'
        
    elif ( abs(objectx-FRAME_CENTERX) < HOVER_THRESH ):
        if(objecty > FRAME_CENTERY):
            return ('DOW')
        else:
            return ('UP*')
    
    elif ( abs(objecty-FRAME_CENTERY) < HOVER_THRESH):
        if(objectx > FRAME_CENTERX):
            return ('RIG')
        else:
            return('LEF')
        
    else:
        if(objectx > FRAME_CENTERX):
            return ('RIG')
        else:
            return('LEF')


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # create NumPy arrays from the boundaries
    lower = np.array(colorBoundaryLower, dtype = "uint8")
    upper = np.array(colorBoundaryUpper, dtype = "uint8")
    
    #create mask to tell what objects are in the color range
    mask = cv2.inRange(frame, lower, upper)
    
    #trying to blur the image to remove some noise
    blur = cv2.GaussianBlur(mask, (5,5), 0)
    
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
    
    
    #Use the object's center point to determine which direction to turn the AUV
    #Then send command to the Arduino through Serial connection
    command = turn_direction(centerx, centery)
    ser.write(command.encode('utf-8'))
    ser.flush()
    print('Sent command: ')
    print(command[i])
    #confirm arduino reception of command
    arduinoFeedback = ser.read(3).decode('utf-8')
    print('Performing command: ')
    print(arduinoFeedback)
    
    
    cv2.imshow("frame", frame)       
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
        
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()