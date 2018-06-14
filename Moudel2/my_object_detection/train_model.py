from __future__ import print_function
from pyimagesearch.utils import dataset
from pyimagesearch.utils.conf import Conf
from sklearn.svm import SVC
import argparse
import pickle
import numpy as np

ap  = argparse.ArgumentParser()
ap.add_argument("-c", "--conf", required = True, help = "path to the configuration file")
ap.add_argument("-n", "--hard-negatives", type = int, default = -1, help="flag indicating whether or not hard negatives should be used")
args = vars(ap.parse_args())

print("[INFO] loading dataset...")
conf = Conf(args["conf"])
(data, labels) = dataset.load_dataset(conf["features_path"], "features")

if args["hard_negatives"] > 0:
    print("[INFO] loading hard negatives...")
    (hardData,hardLabels) = dataset.load_dataset(conf["features_path"], "hard_negatives")
    data = np.vstack([data, hardData])
    labels = np.hstack([labels, hardLabels])

print("[INFO] training classifier...")
model = SVC(kernel = "linear", C = conf["C"], probability = True, random_state = 42)
model.fit(data, labels)

print("[INFO] dumping classifier...")
f = open(conf["classifier_path"], "wb")
f.write(pickle.dumps(model))
f.close()

