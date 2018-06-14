#coding=utf-8
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required= True, help= "Path to the image")
args= vars(ap.parse_args())
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

#获取新图形与原图形宽的比例
r = 550.0 / image.shape[1]
#设置新图形的尺寸高，宽大小
dim = (550, int(image.shape[0] * r))
#将图形转化
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized(with)", resized)

#获取新图形与原图形宽的比例
r = 1250.0 / image.shape[0]
#设置新图形的尺寸高，宽大小
dim = (int(image.shape[0] * r), 1250)
#将图形转化
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized(high)", resized)

#运用imutils模块函数
resized = imutils.resize(image, width = 100)
cv2.imshow("Resized via Function", resized)

#图像放大，不运用插值
resized = imutils.resize(image, width = int(image.shape[1] * 0.5))
cv2.imshow("Resized Big", resized)
#图像放大，运用插值法

methods = [("cv2.INTER_NEAREST", cv2.INTER_NEAREST), ("cv2.INTER_LINEAR", cv2.INTER_LINEAR), ("cv2.INTER_AREA",cv2.INTER_AREA ), ("cv2.INTER_CUBIC", cv2.INTER_CUBIC), ("cv2.INITER_LANCZOS4", cv2.INTER_LANCZOS4)]

for (name, method) in methods:
    resized = imutils.resize(image, width = int(image.shape[1] *2.5 ), inter = method)
    cv2.imshow("Method:{}".format(name), resized)   
    cv2.waitKey(0)
cv2.waitKey(0)
