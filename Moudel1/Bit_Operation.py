#coding=utf-8
import numpy as np
import cv2

#rectangle = np.zeros((300, 300), dtype = "uint8")
#cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
rectangle = cv2.imread("../Image/People2.jpg")
(rectangle, g, r) = cv2.split(rectangle)
cv2.imshow("Rectangle", rectangle)

circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
#circle = cv2.imread("../Image/People2.jpg")

circle = np.zeros(rectangle.shape[:2], dtype = "uint8")
cv2.rectangle(circle, (50,50), (750, 750), 255, -1)
cv2.imshow("Circle", circle)
#cv2.waitKey(0)

bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("And", bitwiseAnd)
cv2.waitKey(0)

bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)
