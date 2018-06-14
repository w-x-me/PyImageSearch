#coding=utf-8
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
kernelSizes = [(3, 3), (9, 9), (15, 15)]

#平均模糊图像
for (kX, kY) in kernelSizes:
    blurred = cv2.blur(image, (kX, kY))
    cv2.imshow("Average({}, {})".format(kX, kY), blurred)
    cv2.waitKey(0)

print "高斯模糊图像"
cv2.destroyAllWindows()
cv2.imshow("Oringinal", image)
for (kX, kY) in kernelSizes:
    blurred = cv2.GaussianBlur(image, (kX, kY), 0)
    cv2.imshow("Gusssian({}, {})".format(kX, kY), blurred)
    cv2.waitKey(0)

print "中位数模糊法"
cv2.destroyAllWindows()
cv2.imshow("Originale", image)
for k in (3, 9, 15):
    blurred = cv2.medianBlur(image, k)
    cv2.imshow("Median{}".format(k), blurred)
    cv2.waitKey(0)

print "双边平滑模糊处理"
cv2.destroyAllWindows()
cv2.imshow("Originale", image)

params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]
i = 1
for (diameter, sigmaColor, sigmaSpace) in params:
    blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
    cv2.imshow("{}".format(sigmaColor), blurred)
    i = i + 1;
    cv2.waitKey(0)
