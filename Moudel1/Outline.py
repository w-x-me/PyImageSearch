#coding=utf-8
import numpy as np
import argparse
import cv2
 
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
 
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
cv2.imshow("Original", image)

(cnts, _) = cv2.findContours(gray.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
clone = image.copy()
cv2.drawContours(clone, cnts, -1, (0, 255, 0), 2)
print "Found {} contours".format(len(cnts))

cv2.imshow("All Contours", clone)
cv2.waitKey(0)

clone = image.copy()

cv2.destroyAllWindows()
for(i, c) in enumerate(cnts):
    print "Drawing contour #{}".format(i + 1)
    cv2.drawContours(clone, [c], -1, (0, 255, 0), 2)
    cv2.imshow("Single Contour", clone)
    cv2.waitKey(0)

clone = image.copy()
cv2.destroyAllWindows()
(cnts, _) = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(clone, cnts, -1, (0, 255, 0), 2)
print "Found {} EXTERNAL contours".format(len(cnts))

cv2.imshow("All Contours", clone)
cv2.waitKey(0)

clone = image.copy()
cv2.destroyAllWindows()

for c in cnts:
    mask = np.zeros(gray.shape, dtype = "uint8")
    cv2.drawContours(mask, [c],  -1, 255,  -1)

    cv2.imshow("Image", image)
    cv2.imshow("Mask", mask)
    cv2.imshow("Image + Mask", cv2.bitwise_and(image, image, mask = mask))
    cv2.waitKey(0)
