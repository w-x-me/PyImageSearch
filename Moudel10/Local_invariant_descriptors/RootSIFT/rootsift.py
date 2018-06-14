import numpy as np
import cv2
import imutils
class RootSIFT:
    def __init__(self):
        if imutils.is_cv2():
            self.extractor = cv2.DescriptorExtractor_create("SIFT")

        else:
            self.extractor = cv2.xfeatures2d.SIFT_create()

    def compute(self, image, kps, eps=1e-7):
        if imutils.is_cv2:
            (kps, descs) = self.extractor.compute(image, kps)
        else:
            (kps, descs) = self.extractor.detecAndCompute(image, None)

        if len(kps) == 0:
            return([], None)
        descs /= (descs.sum(axis = 1, keepdims = True) + eps) 
        descs = np.sqrt(descs)
        return (kps, descs)

