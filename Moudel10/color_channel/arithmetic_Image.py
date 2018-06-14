import numpy as np
import argparse
import cv2

image = cv2.imread("./dinos/trex_01.png")
M = np.ones(image.shape, dtype = "uint8") * 100
added = cv2.add(image, M)
cv2.imwrite("./dinos/trex_05.png", added)
