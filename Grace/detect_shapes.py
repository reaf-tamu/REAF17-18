from ShapeDetector import ShapeDetector
import imutils
import cv2

'''For single image'''
#IMAGE = "dice.jpg"

#image = cv2.imread(IMAGE)
#resized = imutils.resize(image, width=300)
#ratio = image.shape[0] / float(resized.shape[0])

#gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
#blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#thresh = cv2.threshold(blurred, 60, 50, cv2.THRESH_BINARY)[1]

#cv2.imshow("Threshold", thresh)

'''For video feed'''

cap = cv2.VideoCapture(0)
sd = ShapeDetector()

while(True):
    ret, image = cap.read()
    resized = imutils.resize(image, width=300)
    ratio = image.shape[0] / float(resized.shape[0])

    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 100, 50, cv2.THRESH_BINARY)[1]

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    hierarchy = cnts[-1]
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]

    cv2.imshow("Threshold", thresh)
    #print("contours")
    #print (cnts)
    #print("hierarchy")
    hierarchy = hierarchy[0]
    #print(hierarchy)
    # loop over the contours
    i = 0
    for c in cnts:
        if(hierarchy[i][3] == -1):
            # compute the center of the contour, then detect the name of the
            # shape using only the contour
            shape = sd.detect(c)
            if(shape == "square"):
                numPips = hierarchy[i][0] - i - 1
                # multiply the contour (x, y)-coordinates by the resize ratio,
                # then draw the contours and the name of the shape on the image
                M = cv2.moments(c)
                cX = int((M["m10"] / M["m00"]) * ratio)
                cY = int((M["m01"] / M["m00"]) * ratio)
                c = c.astype("float")
                c *= ratio
                c = c.astype("int")
                cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
                if(numPips > 0):
                    cv2.putText(image, str(numPips), (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                    #cv2.putText(image, str(numPips), (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                # show the output image
        i += 1
    cv2.imshow("Image", image)
    #cv2.waitKey(0)
    #input("continue?")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
