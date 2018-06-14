import cv2
import numpy as np
image = cv2.imread("7.bmp")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
(T, threshInv) = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("thresInv", threshInv)
cv2.imshow("thresInv_and_image", cv2.bitwise_and(image, image, mask = threshInv))

(T, thresh) = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)
cv2.imwrite("thres.png", thresh)
cv2.imshow("thres", thresh)

conner =  cv2.bitwise_and(image, image, mask = thresh)
cv2.imshow("conner", conner)
gray =cv2.cvtColor(image,  cv2.COLOR_BGR2GRAY)
ret,  corners =cv2.findChessboardCorners(gray,  (19,  19),  None)
criteria =(cv2.TERM_CRITERIA_EPS  +  cv2.TERM_CRITERIA_MAX_ITER,  30,  0.001)
objp =np.zeros((19 *19,  3),  np.float32)
objp[:,  :2] =np.mgrid[0:19,  0:19].T.reshape( - 1,  2)
objp =objp *20
objpoints =[]
imgpoints =[]
cv2.cornerSubPix(gray,corners,(11,11), (-1,-1),criteria)
cv2.drawChessboardCorners(image,  (19,  19),  corners,  ret)
cv2.imshow("conner1", image)
cv2.waitKey(0)
