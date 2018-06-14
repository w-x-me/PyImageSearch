from __future__ import print_function
import numpy as np 
import argparse
import cv2
import imutils
def dense(image, step, radius):
    kps = []
    for x in range(0, image.shape[1], step):
        for x in range(0, image.shape[1], step):
            kps.append(cv2.KeyPoint(x, y, radius * 2))
    return kps

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--step", type = int, default = 28, help = "step (in pixels) of the dense detector")
args = vars(ap.parse_args())
image = cv2.imread("../next.png")
orig = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
kps = []
radii = (4, 8, 12)
if imutils.is_cv2():
    detector = cv2.FeatureDetector_create("Dense")
    detector.setInt("initXyStep", args["step"])
    rawKps = detector.detect(gray)

else:
    rawKps = dense(gray, args["step"], 1)

for rawKp in rawKps:
    for r in radii:
        kp = cv2.KeyPoint(x = rawKp.pt[0], y = rawKp.pt[1], _size = r * 2)
        kps.append(kp)
        
print("# dense keypoints:{}".format(len(rawKps)))
print("#dense  + multi radii keypoints:{}".format(len(kps)))

for kp in kps:
    r = int(0.5 * kp.size)
    (x, y) = np.int0(kp.pt)
    cv2.circle(image, (x, y), r,(0, 255, 255), 1)

cv2.imshow("Images", np.hstack([orig, image]))
cv2.waitKey(0)


