from __future__ import print_function
import argparse
import cv2
import imutils
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
if imutils.is_cv2():
    detector = cv2.FeatureDetector_create("FAST")
    extractor = cv2.DescriptorExtractor_create("BRIEF")

else:
    detector = cv2.FastFeatureDetector_create()
    extractor = cv2.xfeatures2d.BriefDescriptorExtractor_create()

kps = detector.detect(gray)
(kps, descs) = extractor.compute(gray, kps)
print("[INFO] # of keypoints detected:{}".format(len(kps)))
print("[INFO] feature vector shape:{}".format(descs.shape))

