from . import helpers
import cv2
import numpy
import time
class ObjectDetector:
    def __init__(self, model, desc):
        self.model = model
        self.desc = desc

    def detect(self,image, winDim, winStep = 4, pyramidScale = 1.5, minProb = 0.7):
        boxes = []
        probs = []

        for layer in helpers.pyramid(image, scale = pyramidScale, minSize = winDim):
            scale = image.shape[0]/float(layer.shape[0])

            for (x, y, window) in helpers.sliding_window(layer, winStep, winDim):
                (winH, winW) = window.shape[:2]

                if winH == winDim[1] and winW == winDim[0]:
                    features = self.desc.describe(window).reshape(1,-1)
                    prob = self.model.predict_proba(features)[0][1]
                   # clone = layer.copy()
                   # cv2.rectangle(clone,(x,y),(x+winW,y+winH),(0,255,0),2)
                    #cv2.imshow("Window",  clone)         
                    #cv2.waitKey(1)
                    #time.sleep(0.025)
                    if prob > minProb:
                        print (" -  - ")
                        (startX, startY) = (int(scale * x), int(scale * y))
                        endX = int(startX + (scale * winW))
                        endY = int(startY + (scale * winH))

                        boxes.append((startX, startY, endX, endY))
                        probs.append(prob)
        return (boxes, probs)

