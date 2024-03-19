import cv2

class Posion:
    def __init__(self,box):
        self.index = 0
        self.PosionList = [box]
    """
    def __init__(self,x,y,w,h):
        self.index = 0
        self.PosionList = [self.__invert__(x,y,w,h)]
        """
    def Cappend(self,x,y,w,h):
        self.PosionList.append(self.__invert__(x,y,w,h))
    def __len__(self):
        return len(self.PosionList)
    def __invert__(self,x,y,w,h):
        return [(int(x - w/2),int(y - h/2)),(int(x + w/2),int(y + h/2))]
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.PosionList):
            raise StopIteration
        else:
            val = self.PosionList[self.index]
            self.index += 1
            return val

def rectangele(img,PosionList):
    img = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
    if PosionList is None:
        return img
    if (len(PosionList) is not 0):
        for Posion in PosionList:
            cv2.rectangle(img,Posion[0],Posion[1],(0,0,255),3)
        return img
        