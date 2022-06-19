import math
from operator import gt, indexOf
from random import randint, random
import cv2
from cv2 import COLOR_RGB2GRAY
from cv2 import threshold
from matplotlib import markers
import numpy as np

class ImageProcessing:
    def __init__(self, image): 
        self._image = image
        
    def setImage(self,image):
        self._image = image
    
    def rotate(self,angle):
        return cv2.rotate(self._image,cv2.ROTATE_90_CLOCKWISE)
    
    def flip(self):
        final_image = np.copy(self._image)
        final_image = cv2.flip(final_image,1)
        return final_image
    
    def zoomIn(self,factor=0.5):
        final_image = np.copy(self._image)
        final_image = cv2.resize(final_image,(0,0),fx=factor,fy=factor)
        return final_image
    
    def zoomOut(self,factor=0.5):
        final_image = np.copy(self._image)
        final_image = cv2.resize(final_image,(0,0),fx=1/factor,fy=1/factor)
        return final_image
    
    def brightness(self,value):
        self._image = self._image + value
        return self._image
    
    def contrast(self,value):
        final_image = np.copy(self._image)
        final_image = final_image * value
        return final_image
    
    def highlights(self,value):
        final_image = np.copy(self._image)
        final_image[:,:,1] = final_image[:,:,1] + value
        final_image[:,:,2] = final_image[:,:,2] + value
        return final_image
    
    def warmth(self,value):
        final_image = np.copy(self._image)
        final_image[:,:,0] = final_image[:,:,0] + value/2
        final_image[:,:,1] = final_image[:,:,1] - value/6
        final_image[:,:,2] = final_image[:,:,2] - value/2
        
        return final_image
    
    def sharpen(self,value):
        final_image = np.copy(self._image)
        final_image = cv2.GaussianBlur(final_image,(3,3),0)
        final_image = final_image + value
        return final_image
    
    def shadows(self,value):
        final_image = np.copy(self._image)
        final_image[:,:,0] = final_image[:,:,0] + value
        final_image[:,:,1] = final_image[:,:,1] + value
        final_image[:,:,2] = final_image[:,:,2] + value
        return final_image
    
    def tint(self,value):
        final_image = np.copy(self._image)
        final_image[:,:,0] = final_image[:,:,0] + value
        final_image[:,:,1] = final_image[:,:,1] + value
        final_image[:,:,2] = final_image[:,:,2] + value
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
        hist = cv2.calcHist([self._image],[2],None,[256],[0,256])
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
        scale = 1
        delta = 0
        ddepth = cv2.CV_16S
        
        if len(self._image.shape) == 3:
            original_image = self.grayscale()
        else:
            original_image = self._image
            
        final_image = np.copy(original_image)    

        grad_x = cv2.Sobel(final_image, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
        grad_y = cv2.Sobel(final_image, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
        
        abs_grad_x = cv2.convertScaleAbs(grad_x)
        abs_grad_y = cv2.convertScaleAbs(grad_y)
        
        grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
        
        return grad
    
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
        
        scale = 1
        delta = 0
        ddepth = cv2.CV_16S
        
        if len(self._image.shape) == 3:
            original_image = self.grayscale()
        else:
            original_image = self._image
            
        final_image = np.copy(original_image)    

        grad_x = cv2.Sobel(final_image, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
        grad_y = cv2.Sobel(final_image, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
        
        abs_grad_x = cv2.convertScaleAbs(grad_x)
        abs_grad_y = cv2.convertScaleAbs(grad_y)
        
        grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
        
        return grad
        
    def kirsch(self):
        return 
    
    def regionGrowing(self):
        final_image = np.copy(self._image)
        
        return cv2.region
    
    def regionSpliting(self):
        return
    
    def splitingAndMerging(self):
        return 
    
    def watershed(self):
        final_image = np.copy(self._image)
         
        markers = np.zeros(final_image.shape, dtype=np.int32)
         
        return cv2.watershed(final_image, markers)
    
    def KMeansSegmentation(self):
    
        final_image = np.copy(self._image)
        
        Z = final_image.reshape((-1,3))

        Z = np.float32(Z)

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        K = 8
        ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
        # Now convert back into uint8, and make original image
        center = np.uint8(center)
        res = center[label.flatten()]
        res2 = res.reshape((final_image.shape))
        
        return res2