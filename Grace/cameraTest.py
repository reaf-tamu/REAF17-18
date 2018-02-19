import numpy as np
import cv2


cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame1',frame)
    cv2.imshow('frame2',gray)
    
    #
    #Stereo test, need to download matplotlib to do disparity map
    #stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
    #disparity = stereo.compute(frame2, frame3)
    #cv2.imshow('disparity', disparity)
    #
    #
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
