#coding=utf-8
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

gX = cv2.Sobel(gray, ddepth = cv2.CV_64F, dx = 1, dy = 0)
gY = cv2.Sobel(gray, ddepth = cv2.CV_64F, dx = 0, dy = 1)

gX = cv2.convertScaleAbs(gX)
gY = cv2.convertScaleAbs(gY)

sobleCombined = cv2.addWeighted(gX, 0.5, gY, 0.5, 0)

cv2.imshow("Sobel X", gX)
cv2.imshow("Sobel Y", gY)
cv2.imshow("Sobel Combined", sobleCombined)
cv2.waitKey(0)
