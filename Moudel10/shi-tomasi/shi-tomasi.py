from __future__ import print_function
import numpy as np
import cv2
import imutils

def gftt(gray, maxCorners = 0, qualityLevel = 0.01, minDistance = 1, mask = None, blockSize = 3, useHarrisDetector = False, k = 0.04):
    kps = cv2.goodFeaturesToTrack(gray, maxCornners, qualityLevel, minDistance, mask = mask, blockSize = blockSize, useHarrisDetector = useHarrisDetector, k = k)
    return [cv2.KeyPoint(pt[0][0], pt[0][1], 3) for pt in kps]

image = cv2.imread("next.png")
orig = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if imutils.is_cv2():
    detector = cv2.FeatureDetector_create("GFTT")
    kps = detector.detect(gray)

else:
    kps = gftt(gray)

for kp in kps :
    r = int(0.5 * kp.size)
    (x, y) = np.int0(kp.pt)
    cv2.circle(image, (x, y), r, (0, 255, 255), 2)

cv2.imshow("Images", np.hstack([orig, image]))
cv2.waitKey(0)
