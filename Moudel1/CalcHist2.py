from matplotlib import pyplot as plt
import numpy as np
import cv2

def plot_histogram(image, title, mask = None):
    chans = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of Pixel")

    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
        plt.plot(hist, color = color)
        plt.xlim([0, 256])
image = cv2.imread("../Image/beach.png")
cv2.imshow("Original", image)
cv2.waitKey(0)
plot_histogram(image, "Histogram for Original Image")

mask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.rectangle(mask, (60, 290), (210, 390), 255,  - 1)
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Applying the Mask", masked)

plot_histogram(image, "Histogram for Masked Image", mask = mask)
plt.show()
