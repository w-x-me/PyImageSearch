#coding=utf-8
import numpy as np
import cv2
backgroud=(128,0,128)
#设置画布大小
canvas=np.zeros((300,300,3),dtype="uint8")
#设置线条颜色为绿色
green=(0,255,0)
#设置直线起点坐标位置和终点坐标位置
cv2.line(canvas,(0,0),(300,300),green)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
#设置线条为红色
red=(0,0,255)
#设置线条的起始位置和终点位置,最后一个参数设置线条厚度（指线条宽度）
cv2.line(canvas,(300,0),(0,300),red,3)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
#矩形绘制
cv2.rectangle(canvas,(10,10),(60,60),green)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
#矩形线条厚度设置
cv2.rectangle(canvas,(50,200),(200,255),red)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
#设置矩形颜色，颜色值的输入和实际值想法（定理）
blue=(255,0,0)
#矩形绘制函数,运用负数就是填充
cv2.rectangle(canvas,(200,50),(225,125),blue,-1)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)

#画圆
#重新初始化一块画布
canvas=np.zeros((300,300,3),dtype="uint8")
(centerX,centerY)=(canvas.shape[1]/2,canvas.shape[0]/2)
white=(255,255,255)

for r in xrange(0,175,25):
    cv2.circle(canvas,(centerX,centerY),r,white, 3)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)

#画随机圆
for i in xrange(0,5):
    radius=np.random.randint(5,high=200)
    color=np.random.randint(0,high=256,size=(3,)).tolist()
    pt=np.random.randint(0,high=300,size=(2,))
    print radius
    print color
    print pt
    cv2.circle(canvas,tuple(pt),radius,color,-1)
    cv2.imshow("Canvas",canvas)
    cv2.waitKey(0)
cv2.waitKey(0)
