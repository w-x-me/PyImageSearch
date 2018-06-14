#coding=utf-8
import numpy as np
import argparse
import cv2
 
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
 
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray, 255, 50)
cv2.imshow("Edge Map", edged)
cv2.imshow("Original", image)
"""i = 0
j = 0
while i<250:
    while j<250:
        image = cv2.imread(args["image"])
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(gray, i, j)
        cv2.imshow(("Edge Map %d %d")%(i, j), edged)
        j = j + 50
        (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:1]

        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.1 * peri, True)
        
            print "original:{}, approx:{}".format(len(c), len(approx))

            cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)

            cv2.imshow("Output", image)
            cv2.waitKey(0)
    i = i + 50
    j = 0"""
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]

for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.01 * peri, True)

    print "original:{}, approx:{}".format(len(c), len(approx))

    cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)

    cv2.imshow("Output", image)
    cv2.waitKey(0)

    #if len(approx)==4:
     #   cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)

#cv2.imshow("Output", image)
#cv2.waitKey(0)
