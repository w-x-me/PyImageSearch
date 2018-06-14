import cv2
import imutils

image = cv2.imread("shape_explosion.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
moments = cv2.HuMoments(cv2.moments(image)).flatten()
print("PRIGINAL MOMENTS:{}".format(moments))
cv2.imshow("Image", image)
cv2.waitKey(0)

cnts = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]

for (i, c) in enumerate(cnts):
    (x, y, w, h) = cv2.boundingRect(c)
    roi = image[y:y + h, x:x + w]
    moments = cv2.HuMoments(cv2.moments(roi)).flatten()
    cv2.imshow("shape", roi)
    cv2.waitKey(0)
    print("MOMENTS FOT PLANE #{}:{}".format(i + 1, moments))
    if roi.shape[1] >  200:
        cv2.imshow("ROI #{}".format(i + 1), roi)
cv2.waitKey(0)

