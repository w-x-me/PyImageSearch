import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
(B, G, R) = cv2.split(image)
print "image:{}".format(image[117,890 ])
cv2.imshow("Red", R)
print "R:{}".format(R[117, 890])
cv2.imshow("Green", G)
print "G:{}".format(R[117, 890])
cv2.imshow("Blue", B)
print "B:{}".format(R[117, 890])
cv2.waitKey(0)

merged = cv2.merge([B, G, R])
print "merged:{}".format(merged[204, 390])
cv2.imshow("Merged", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

zeros = np.zeros(image.shape[:2], dtype = "uint8")
print zeros[90, 90]
cv2.imshow("Red",cv2.merge([zeros, zeros, R]))
print "Red:{}".format(cv2.merge([zeros, zeros, R])[90, 90])
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
print "Green:{}".format(cv2.merge([zeros, G, zeros])[90, 90])
cv2.imshow("Blue", cv2.merge([B, zeros, zeros,]))
print "Bule:{}".format(cv2.merge([B, zeros, zeros,])[90, 90])
cv2.imshow("Zeros", cv2.merge([zeros, zeros, zeros,]))
cv2.waitKey(0)

