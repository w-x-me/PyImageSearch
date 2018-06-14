from scipy.spatial import distance as dist
from imutils import paths
import numpy as np
import cv2

imagePaths = sorted(list(paths.list_images("dinos")))
print "imagePaths"
print imagePaths
index = {}
for imagePath in imagePaths:
    image = cv2.imread(imagePath)
    filename = imagePath[imagePath.rfind("/") + 1:]
    print "filename"
    print filename
    (means, stds) = cv2.meanStdDev(image)
    print "means"
    print means
    print "stds"
    print stds
    features = np.concatenate([means, stds]).flatten()
    print "features"
    print features
    index[filename] = features

query = cv2.imread(imagePaths[0])
cv2.imshow("Query (trex_01.png)", query)
keys = sorted(index.keys())
print "keys"
print keys
for (i, k) in enumerate(keys):
   # if k == "trex_01.png":
        #continue
    image = cv2.imread(imagePaths[i])
    d = dist.euclidean(index["trex_01.png"], index[k])
    cv2.putText(image, "%.2f"%(d), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
    cv2.imshow(k, image)
cv2.waitKey(0)
