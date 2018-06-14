from scipy.spatial import distance as dist
import numpy as np
import mahotas
import cv2
import imutils

def describe_shapes(image):
    shapeFeatures = []
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (13, 13), 0)
    cv2.imshow("2", blurred)
    cv2.waitKey(0)
    thresh = cv2.threshold(blurred, 120, 255, cv2.THRESH_BINARY)[1]
    thresh  = cv2.dilate(thresh, None, iterations = 4)
    thres = cv2.erode(thresh, None, iterations = 2)
    
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    for c in cnts:
        mask = np.zeros(image.shape[:2], dtype = "uint8")
        cv2.drawContours(mask, [c], -1, 255, -1)
        (x, y, w, h) = cv2.boundingRect(c)
        roi = mask[y:y + h, x:x + w]
        features = mahotas.features.zernike_moments(roi, cv2.minEnclosingCircle(c)[1], degree = 8)
        print " -  -  -  -  -  -  -  -  -  -  - "
      #  features = mahotas.features.zernike_moments(roi, 200, degree = 8)
        #print cv2.minEnclosingCircle(c)[1]

        #print features
        shapeFeatures.append(features)


    return(cnts, shapeFeatures)

refImage = cv2.imread("2.jpg")
(_, gameFeatures)  = describe_shapes(refImage)
shapesImage = cv2.imread("1.jpg")
(cnts, shapeFeatures) = describe_shapes(shapesImage)
D = dist.cdist(gameFeatures, shapeFeatures)
print D
i = np.argmin(D)

for (j, c) in enumerate(cnts):
    
    if i != j:
        box = cv2.minAreaRect(c)
        #print "box"
        #print box
        #print i, j
        box = np.int0(cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box))
        cv2.drawContours(shapesImage, [box],  - 1, (0, 0, 255), 2)

box = cv2.minAreaRect(cnts[i])
print "box"
print box
box = np.int0(cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box))
cv2.drawContours(shapesImage, [box],  - 1, (0, 255, 0), 2)
(x, y, w, h) = cv2.boundingRect(cnts[i])

cv2.putText(shapesImage, "FOUND!", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 3)

cv2.imshow("Input Image", refImage)
cv2.imshow("Detected Shapes", shapesImage)
cv2.waitKey(0)



