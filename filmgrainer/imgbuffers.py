
from PIL import Image
import numpy as np


class RgbBuffer:
    def __init__(self, data):
        self._Data = data
        self.Width = data.shape[1]
        self.Height = data.shape[0]
        
    @staticmethod
    def fromZeros(width, height):
        return RgbBuffer(np.zeros([height, width, 3], dtype=np.uint8))
    
    @staticmethod
    def fromImg(img):
        data = np.array(img)
        if len(data.shape) == 3:
            return RgbBuffer(data)
        else:
            return GrayBuffer(data)

    def toImg(self):
        return Image.fromarray(self._Data)
        
    def getRgb(self, x, y):
        return (self._Data[y, x, 0], self._Data[y, x, 1], self._Data[y, x, 2])
    
    def setRgb(self, x, y, rgb_tuple):
        self._Data[y, x, 0] = rgb_tuple[0]
        self._Data[y, x, 1] = rgb_tuple[1]
        self._Data[y, x, 2] = rgb_tuple[2]


class GrayBuffer:
    def __init__(self, data):
        self._Data = data
        self.Width = data.shape[1]
        self.Height = data.shape[0]
        
    @staticmethod
    def fromZeros(width, height):
        return GrayBuffer(np.zeros([height, width], dtype=np.uint8))
    
    def toImg(self):
        return Image.fromarray(self._Data)
        
    def getRgb(self, x, y):
        return (self._Data[y, x], self._Data[y, x], self._Data[y, x])

    def getGray(self, x, y):
        return self._Data[y, x]

    def setGray(self, x, y, value):
        self._Data[y, x] = value


class IntBuffer:
    def __init__(self, width, height):
        self._Data = np.zeros([width, height], dtype=np.int)
        self.Width = width
        self.Height = height
        
    def getInt(self, x, y):
        return self._Data[x, y]
        
    def setInt(self, x, y, value):
        self._Data[x, y] = value
