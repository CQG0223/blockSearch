from .visualization import Posion,rectangele
import cv2
import numpy as np


def pairShow(imgL,imgR,BoxL=None,BoxR=None,result = None):
    imgL = rectangele(imgL,BoxL)
    imgR = rectangele(imgR,BoxR)
    cv2.namedWindow("L", cv2.WINDOW_NORMAL)
    cv2.imshow('L',imgL)
    cv2.namedWindow("R", cv2.WINDOW_NORMAL)
    cv2.imshow('R',imgR)
    if result is not None:
        result_nor = cv2.normalize(result.astype(np.float32),None,0,255,cv2.NORM_MINMAX)
        result_nor = result_nor.astype(np.uint8)
        cv2.namedWindow("result",cv2.WINDOW_NORMAL)
        cv2.imshow('result',result_nor)
    cv2.waitKey(20)

def singleShow(img,Box = None):
    if Box is not None:
        img = rectangele(img,Box)
    cv2.namedWindow("Single", cv2.WINDOW_NORMAL)
    cv2.imshow('Single',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def test(img):
    #img = np.zeros((2048, 4048),np.uint8)
    rec1 = Posion(100,100,50,50)
    rec1.Cappend(1000,1000,200,200)
    print("Number box is : {}".format(len(rec1)))
    img = rectangele(img,rec1)
    cv2.namedWindow("rectangle", cv2.WINDOW_NORMAL)
    cv2.imshow('rectangle',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()