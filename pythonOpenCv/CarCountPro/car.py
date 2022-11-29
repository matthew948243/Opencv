# -*- coding: utf-8 -*- 
# @Time : 2022/11/11 19:03
# @Author : KeJun 
# @File : car.py
# @IDE ：PyCharm
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

min_w = 120
min_h = 100
line_high = 600
offset = 9
cars=[]
#计算外接矩形的中心
def center(x,y,w,h):
    x1=int(w/2)
    y1=int(h/2)
    cx=int(x)+x1
    cy=int(y)+y1
    return cx,cy

def Video():
    # "../images/video.mp4"
    vc = cv2.VideoCapture("../images/video2.mp4")  # 写0代表的是摄像头

    mog= cv2.bgsegm.createBackgroundSubtractorMOG()
    if vc.isOpened():
        op = vc.read()
    else:
        op = False
    # i=0
    # flag=80
    carno=0
    while vc.isOpened():  # op

        # if i<flag:
        #     i += 1
        #     ret, frame = vc.read()
        #     continue;

        ret, frame = vc.read()
        # if frame is None:
        #     break
        kernerl = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
        # if ret and i>=flag:
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            #去噪
            blur=cv2.GaussianBlur(gray,(3,3),5)
            #得到前景
            mask = mog.apply(blur)

            #腐蚀
            erode=cv2.erode(mask,kernerl)
            # 膨胀
            dilate = cv2.dilate(erode, kernerl,iterations=2)
            #闭运算
            close=cv2.morphologyEx(dilate,cv2.MORPH_CLOSE,kernerl)

            #查找轮廓
            contours,hierarch= cv2.findContours(close,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

            cv2.line(frame,(10,line_high),(2000,line_high),(255,255,0),2)
            #画出所有的轮廓
            for contour in contours:
                #最大的轮廓
                x,y,w,h=cv2.boundingRect(contour)
                is_valid=(w>min_w) and (h>min_h)
                if not is_valid:
                    continue
                #转整数
                cv2.rectangle(frame,(int(x),int(y)),(int(x+w),int(y+h)),(0,0,255),thickness=2)
                cpoint=center(x,y,w,h)
                cv2.circle(frame,(cpoint),5,(0,0,255),-1)
                cars.append(cpoint)
                for(x,y) in cars:
                    if y>(line_high-offset) and y<(line_high+offset):
                        carno=carno+1
                        cars.remove((x,y))
            cv2.putText(frame,"Vehicle Count:"+str(carno),(500,60),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),5)
            cv2.imshow("result", frame)

        if cv2.waitKey(10) & 0xFF == 27:
            break
    vc.release()
    cv2.destroyAllWindows()

Video()