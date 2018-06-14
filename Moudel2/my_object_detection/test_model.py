from pyimagesearch.object_detection.nms import non_max_suppression
from pyimagesearch.object_detection.objectdetector import ObjectDetector 
from pyimagesearch.descriptors.hog import HOG
from pyimagesearch.utils.conf import Conf
import numpy as np
import imutils
import argparse
import pickle
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--conf", required = True, help = "path to the configuration file")
ap.add_argument("-i", "--image", required = True, help = "path to the image to be classified")
args = vars(ap.parse_args())
conf = Conf(args["conf"])

model = pickle.loads(open(conf["classifier_path"], "rb").read())
#hog = HOG(orientations = conf["orientations"], pixelsPerCell = tuple(conf["pixels_per_cell"]), cellsPerBlock = tuple(conf["cells_per_block"]), normalize = conf["normalize"], block_norm = "L1")
hog =HOG(orientations = conf["orientations"],  pixelsPerCell = tuple(conf["pixels_per_cell"]), 
    cellsPerBlock = tuple(conf["cells_per_block"]),  normalize = conf["normalize"])
od = ObjectDetector(model, hog)

image = cv2.imread(args["image"])
image = imutils.resize(image, width = min(260, image.shape[1]))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
(boxes, probs) = od.detect(gray, conf["window_dim"], winStep = conf["window_step"], pyramidScale = conf["pyramid_scale"], minProb = conf["min_probability"])
pick = non_max_suppression(np.array(boxes), probs, conf["overlap_thresh"])
print ("return pick")
print pick
orig = image.copy()
for (startX, startY, endX, endY) in boxes:
    cv2.rectangle(orig, (startX, startY), (endX, endY), (0, 0, 255), 2)

#    cv2.imshow("Ori", orig)
 #   cv2.waitKey(0)
for (startX, startY, endX, endY) in pick:
    cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255,0), 2)
cv2.imshow("Original", orig)
cv2.imshow("Image", image)
cv2.waitKey(0)

