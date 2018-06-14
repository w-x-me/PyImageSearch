#coding=utf-8
import numpy as np
import cv2

image = cv2.imread("../Image/People.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#thresh = cv2.threshold(gray, 255, 255, cv2.THRESH_BINARY_INV)[1]
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Original", image)
cv2.imshow("Thresh", thresh)

(cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
hullImage = np.zeros(gray.shape[:2], dtype = "uint8")

for (i, c) in enumerate(cnts):
    area  =  cv2.contourArea(c)
    (x,  y,  w,  h)  =  cv2.boundingRect(c)
   # area = cv2.contourArea(c)
   # (x, y, w, h) = cv2.boundingRect(c)
    aspectRatio  =  w / float(h)
   # aspectRatio = w / float(h)
    extent = area / float(w * h)
   #extent = area / float(w * h)

    hull = cv2.convexHull(c)
    hullArea = cv2.contourArea(hull)
    solidity = area / float(hullArea)

    cv2.drawContours(hullImage,[hull],-1,255,-1)
    cv2.drawContours(image,  [c],-1,(240,0,159),3)
    
    #cv2.drawContours(hullImage, [hull], -1, 255, -1)
    #cv2.drawContours(image, [c], -1, (240, 0, 159), 3)
    shape = ""

    if aspectRatio >= 0.98 and aspectRatio <= 1.02:
        shape = "SQUARE"

    elif aspectRatio >= 3.0:
        shape = "RECTANGLE"

    elif extent < 0.65:
        shape = "L-PIECE"

    elif solidity > 0.80:
        shape = "Z-PIECE"

    cv2.putText(image, shape, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (240, 0, 159), 2) 

    print "Contour #%d -- aspect_ratio =%.2f, extent=%.2f, solidity = %.2f"%(i + 1, aspectRatio, extent, solidity)

    cv2.imshow("Convex Hull", hullImage)
    cv2.imshow("Image", image)
    cv2.waitKey(0) 
