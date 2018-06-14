#coding=utf-8
#提取hog特征向量，并且写入数据库中
from __future__ import print_function

#from sklearn.feature_extraction.image import extract_patches_2d
from sklearn.feature_extraction.image import extract_patches_2d
from pyimagesearch.object_detection import helpers
from pyimagesearch.descriptors.hog import HOG
from pyimagesearch.utils import dataset
from pyimagesearch.utils.conf import Conf
from imutils import paths
from scipy import io
import numpy as np
import progressbar
import argparse
import random
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--conf", required = True, help = "path to the configuration file")
args = vars(ap.parse_args())

conf = Conf(args["conf"])

hog = HOG(orientations = conf["orientations"], pixelsPerCell = tuple(conf["pixels_per_cell"]), cellsPerBlock = tuple(conf["cells_per_block"]), normalize = conf["normalize"])
data = []
labels = []

trnPaths = list(paths.list_images(conf["image_dataset"]))
trnPaths = random.sample(trnPaths, int(len(trnPaths) * conf["percent_gt_images"]))
print("[INFO] describing training ROIs...")

widgets = ["Extracting: ", progressbar.Percentage(), " ", progressbar.Bar(), " ", progressbar.ETA()]
pbar = progressbar.ProgressBar(maxval = len(trnPaths), widgets = widgets).start()
myindex = 0
for (i, trnPath) in enumerate(trnPaths):
    image = cv2.imread(trnPath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    imageID = trnPath[trnPath.rfind("_") + 1:].replace(".jpg", "")

    p = "{}/annotation_{}.mat".format(conf["image_annotations"], imageID)
    bb = io.loadmat(p)["box_coord"][0]
    roi = helpers.crop_ct101_bb(image, bb, padding = conf["offset"], dstSize = tuple(conf["window_dim"]))

    if myindex < 3:
        cv2.imshow("roi1", roi)
        cv2.waitKey(0)
    rois = (roi, cv2.flip(roi, 1)) if conf["use_flip"] else (roi, )

    for roi in rois:
        if myindex < 3:
            cv2.imshow("roi", roi)
            cv2.waitKey(0)
        features = hog.describe(roi)
        data.append(features)
        labels.append(1)
    myindex = myindex + 1
    pbar.update(i)

pbar.finish()
dstPaths = list(paths.list_images(conf["image_distractions"]))
pbar = progressbar.ProgressBar(maxval = conf["num_distraction_images"], widgets = widgets).start()
print("[INFO], describing distraction ROIs...")

myindex = 0
for i in np.arange(0, conf["num_distraction_images"]):
    image = cv2.imread(random.choice(dstPaths))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    patches = extract_patches_2d(image, tuple(conf["window_dim"]), max_patches = conf["num_distractions_per_image"])

    for patch in patches:
        features = hog.describe(patch)
        if myindex < 10:
            print (features)
            print (" -  -  -  -  - ")
            myindex = myindex + 1
        data.append(features)
        labels.append(-1)

    pbar.update(i)
pbar.finish()
print("[INFO] dumping features and labels to file...")
dataset.dump_dataset(data, labels, conf["features_path"], "features")

