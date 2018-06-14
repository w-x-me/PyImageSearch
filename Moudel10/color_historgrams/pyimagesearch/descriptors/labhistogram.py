#coding=utf-8
import cv2
import imutils

class LabHistogram:
    def __init__(self, bins):
        self.bins = bins

    def describe(self, image, mask = None):
        #将图片有RGB格式转换成LAB
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        #获取3D直方图
        hist = cv2.calcHist([lab], [0, 1, 2], mask, self.bins, [0, 256, 0, 256, 0, 256])

        if imutils.is_cv2():
            hist = cv2.normalize(hist).flatten()
        else:
            hist = cv2.normalize(hist, hist).flatten()
        return hist
