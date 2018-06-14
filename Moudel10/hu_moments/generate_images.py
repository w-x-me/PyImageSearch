import numpy as np
import argparse
import uuid
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required = True, help = "Path to the output directory")
ap.add_argument("-n", "--num-images", type=int, default=500, help = "# of disctrator images to generate")
args = vars(ap.parse_args())

for i in range(0, args["num_images"]):
    image = np.zeros((500, 500, 3), dtype = "uint8")
    topLeft = np.random.uniform(low = 25, high = 225, size = (2, )).astype("int0")
    botRight = np.random.uniform(low = 250, high = 400, size = (2, )).astype("int0")
    color = np.random.uniform(low = 0, high = 255, size = (3, )).astype("int0")
    color = tuple(map(int, color))
    cv2.rectangle(image, tuple(topLeft), tuple(botRight), color,  - 1)
    cv2.imwrite("{}/{}.jpg".format(args["output"], uuid.uuid4()), image)

image = np.zeros((500, 500, 3), dtype = "uint8")
(x, y) = np.random.uniform(low = 105, high = 405,  size = (2, )).astype("int0")
r = np.random.uniform(low = 25,high = 100, size = (1, )).astype("int0")[0]
color =np.random.uniform(low = 0, high = 255, size = (3, )).astype("int0") 
color = tuple(map(int, color))
cv2.circle(image, (x, y), r, color,  -1)
cv2.imwrite("{}/{}.jpg".format(args["output"], uuid.uuid4()), image)

