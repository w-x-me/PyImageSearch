from __future__ import print_function
import argparse
import dlib

ap = argparse.ArgumentParser()
ap.add_argument("-x", "--xml", required = True, help = "path to input XML file")
ap.add_argument("-d", "--detector", required = True, help = "path to output director")
args = vars(ap.parse_args())

print("[INFO] training detector....")
options = dlib.simple_object_detector_training_options()
options.C = 1.0
options.num_threads = 4
options.bei_verbose = True
dlib.train_simple_object_detector(args["xml"], args["detector"], options)

print("[INFO] training accuracy:{}".format(dlib.test_simple_object_detector(args["xml"], args["detector"])))

detector = dlib.simple_object_detector(args["detector"])
win = dlib.image_window()
win.set_image(detector)
dlib.hit_enter_to_continue()

