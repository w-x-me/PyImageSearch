from __future__ import print_function
from pyimagesearch.object_detection.objectdetector import ObjectDetector
from pyimagesearch.descriptors.hog import HOG
from pyimagesearch.utils import dataset
from pyimagesearch.utils.conf import Conf
from imutils import paths
import numpy as np
import progressbar
import argparse
import cPickle
import random
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--conf", required = True, help = "path to the configuration file")
args = vars(ap.parse_args())

conf =Conf(args["conf"])
data =[]

model =cPickle.loads(open(conf["classifier_path"]).read())
hog =HOG(orientations = conf["orientations"],  pixelsPerCell = tuple(conf["pixels_per_cell"]), 
    cellsPerBlock = tuple(conf["cells_per_block"]),  normalize = conf["normalize"])


od = ObjectDetector(model, hog)

dstPaths = list(paths.list_images(conf["image_distractions"]))
dstPaths =random.sample(dstPaths,  conf["hn_num_distraction_images"])

widgets = ["Mining:", progressbar.Percentage(), " ", progressbar.Bar(), "", progressbar.ETA()]
pbar = progressbar.ProgressBar(maxval = len(dstPaths), widgets = widgets).start()
myindex = 0
print ("2")
for (i, imagePath) in enumerate(dstPaths):
    image = cv2.imread(imagePath)
    print ("1")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("image",image )
    cv2.waitKey(0)
    (boxes, probs) = od.detect(gray, conf["window_dim"], winStep = conf["hn_window_step"], pyramidScale = conf["hn_pyramid_scale"], minProb = conf["hn_min_probability"])
    
    for (prob, (startX, startY, endX, endY)) in zip(probs, boxes):
        roi = cv2.resize(gray[startY:endY, startX:endX], tuple(conf["window_dim"]), interpolation = cv2.INTER_AREA)
        if myindex < 2:
            cv2.imshow("roi",roi )
            cv2.waitKey(0)
        features = hog.describe(roi)
        data.append(np.hstack([[prob], features]))
    myindex = myindex + 1 
    pbar.update(i)

pbar.finish()
print("[INFO] sorting by probability...")
data = np.array(data)
data = data[data[:, 0].argsort()[::-1]]

print("[INFO] dmping hard negatives to file...")
dataset.dump_dataset(data[:, 1:], [-1] * len(data), conf["features_path"], "hard_negatives", writeMethod = "a")

