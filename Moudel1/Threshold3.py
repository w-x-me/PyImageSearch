from skimage.filters import threshold_adaptive
import argparse
import cv2

ap = argparse.ArgumenParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 25, 15)
cv2.imshow("OpenCV Mean Thresh", thresh)

thresh = threshold_adaptive(blurred, 29, offset = 5).astype("uint8") * 255
thresh = cv2.bitwise_not(thresh)
cv2.imshow("scikit-image Mean Thresh", thresh)
cv2.waitKey(0)
