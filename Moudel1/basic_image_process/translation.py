import numpy as np
import argparse
import imutils
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the image")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
cv2.imshow("Original",image)

M=np.float32([[1,0,-50],[0,1,-90]])
shifted=cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
cv2.imshow("Shifted",shifted)
print shifted.shape[:2]
M1=np.float32([[1,0,25],[0,1,45]])
shifted1=cv2.warpAffine(shifted,M1,(image.shape[1],image.shape[0]))
cv2.imshow("Shifted1",shifted1)
print shifted1.shape[:2]
cv2.waitKey(0)
