from src.modules.PicProcessingSettings import PicProcessingSettings
from src.modules.ImageProcessing import ImageProcessing

class PicProcessingApp(object):
    def __init__(self,image):
        self.image = image
        self.settings = PicProcessingSettings(self.image)
        self.imageProcessing = ImageProcessing(self.image)
        
    def setImage(self,image):
        self.image = image
        self.imageProcessing.setImage(image)
    
    def rotate(self):
        return self.imageProcessing.rotate()
    
    def grayscale(self):
        return self.imageProcessing.grayscale()
        
    def invert(self,value=0):
        return self.imageProcessing.invert(value)
    
    def histogram(self):
        return
    
    def manualThresholding(self,threshold=127):
        return self.imageProcessing.threshold(threshold)

    def otsu(self):
        return self.imageProcessing.otsu()
    
    def erosion(self,kernel=None,iterations=1):
        return self.imageProcessing.erosion(kernel=kernel,iterations=iterations)
    
    def dilation(self,kernel=None,iterations=1):
        return self.imageProcessing.dilation(kernel=kernel,iterations=iterations)
    
    def opening(self,kernel=None,iterations=1):
        return self.imageProcessing.opening(kernel=kernel,iterations=iterations)
    
    def closing(self,kernel=None,iterations=1):
        return self.imageProcessing.closing(kernel=kernel,iterations=iterations)
    
    def meanBlur(self,kernel_size=None):
        return self.imageProcessing.mean_filter(kernel_size=kernel_size)
    
    def medianBlur(self,kernel_size=None):
        return self.imageProcessing.median_filter(kernel_size=kernel_size)
    
    def gaussianBlur(self,kernel_size=None,sigma=None):
        return self.imageProcessing.gaussian_blur(kernel_size=kernel_size,sigma=sigma)
    
    def gradiant(self):
        return self.imageProcessing.gradiant()
    
    def sobel(self):
        return self.imageProcessing.sobel()
    
    def laplacian(self):
        return self.imageProcessing.laplacian()
    
    def canny(self):
        return self.imageProcessing.canny()
    
    def hough(self):
        return self.imageProcessing.hough()
    
    def sift(self):
        return self.imageProcessing.sift()
    
    def harris(self):
        return self.imageProcessing.harris()
    
    def roberts(self):
        return self.imageProcessing.roberts()
    
    def prewitt(self):
        return self.imageProcessing.prewitt()
        
    def kirsch(self):
        return self.imageProcessing.kirsch()
    
    def undo(self):
        self.settings.undoLastImageAction()
        return
    
    def reset(self):
        self.settings.resetImage()
        return