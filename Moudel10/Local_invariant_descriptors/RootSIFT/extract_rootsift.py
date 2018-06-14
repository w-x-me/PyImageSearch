from __future__ import print_function
from rootsift import * 
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if imutils.is_cv2():
    detector = cv2.FeatureDetector_create("SIFT")
    extractor  = RootSIFT()
    kps = detector.detect(gray)

else:
    detector = cv2.xfeatureDetector_create("SIFT")
    extractor = RootSIFT()
    (kps, _) = detector.detect(grayi, None)

(kps, descs) = extractor.compute(gray, kps)
print("[INFO] # of keypoints detected:{}".format(len(kps)))
print("[INFO] feature vector shape:{}".format(descs.shape))
    

