import cv2

image = cv2.imread("../Image/circles_and_squares.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

(cnts, _) = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in cnts:
    peri  = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.01*peri, True)
    if len(approx) ==4:
        cv2.drawContours(image, [c], -1,(0, 255, 255), 2)
        (x, y, w, h) = cv2.boundingRect(approx)
        cv2.putText(image, "Rectangle", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

cv2.imshow("Image", image)
cv2.waitKey(0)


