import numpy as np

def non_max_suppression(boxes, probs, overlapThresh):
    if len(boxes) == 0:
        return []

    if boxes.dtype.kind == "i":
        boxes = boxes.astype("float")

    pick = []
    print ("boxes")
    print (boxes)
    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    print ("y1")
    print (y1)
    x2 = boxes[:, 2]
    y2 = boxes[:, 3]

    area = (x2 - x1 + 1) * (y2  - y1  + 1)
    print ("area")
    print (area)
    idxs = np.argsort(probs)
    print ("idxs")
    print (idxs)
    while len(idxs) > 0:
        last = len(idxs) - 1
        i = idxs[last]
        pick.append(i)


        xx1 = np.maximum(x1[i], x1[idxs[:last]])
        yy1 = np.maximum(y1[i], y1[idxs[:last]])
        xx2 = np.minimum(x2[i], x2[idxs[:last]])
        yy2 = np.minimum(y2[i], y2[idxs[:last]])
        print ("xx1, yy1, xx2, yy2")
        print (xx1, yy1, xx2, yy2)

        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)


        overlap = (w * h)/area[idxs[:last]]
        print ("overlap")
        print (overlap)

	idxs = np.delete(idxs, np.concatenate(([last],
			np.where(overlap > overlapThresh)[0])))
        print ("idxs")
        print idxs
    return boxes[pick].astype("int")


