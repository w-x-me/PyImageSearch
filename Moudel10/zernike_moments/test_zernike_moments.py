import mahotas
import cv2
image = cv2.imread("checkmark.jpg")
#moments = mahotas.features.zernike_moments(image, 21, degree = 8)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
moments =mahotas.features.zernike_moments(image,  200,  degree = 3)

print moments
