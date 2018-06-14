import cv2

image = cv2.imread("../Image/People.jpg")
cv2.imshow("Original", image)

(h, w) = image.shape[:2]
print h, w

face = image[35:468, 405:1136]
cv2.imshow("Face", face)
cv2.waitKey(0)
