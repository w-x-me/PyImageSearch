from pyimagesearch.object_detection.objectdetector import ObjectDetector
from pyimagesearch.descriptors.hog import HOG
from pyimagesearch.utils.conf import Conf
import imutils
import argparse
import pickle
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--conf", required = True, help = "path to the configuration file")
ap.add_argument("-i", "--image", required = True, help = "path to the image to be classified")
args = vars(ap.parse_args())

conf  = Conf(args["conf"])

model = pickle.loads(open(conf["classifier_path"], "rb").read())
#hog = HOG(orientations = conf["orientations"], pixelsPerCell = tuple(conf["pixels_per_cell"]), cellsPerBlock = tuple(conf["cells_per_block"]), normalize = conf["normalize"])
hog = HOG(orientations = conf["orientations"], pixelsPerCell = tuple(conf["pixels_per_cell"]), cellsPerBlock = tuple(conf["cells_per_block"]), normalize = conf["normalize"])
od = ObjectDetector(model, hog)
image = cv2.imread(args["image"])
image = imutils.resize(image, width = min(260, image.shape[1]))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

(boxes,probs) =od.detect(gray,conf["window_dim"],winStep = conf["window_step"],pyramidScale =conf["pyramid_scale"],minProb = conf["min_probability"])
#(boxes, probs) = od.detect(gray, conf["window_dim"], winStep = conf["window_step"], pyramidScale = conf["pyramid_scale"], minProb = conf["min_probability"])

for (startX, startY, endX, endY) in boxes:
    cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)

cv2.imshow("Image", image)
cv2.waitKey(0)

