#coding=utf-8
import numpy as np
import argparse
import imutils
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the image")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
cv2.imshow("Original",image)
#cv2.waitKey(0)

#获得图像尺寸
(h,w)=image.shape[:2]
(cX,cY)=(w/2,h/2)


M=np.float32([[1,0,50],[0,1,50]])
rotated1=cv2.warpAffine(image,M,(w+100,h+100))
cv2.imshow("move50",rotated1)

#图像旋转矩阵设置，第一个参数，旋转圆心，第二个参数：旋转角度，第三个参数：旋转后的缩放比例
#M=cv2.getRotationMatrix2D((cX + 250,cY + 250),45,1.0)
#图像旋转，旋转图像，旋转矩阵，旋转后图像尺寸
#rotated=cv2.warpAffine(rotated,M,(w+500,h+500))
#cv2.imshow("Rotated by 45+50",rotated)


M=cv2.getRotationMatrix2D((cX,cY),0,1.5)
#rotated=cv2.warpAffine(image,M,(int(w * 1.3),int(h * 1.3)))
rotated=cv2.warpAffine(rotated1,M,(int(w * 1.5),int(h * 1.5)))
cv2.imshow("Rotated by 45",rotated)

M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", rotated)

#imutils模块的使用
rotated=imutils.rotate(image,180)
cv2.imshow("Rotated by 180 Degrees",rotated)
cv2.waitKey(0)
