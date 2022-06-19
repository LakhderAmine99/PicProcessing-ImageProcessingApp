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
    
    def rotate(self,angle=45):
        image = self.imageProcessing.rotate(angle)
        self.imageProcessing.setImage(image)
        return image
    
    def flip(self):
        image = self.imageProcessing.flip()
        self.imageProcessing.setImage(image)
        return image
    
    def zoomIn(self):
        image = self.imageProcessing.zoomIn()
        self.imageProcessing.setImage(image)
        return image
    
    def zoomOut(self):
        image = self.imageProcessing.zoomOut()
        self.imageProcessing.setImage(image)
        return image
    
    def grayscale(self):
        return self.imageProcessing.grayscale()
        
    def invert(self,value=0):
        return self.imageProcessing.invert(value)
    
    def contrast(self,value=0):
        return self.imageProcessing.contrast(value)
    
    def warmth(self,value=0):
        return self.imageProcessing.warmth(value)
    
    def hightlights(self,value):
        return self.imageProcessing.highlights(value)
    
    def saturation(self,value=0):
        return self.imageProcessing.saturation(value)
    
    def shadows(self,value=0):
        return self.imageProcessing.shadows(value)
    
    def tint(self,value=0):
        return self.imageProcessing.tint(value)
    
    def sharpen(self,value=0):
        return self.imageProcessing.sharpen(value)
    
    def histogram(self):
        return self.imageProcessing.histogram()
    
    def equalize(self):
        return self.imageProcessing.equalization()
    
    def stretch(self):
        return self.imageProcessing.stretching()
    
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
    
    def watershed(self):
        return self.imageProcessing.watershed()
    
    def KMeansSegmentation(self):
        return self.imageProcessing.KMeansSegmentation()
    
    def undo(self):
        self.settings.undoLastImageAction()
        return
    
    def reset(self):
        self.settings.resetImage()
        return