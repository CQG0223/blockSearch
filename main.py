from core import getSAD
import cv2

imgLPath = '/media/cqg/CQG/CQGData/3L3DR_Res/C0010/recded/L/7_16.bmp'
imgRPath = '/media/cqg/CQG/CQGData/3L3DR_Res/C0010/recded/R/7_16.bmp'

if __name__ == '__main__':
    imgL = cv2.imread(imgLPath,0)
    imgR = cv2.imread(imgRPath,0)
    getSAD(imgL,imgR)