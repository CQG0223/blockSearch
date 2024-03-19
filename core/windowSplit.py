import numpy as np

class WinAndBoxData:
    def __init__(self,img,Box) -> None:
        self.image = img
        xx = (Box[0],Box[2])
        yy = (Box[1],Box[3])
        self.box = [xx,yy]
        self.centerX = (int((Box[0] + Box[1])/2),int((Box[2] + Box[3])/2))

class windowSplit:
    def __init__(self,img,imgMax,winsize = 3,maxDisp = 10000):
        self.img = img
        self.windowSize = winsize
        self.h,self.w = self.img.shape
        self.window = []
        self.max = imgMax
        self.maxdisp = maxDisp
    
    def __index__(self,x,y):
        #windowAB = np.zeros(self.windowSize)
        xSize = (self.windowSize-1)/2
        box = [x - xSize,x + xSize+1,y - xSize,y + xSize+1]

        if (box[0] < 0 or box[2]<0 or box[1]>self.max or box[3]>self.max):
            return None
        box = [int(i) for i in box ]
        img = np.copy(self.img[box[2]:box[3],box[0]:box[1]])
        data = WinAndBoxData(img,box)
        
        return data

    def cacualate(self,y):
        for x in range(self.w):
            xx = self.__index__(x,y)
            if xx is not None:
                self.window.append(xx)

    def __iter__(self):
        return iter(self.window)
    
    def __len__(self):
        return len(self.window)
    
    def __getitem__(self,index):
        return self.window[index]


class SlidingWindowGenerator:
    def __init__(self, image):
        self.image = image
    
    def generate_windows(self, center_col,center_raw, window_size, num_windows_left, num_windows_right):
        _, width = self.image.shape
        halfStep = int((window_size - 1)/2)
        top = center_raw - halfStep
        for i in range(num_windows_left, -1, -1):
            left_col = center_col - halfStep - i
            if left_col + window_size > width or left_col < 0:
                continue  # 超出图像宽度，跳过该窗口
            box = [left_col,left_col+window_size- 1,top,top+window_size- 1]
            window = self.image[top:top+window_size , left_col:left_col+window_size ]
            data = WinAndBoxData(window,box)
            yield data
        
        for i in range(1, num_windows_right+1):
            right_col = center_col - halfStep + i
            if right_col + window_size > width or right_col < 0:
                continue  # 超出图像宽度，跳过该窗口
            box = [right_col,right_col+window_size - 1,top,top+window_size - 1]
            window = self.image[top:top+window_size, right_col:right_col+window_size]
            data = WinAndBoxData(window,box)
            yield data