from __future__ import print_function
from skimage.filters import threshold_adaptive
from skimage import measure
import numpy as np
import cv2

plate = cv2.imread("../Image/license_plate.png")

v = cv2.split(cv2.cvtColor(plate, cv2.COLOR_BGR2HSV))[2]
thresh = threshold_adaptive(v, 29, offset = 15).astype("uint8") * 255
thresh = cv2.bitwise_not(thresh)

cv2.imshow("License Plate", plate)
cv2.imshow("Thresh", thresh)

labels = measure.label(thresh, neighbors = 8, background = 0)
mask = np.zeros(thresh.shape, dtype = "uint8")
print("[INFO] found {} blobs".format(len(np.unique(labels))))

for (i, label) in enumerate(np.unique(labels)):
    if label == 0:
        print("[INFO] label:0 (background)")
        continue
    print("[INFO] label: {} (foreground)".format(i))
    labelMask = np.zeros(thresh.shape, dtype = "uint8")
    labelMask[labels == label] = 255
    numPixels = cv2.countNonZero(labelMask)

    if numPixels > 300 and numPixels < 1500:
        mask = cv2.add(mask, labelMask)
    
    cv2.imshow("Label", labelMask)
    cv2.waitKey(0)

cv2.imshow("Large Blobs", mask)
cv2.waitKey(0)
