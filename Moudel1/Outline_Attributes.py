#coding=utf-8
import numpy as np
import argparse
import cv2
 
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
 
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 9)
(cnts, _) = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
clone = image.copy()

#质心
print "质心"
for c in cnts:
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    cv2.circle(clone, (cX, cY), 10, (0, 255, 0),  -1)

cv2.imshow("Centroids", clone)
cv2.waitKey(0)
clone = image.copy()

#面积和周长
print "面积和周长"
for(i, c) in enumerate(cnts):
    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c, True)
    print "Contour #%d -- area:%.2f, perimetr:%.2f"%(i + 1, area, perimeter)
    
    cv2.drawContours(clone, [c], -1, (0, 255, 0), 2)
    
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    cv2.putText(clone, "#%d"%(i + 1), (cX - 20, cY), cv2.FONT_HERSHEY_SIMPLEX, 1.25, (255, 255, 255), 4)

cv2.imshow("Contours", clone)
cv2.waitKey(0)

#边框
print "边框"
clone = image.copy()
for c in cnts:
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(clone, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Bounding Boxes", clone)
cv2.waitKey(0)
clone = image.copy()

#旋转边框
print "旋转边框"
for c in cnts:
    box = cv2.minAreaRect(c)
    box = np.int0(cv2.cv.BoxPoints(box))
    cv2.drawContours(clone, [box], -1, (0, 255, 0), 2)

cv2.imshow("Rotated Bounding Boxes", clone)
cv2.waitKey(0)
clone = image.copy()

#最小封闭圆圈
print "最小封闭圆圈"
for c in cnts:
    ((x, y), radius) = cv2.minEnclosingCircle(c)
    cv2.circle(clone, (int(x), int(y)), int(radius), (0, 255, 0), 2)

cv2.imshow("Min-Enclosing Circles", clone)
cv2.waitKey(0)
clone = image.copy()

#拟合圆
print "拟合圆"
for c in cnts:
    if len(c)>=5:
        ellipse = cv2.fitEllipse(c)
        cv2.ellipse(clone, ellipse, (0, 255, 0), 2)

cv2.imshow("Ellipses", clone)
cv2.waitKey(0)
