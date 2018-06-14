import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)

cv2.imshow("Original", image)
cv2.imshow("Blurred", blurred)

wide = cv2.Canny(blurred, 10, 20)
mid = cv2.Canny(blurred, 30, 50)
tight = cv2.Canny(blurred, 240, 250)

cv2.imshow("Wide Edge Map", wide)
cv2.imshow("Mide Edge Map", mid)
cv2.imshow("Tight Edge Map", tight)
cv2.waitKey(0)
