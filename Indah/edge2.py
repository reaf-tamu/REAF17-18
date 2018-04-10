import cv2
import numpy as np
from matplotlib import pyplot as plt



cap = cv2.VideoCapture(0)
while(True):
	ret, frame = cap.read()
	
	blor=cv2.blur(frame, (4,4))
	edge = cv2.Canny(blor,100,200)
	circ=cv2.HoughCircles(edge,cv2.HOUGH_GRADIENT,2,100)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#blur= cv2.blur(frame,1) idk how to use blur
	
	if circ is not None:
		circ=np.round(circ[0,:].astype("int"))
		for (x,y,r) in circ:
			cv2.circle(edge,(x,y),r,(0,255,0),4)
	#cv2.imshow('original',frame)
	cv2.imshow('canny',edge)
	#cv2.imshow('grayscale',gray)
	cv2.imshow('blur',blor)
	
	#plt.imshow(edges,cmap = 'gray')
	#plt.xticks([]), plt.yticks([]) 
	#plt.show([])
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
    
    # When everything done, release the capture
cap.release()
cv2.destroyAllWindows()	