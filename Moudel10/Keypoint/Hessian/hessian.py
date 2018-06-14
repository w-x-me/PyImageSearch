from __future__ import print_function
import numpy as np
import cv2
import imutils

image = cv2.imread("../next.png")
orig = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
if imutils.is_cv2():
    detector = cv2.FeatureDetector_create("SURF")
    kps = detector.detect(gray)

else:
    detector = cv2.xfeatures2d.SURF_create()
    (kps, _) = detector.detectAndCompute(gray, None)

print ("# of keypoints:{}".format(len(kps)))

for kp in kps:
    r = int(0.5 * kp.size)
    (x, y)  = np.int0(kp.pt)
    cv2.circle(image, (x, y), r, (0, 255, 255), 2)

cv2.imshow("Images", np.hstack([orig, image]))
cv2.waitKey(0)
