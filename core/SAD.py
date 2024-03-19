import numpy as np
from .windowSplit import windowSplit,SlidingWindowGenerator
from visualization import Posion,pairShow

class SAD:
    def __init__(self,winSize,maxDisp) -> None:
        self.winSize = winSize
        self.Src = []
        self.Tar = []
        self.MaxDisp = maxDisp
    def cacualte(self,Sourse,target,mask):
        self.result = np.zeros_like(np.array(Sourse))
        h,w = Sourse.shape
        indices = np.argwhere(mask == 1)    #row行索引  col列索引
        for index in indices:
            row,col = index
            try:
                del win
            except:
                pass
            win = SlidingWindowGenerator(Sourse)
            windowsList = list(win.generate_windows(col,row,self.winSize,800,800))

            winTarget,box = self.__targetCut__(target,self.winSize,col,row)
            if col <= self.winSize/2:   #这里第一个数据表示纵向坐标
                continue
            old = np.inf
            winResult = windowsList[0]
            for winIndex in windowsList:
                new = self.__sad__(winIndex.image,winTarget)
                if new < old:
                    old = new
                    winResult = winIndex

            Tarbox = winResult.box
            Srcbox = [(box[0],box[2]),(box[1],box[3])]
            self.result[row,col] = self.__distance__(Tarbox,Srcbox)
            pairShow(Sourse,target,Posion(Tarbox),Posion(Srcbox),result=self.result)#绘图
            #print('row:{}'.format(row))
        return self.result
        

    def __sad__(self,Src,Tar):
        return np.sum(np.abs(Src - Tar))        #要改的地方，计算cost代价的位置
    
    def __targetCut__(self,target,winSize,x,y):
        xSize = (winSize-1)/2
        box = [x - xSize,x + xSize+1,y - xSize,y + xSize+1]
        box = [int(i) for i in box ]
        return target[box[2]:box[3],box[0]:box[1]],box
    
    def __distance__(self,tarbox,srcbox):
        return tarbox[0][0] - srcbox[0][0]
    
    def __binTest__(self,image):
        if image.size == 0:
            return 0
        else:
            return float(np.count_nonzero(image))/float(image.size)
