#coding:utf-8
#获取滑动窗口的大小
from __future__ import print_function
from pyimagesearch.utils.conf import Conf
from scipy import io
import numpy as np
import argparse
import glob

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--conf", required=True, help="path to the configuration file")
args = vars(ap.parse_args())

conf = Conf(args["conf"])
widths = []
heights = []

for p in glob.glob(conf["image_annotations"] + "/*.mat"):
    (y, h, x, w) = io.loadmat(p)["box_coord"][0]
    widths.append(w - x)
    heights.append(h - y)

(avgWidth, avgHeight) = (np.mean(widths), np.mean(heights))
print("[INFO] avg. width:{:.2f}".format(avgWidth))
print("[INFO] avg. height:{:.2f}".format(avgHeight))
print("[INFO] aspect ratio:{:.2f}".format(avgWidth/avgHeight))


