import math
from operator import gt, indexOf
from random import randint, random
import cv2
from cv2 import COLOR_RGB2GRAY
from cv2 import threshold
import numpy as np

class ImageProcessing:
    def __init__(self, image): 
        self._image = image
        
    def setImage(self,image):
        self._image = image
    
    def brightness(self,value):
        self._image = self._image + value
        return self._image
    
    def contrast(self,value):
        final_image = np.copy(self._image)
        final_image = final_image * value
        return final_image
    
    def highlight(self):
        return self._image + 255 - self._image * 0.5
    
    def warmth(self,value):
        final_image = np.copy(self._image)
        final_image = final_image + value
        return final_image
    
    def sharpen(self):
        return
    
    def shadows(self):
        return
    
    def tint(self,color):
        final_image = np.copy(self._image)
        final_image[:,:,0] = final_image[:,:,0] + color[0]
        final_image[:,:,1] = final_image[:,:,1] + color[1]
        final_image[:,:,2] = final_image[:,:,2] + color[2]
        return final_image
    
    def saturation(self,value):
        final_image = np.copy(self._image)
        final_image[:,:,0] = final_image[:,:,0] + value
        final_image[:,:,1] = final_image[:,:,1] + value
        final_image[:,:,2] = final_image[:,:,2] + value
        return final_image
    
    def invert(self,value):
        self._image = 255 - self._image
        return self._image
    
    def histogram(self):
        hist = cv2.calcHist([self._image],[0],None,[256],[0,256])
        return hist

    def equalization(self):
        image = self._image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.equalizeHist(image)
        return image
    
    def stretching(self,histogram=None):
        histogram = self.histogram() if histogram is None else histogram
        histogram = np.array(histogram)
        histogram = histogram / np.sum(histogram)
        histogram = histogram * 255
        return histogram
    
    def gaussian_blur(self,kernel_size=3,sigma=0.01):
        final_image = np.copy(self._image)
        return cv2.GaussianBlur(final_image,(kernel_size,kernel_size),0)
    
    def mean_filter(self,kernel_size=3):
        final_image = np.copy(self._image)
        kernel = np.ones((kernel_size,kernel_size),np.uint8)
        return cv2.filter2D(final_image,-1,kernel)
    
    # def mean_filter(self,kernel_size=3):
    #     kernel = np.ones((kernel_size,kernel_size),np.uint8)
        
    #     kernel_width,kernel_height = kernel.shape[0],kernel.shape[1]
    #     x_kernel_center,y_kernel_center = kernel.shape[0]//2,kernel.shape[1]//2
                        
    #     if len(self._image.shape) == 3:
    #         red_channel_pad = np.pad(self._image[:,:,0],((y_kernel_center,y_kernel_center),((x_kernel_center,x_kernel_center))),'symmetric')
    #         green_channel_pad = np.pad(self._image[:,:,1],((y_kernel_center,y_kernel_center),((x_kernel_center,x_kernel_center))),'symmetric')
    #         blue_channel_pad = np.pad(self._image[:,:,2],((y_kernel_center,y_kernel_center),((x_kernel_center,x_kernel_center))),'symmetric')
                        
    #         original_image = np.dstack((red_channel_pad,green_channel_pad,blue_channel_pad))
    #     else:
    #         original_image = np.pad(self._image,((y_kernel_center,y_kernel_center),((x_kernel_center,x_kernel_center))),'symmetric')
        
    #     final_image = np.copy(original_image)
        
    #     for i in  range(x_kernel_center,original_image.shape[0] - x_kernel_center):
    #         for j in  range(y_kernel_center,original_image.shape[1] - y_kernel_center):
    #             final_image[i,j,0] = np.mean(np.multiply(kernel,original_image[i-x_kernel_center:i-x_kernel_center+kernel_width,j-y_kernel_center:j-y_kernel_center+kernel_height,0]))
    #             final_image[i,j,1] = np.mean(np.multiply(kernel,original_image[i-x_kernel_center:i-x_kernel_center+kernel_width,j-y_kernel_center:j-y_kernel_center+kernel_height,1]))
    #             final_image[i,j,2] = np.mean(np.multiply(kernel,original_image[i-x_kernel_center:i-x_kernel_center+kernel_width,j-y_kernel_center:j-y_kernel_center+kernel_height,2]))
        
    #     final_image = final_image[x_kernel_center:original_image.shape[0] - x_kernel_center,y_kernel_center:original_image.shape[1] - y_kernel_center]

    #     return final_image
    
    def median_filter(self,kernel_size=3):
        final_image = np.copy(self._image)
        return cv2.medianBlur(final_image,kernel_size)
    
    def grayscale(self):
        final_image = np.copy(self._image)
        
        # grayscale = 0
        
        # for i in range(0,self._image.shape[0]):
        #     for j in range(0,self._image.shape[1]):
        #         grayscale = final_image[i,j,0]*0.3 + final_image[i,j,1]*0.4 + final_image[i,j,2]*0.3
        #         final_image[i,j,0] = grayscale
        
        # return final_image[:,:,0]
        return cv2.cvtColor(final_image,COLOR_RGB2GRAY)
    
    def threshold(self,threshold):        
        # return cv2.threshold(self._image,threshold,255,cv2.THRESH_BINARY)[1]
        final_image = np.copy(self._image)
        final_image[:,:] = (final_image[:,:] > threshold)*255
                
        return final_image
    
    def otsu(self):
        
        final_image = np.copy(self._image)
        number_of_pixels,bins = np.histogram(final_image,np.arange(0,257))
        
        sumOfPixels = np.sum(number_of_pixels)
        
        threshold = 1
        
        for index in range(1,len(number_of_pixels)):
            
            sb = 0
            sf = 0
            wb = 0
            wf = 0
            vb = 0
            vf = 0
            mb = 0
            mf = 0
                        
            sb = np.sum(number_of_pixels[:index])
            sf = np.sum(number_of_pixels[index:])
            
            wb = sb/sumOfPixels
            wf = sf/sumOfPixels
            
            if sb != 0:
                for i in range(0,index):
                    mb = mb + ((number_of_pixels[i]*i)/sb)
                for k in range(0,index):
                    vb = vb + ((((k - mb)**2)*number_of_pixels[k])/sb)
            
            if sf != 0:
                for j in range(index,len(number_of_pixels)):
                    mf = mf + ((number_of_pixels[j]*j)/sf)
                for l in range(index,len(number_of_pixels)):
                    vf = vf + ((((l - mf)**2)*number_of_pixels[l])/sf)
                
            withinClassVariance = wb*vb + wf*vf
            
            if index == 1:
                minWithinClassVariance = withinClassVariance
            
            if minWithinClassVariance > withinClassVariance:
                minWithinClassVariance = withinClassVariance
                threshold = index
        
        return self.threshold(threshold)
          
    # def erosion(self,kernel,iterations):
    #     kernel = np.ones((3,3),np.uint8)*255 if kernel is None else kernel
    #     kernel_width,kernel_height = kernel.shape[0],kernel.shape[1]
    #     x_kernel_center,y_kernel_center = kernel.shape[0]//2,kernel.shape[1]//2
                        
    #     if len(self._image.shape) == 3:
    #         original_image = np.pad(self.grayscale(),((y_kernel_center,y_kernel_center),((x_kernel_center,x_kernel_center))),'symmetric')
    #     else:
    #         original_image = np.pad(self._image,((y_kernel_center,y_kernel_center),((x_kernel_center,x_kernel_center))),'symmetric')
        
    #     self.setImage(original_image)
    #     original_image = self.otsu()
    #     final_image = np.copy(original_image)
        
    #     for i in range(x_kernel_center,original_image.shape[0] - x_kernel_center):
    #         for j in range(y_kernel_center,original_image.shape[1] - y_kernel_center):
    #             if np.array_equal(kernel,original_image[i-x_kernel_center:i-x_kernel_center+kernel_width,j-y_kernel_center:j-y_kernel_center+kernel_height]):
    #                 final_image[i,j] = 255
    #             else:
    #                 final_image[i,j] = 0
            
    #     final_image = final_image[x_kernel_center:original_image.shape[0] - x_kernel_center,y_kernel_center:original_image.shape[1] - y_kernel_center]
    #     return final_image
    
    def erosion(self,kernel,iterations):
        kernel = np.ones((3,3),np.uint8)*255 if kernel is None else kernel
    
        final_image = np.copy(self._image)
        
        return cv2.erode(final_image,kernel)
    
    def dilation(self,kernel,iterations):                
        kernel = np.ones((3,3),np.uint8)*255 if kernel is None else kernel
    
        final_image = np.copy(self._image)
        
        return cv2.dilate(final_image,kernel)

    def opening(self,kernel,iterations):
        kernel = np.ones((3,3),np.uint8)*255 if kernel is None else kernel
        
        final_image = np.copy(self._image)
        
        return cv2.dilate(cv2.erode(final_image,kernel),kernel)
    
    def closing(self,kernel,iterations):
        return
    
    def gradiant(self):
        gradient_kernel = [-1,1]
        
        if len(self._image.shape) == 3:
            original_image = np.pad(self.grayscale(),((1,1),((1,1))),'symmetric')
        else:
            original_image = np.pad(self._image,((1,1),((1,1))),'symmetric')
            
        final_image = np.copy(original_image)
        final_image_x = np.copy(original_image)
        final_image_y = np.copy(original_image)
        
        for i in range(1,original_image.shape[0] - 1):
            for j in range(1,2,original_image.shape[1] - 1):
                final_image_x[i,j] = np.sum(gradient_kernel[0]*original_image[i,j] + gradient_kernel[1]*original_image[i,j+1])
            
        for i in range(1,2,original_image.shape[0] - 1):
            for j in range(1,original_image.shape[1] - 1):
                final_image_y[i,j] = np.sum(gradient_kernel[0]*original_image[i,j] + gradient_kernel[1]*original_image[i,j+1])
        
        # for i in range(1,original_image.shape[0] - 1):
        #     for j in range(1,original_image.shape[1] - 1):
        #         final_image[i,j] = math.atan(final_image_y[i,j]/(final_image_x[i,j]+1))
                
        for i in range(1,original_image.shape[0] - 1):
            for j in range(1,original_image.shape[1] - 1):
                final_image[i,j] = math.floor(math.sqrt(final_image_y[i,j]**2 + final_image_x[i,j]**2))
                
        final_image = abs(final_image[1:original_image.shape[0] - 1,1:original_image.shape[1] - 1])
        
        self._image = np.copy(final_image)
        final_image = self.otsu()
                        
        return final_image
    
    # def sobel(self):
        
    #     sobel_kernel_x = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
        
    #     sobel_kernel_y = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
        
    #     if len(self._image.shape) == 3:
    #         original_image = np.pad(self.grayscale(),((1,1),((1,1))),'symmetric')
    #     else:
    #         original_image = np.pad(self._image,((1,1),((1,1))),'symmetric')
        
    #     final_image_x = np.copy(original_image)
        
    #     final_image_y = np.copy(original_image)
        
    #     for i in range(1,original_image.shape[0] - 1):
    #         for j in range(1,original_image.shape[1] - 1):
    #             final_image_x[i,j] = np.sum(sobel_kernel_x*original_image[i,j] + sobel_kernel_x*original_image[i,j+1])
    
    #     for i in range(1,original_image.shape[0] - 1):
    #         for j in range(1,original_image.shape[1] - 1):
    #             final_image_y[i,j] = np.sum(sobel_kernel_y*original_image[i,j] + sobel_kernel_y*original_image[i,j+1])
                
    #     final_image = np.copy(original_image)
        
    #     for i in range(1,original_image.shape[0] - 1):
    #         for j in range(1,original_image.shape[1] - 1):
    #             final_image[i,j] = math.floor(math.sqrt(final_image_y[i,j]**2 + final_image_x[i,j]**2))
    
    #     final_image = abs(final_image[1:original_image.shape[0] - 1,1:original_image.shape[1] - 1])
        
    #     self._image = np.copy(final_image)
        
    #     final_image = self.otsu()
        
    #     return final_image
    
    def sobel(self):
        
        if len(self._image.shape) == 3:
            original_image = self.grayscale()
        else:
            original_image = self._image
            
        final_image = np.copy(original_image)    
        sobel_x = cv2.Sobel(final_image,cv2.CV_8U,1,0,ksize=3)
        sobel_y = cv2.Sobel(final_image,cv2.CV_8U,0,1,ksize=3)

        return sobel_x + sobel_y
    
    def laplacian(self):            
        final_image = np.copy(self._image)

        return cv2.Laplacian(final_image,cv2.CV_8U,ksize=3)
    
    def canny(self):
        if len(self._image.shape) == 3:
            original_image = self.grayscale()
        else:
            original_image = self._image
            
        final_image = np.copy(original_image)

        return cv2.Canny(final_image,100,200)
    
    def hough(self):
        if len(self._image.shape) == 3:
            original_image = self.grayscale()
        else:
            original_image = self._image
            
        final_image = np.copy(original_image)

        return cv2.Canny(final_image,100,200)
    
    def sift(self):
        final_image = np.copy(self._image)

        return cv2.sift
    
    def harris(self):
        return
    
    def roberts(self):
        
        gradient_kernel = [[0,1],[-1,0]]
        
        if len(self._image.shape) == 3:
            original_image = np.pad(self.grayscale(),((1,1),((1,1))),'symmetric')
        else:
            original_image = np.pad(self._image,((1,1),((1,1))),'symmetric')
            
        final_image = np.copy(original_image)
        final_image_x = np.copy(original_image)
        final_image_y = np.copy(original_image)
        
        for i in range(1,original_image.shape[0] - 1):
            for j in range(1,2,original_image.shape[1] - 1):
                final_image_x[i,j] = np.sum(gradient_kernel[0][1]*original_image[i,j] 
                                            + gradient_kernel[0][0]*original_image[i,j-1]
                                            + gradient_kernel[1][0]*original_image[i+1,j-1]
                                            + gradient_kernel[1][1]*original_image[i+1,j+1])
            
        for i in range(1,2,original_image.shape[0] - 1):
            for j in range(1,original_image.shape[1] - 1):
                final_image_y[i,j] = np.sum(gradient_kernel[0][0]*original_image[i,j] 
                                            + gradient_kernel[0][1]*original_image[i,j-1]
                                            + gradient_kernel[1][1]*original_image[i+1,j-1]
                                            + gradient_kernel[1][0]*original_image[i+1,j+1])
        
        for i in range(1,original_image.shape[0] - 1):
            for j in range(1,original_image.shape[1] - 1):
                final_image[i,j] = math.floor(math.sqrt(final_image_y[i,j]**2 + final_image_x[i,j]**2))
                
        final_image = abs(final_image[1:original_image.shape[0] - 1,1:original_image.shape[1] - 1])
        
        self._image = np.copy(final_image)
        final_image = self.otsu()
                    
        return final_image
    
    def prewitt(self):
        
        if len(self._image.shape) == 3:
            original_image = self.grayscale()
        else:
            original_image = self._image
            
        final_image = np.copy(original_image)

        return cv2.Prewitt(final_image,cv2.CV_8U,1,0,ksize=3)
        
    def kirsch(self):
        return 
    
    def regionGrowing(self):
        final_image = np.copy(self._image)
        
        return cv2.region
    
    def regionSpliting(self):
        return
    
    def splitingAndMerging(self):
        return 
    
    def KMeansSegmentation(self):
        return