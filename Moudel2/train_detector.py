#coding=utf-8
from __future__ import print_function
from imutils import paths
from scipy.io import loadmat
from skimage import io
import argparse
import dlib

ap = argparse
ap.add_argument("-c", "--class", required = True, help = "Path to the CALTECH-101 class images")
ap.add_argument("-a", "--annotations", required = True, help = "Path to the CALTECH-101 class annotations")
ap.add_argument("-o", "--output", required = True, help = "Path to the output detector")
args = vars(ap.parse_args())

print("[INFO] gathering images and bounding boxes...")
options = dlib.simple_object_detector_training_options()
images = []
boxes = []

for imagePath in paths.list_images(args["class"]):
    imageID = imagePath[imagePath.rfind("/") + 1:].split("_")[1]
    imageID = imageID.replace(".jpg", "")
    p = "{}/annotation_{}.mat".format(args["annotations"], imageID)
    annotations = loadmat(p)["box_coord"]

    bb = [dlib.rectangle(left = long(x), top = long(y), right = long(w), bottom = long(h)) for (y, h, x, w) in annotations]

    boxes.append(bb)

    images.append(io.imread(imagePath))
