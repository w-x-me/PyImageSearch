from __future__ import print_function
import numpy as np 
import imutils

import cv2
images = cv2.imread("../next.png")
orig = images.copy()
gray = cv2.cvtColor(images,  cv2.COLOR_BGR2GRAY)

if imutils.is_cv2():
    detector = cv2.FeatureDetector_create("SIFT")
    kps = detector.detect(gray)

else:
    detector = cv2.xfeatures2d.SIFT_create()
    (kps, _) = detector.detectAndCompute(gray, None)

print("#of keypoints:{}".format(len(kps)))

for kp in kps:
    r = int(0.5 * kp.size)
    (x, y) = np.int0(kp.pt)
    cv2.circle(images, (x, y), r, (0, 255, 255), 2)

cv2.imshow("Images", np.hstack([orig, images]))
cv2.waitKey(0)
