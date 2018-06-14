#coding=utf-8
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
print image[200, 800]
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#gray = image
print gray[200, 200]
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original1", image)
cv2.imshow("Gray", gray)
cv2.waitKey(0)

green = (0, 255, 0)
#侵蚀
print "开始出现侵蚀"
for i in xrange(0, 3):
    eroded = cv2.erode(gray.copy(), None, iterations = i + 1)
    cv2.imshow("Eroded{} times".format(i + 1), eroded)
    cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("Original2", image)

#扩张
print "开始出现扩张"
for i in xrange(0, 3):
    dilated = cv2.dilate(gray.copy(), None, iterations = i + 1)
    cv2.imshow("Dilated{} times".format(i + 1), dilated)
    cv2.waitKey(0)

#开盘
print "开始出现开盘"
cv2.destroyAllWindows()
image1 = cv2.imread("../Image/People2.jpg")
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original3", image1)
kernelSizes = [(3, 3), (5, 5), (7, 7)]

for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    opening = cv2.morphologyEx(gray1, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Opening:([{}, {}])".format(kernelSize[0], kernelSize[1]), opening)
    cv2.waitKey(0)

#闭幕
print "开始闭幕操作"
cv2.destroyAllWindows()
cv2.imshow("Original", image)

for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closing:({}, {})".format(kernelSize[0], kernelSize[1]), closing)
    cv2.waitKey(0)

#形态梯度
print "开始梯度形态操作"
cv2.destroyAllWindows()
cv2.imshow("Original", image)

for kernelSize in kernelSizes:
    kernel  = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    gradient  = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow("Gradient:({}, {})".format(kernelSize[0], kernelSize[1]), gradient)
    cv2.waitKey(0)

#顶帽/黑帽测试
print "车牌"
image1 = cv2.imread("../Image/car.png")
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
blackhat = cv2.morphologyEx(gray1, cv2.MORPH_BLACKHAT, rectKernel)

tophat = cv2.morphologyEx(gray1, cv2.MORPH_TOPHAT, rectKernel)

cv2.imshow("Original", image1)
cv2.imshow("Blackhat", blackhat)
cv2.imshow("Tophat", tophat)
cv2.waitKey(0)
