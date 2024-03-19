from .SAD import SAD
import numpy as np

def getSAD(Src,Tar):
    A = SAD(101,10000)      #第一个参数：窗口大小；第二个参数：最大视差
    mask = Tar > 0
    A.cacualte(Src,Tar,mask)