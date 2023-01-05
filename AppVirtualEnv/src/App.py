import math
import sys
import random
import cv2
from cv2 import threshold
from cv2 import COLOR_RGB2GRAY
from cv2 import sqrt
import numpy as np
import matplotlib.pyplot as plt

from src.modules.PicProcessingApp import PicProcessingApp
from PySide6.QtCore import (Qt, QRect)
from PySide6.QtGui import (QImage, QPixmap)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel,
                               QMainWindow, QVBoxLayout, QFileDialog, 
                               QSlider, QHBoxLayout)

from src.ui.DEV_UI_MainWindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.filename = None
        self.tmp = None
        self.pixmap = None
        
        self._isFiltersMenuOpen = False
        self._isLightAndColorsMenuOpen = False
        
        self._isImageFiltredHidden = False
        self._isImageEditMenuHidden = True
        self._isImageAdjustMenuHidden = True
        
        self.initApp()
        self.connectingListeners()
        
    def initApp(self):
        
        self.pixmap = self.ui.Image.pixmap()
        self.pixmapcopy = self.ui.Image_copy.pixmap()
        
        self.image = cv2.imread("C:\\Users\\amine\\OneDrive\\Desktop\\Programming\\Python\\workspace\\computer vision\\ComputerVisionApp\\AppVirtualEnv\\src\\assets\\as11.png")
        self.persistingImage = cv2.imread("C:\\Users\\amine\\OneDrive\\Desktop\\Programming\\Python\\workspace\\computer vision\\ComputerVisionApp\\AppVirtualEnv\\src\\assets\\as11.png")
        self.setPicture(self.image,pixmap=self.pixmapcopy)
        
        if self._isFiltersMenuOpen == False:
            self.ui.FiltersScrollArea.hide()
            
        if self._isLightAndColorsMenuOpen == False:
            self.ui.LightAndColorsScrollArea.hide()
        
        if self._isImageAdjustMenuHidden == True:
            self.ui.AdjustTopMenu.hide()
            
        if self._isImageEditMenuHidden == True:
            self.ui.AdjustMenu.hide()
        
        self.picProcessingApp = PicProcessingApp(self.image)
    
    def connectingListeners(self):
        self.ui.AdjustImageBtn.clicked.connect(self.setupAdjustImageMenuToggleTool)
        self.ui.EditImageBtn.clicked.connect(self.setupEditImageMenuToggleTool)
        self.ui.AdjustementBtn.clicked.connect(self.setupAdjustementMenuToggleTool)
        self.ui.ApplyFiltersBtn.clicked.connect(self.setupApplyFiltersMenuToggleTool)
        self.ui.ResetChangesBtn.clicked.connect(self.resetChanges)
        
        self.ui.RotateBtn.clicked.connect(self.setupRotateTool)
        self.ui.ZoomInBtn.clicked.connect(self.setupZoomInTool)
        self.ui.ZoomOutBtn.clicked.connect(self.setupZoomOutTool)
        self.ui.FlipBtn.clicked.connect(self.setupFlipTool)
        self.ui.CropBtn.clicked.connect(self.setupCropTool)
        self.ui.ViewSwitchedBtn.clicked.connect(self.setupSwitchViewTool)
        
        self.ui.FiltersBtn.clicked.connect(self.setupFiltersToggleTool)
        self.ui.SwitchViewBtn.clicked.connect(self.setupSwitchViewTool)
        
        self.ui.OpenImageBtn.clicked.connect(self.loadImageFile)
        self.ui.SaveImageBtn.clicked.connect(self.saveImageFile)
        self.ui.ResetBtn.clicked.connect(self.resetChanges)
        self.ui.NoEffectsBtn.clicked.connect(self.noEffects)
        
        self.ui.BrightnessBtn.clicked.connect(self.setupBrightnessTool)
        self.ui.InvertBtn.clicked.connect(self.setupInvertTool)
        self.ui.GrayScaleBtn.clicked.connect(self.setupGrayScaleTool)
        self.ui.ContrastBtn.clicked.connect(self.setupContrastTool)
        self.ui.HighlightsBtn.clicked.connect(self.setupHighlightsTool)
        self.ui.ShadowsBtn.clicked.connect(self.setupShadowsTool)
        self.ui.WarmthBtn.clicked.connect(self.setupWarmthTool)
        self.ui.SaturationBtn.clicked.connect(self.setupSaturationTool)
        self.ui.TintBtn.clicked.connect(self.setupTintTool)
        
        self.ui.HistBtn.clicked.connect(self.setupHistogramTool)
        self.ui.HistEqualizerBtn.clicked.connect(self.setupHistogramEqualizerTool)
        self.ui.HistStretchBtn.clicked.connect(self.setupHistogramStretchTool)
        
        self.ui.ManualTresholdingBtn.clicked.connect(self.setupThresholdTool)
        self.ui.OtsuTresholdingBtn.clicked.connect(self.setupOtsuTool)
        
        self.ui.MeanBlurBtn.clicked.connect(self.setupMeanBlurTool)
        self.ui.MedianBlurBtn.clicked.connect(self.setupMedianBlurTool)
        self.ui.GaussienBlurBtn.clicked.connect(self.setupGaussianBlurTool)
        
        self.ui.ErosionBtn.clicked.connect(self.setupErosionTool)
        self.ui.DilationBtn.clicked.connect(self.setupDilationTool)
        self.ui.OpeningBtn.clicked.connect(self.setupOpeningTool)
        self.ui.ClosingBtn.clicked.connect(self.setupClosingTool)
        
        self.ui.GradiantBtn.clicked.connect(self.setupGradiantEdgeDetectionTool)
        self.ui.LaplacianBtn.clicked.connect(self.setupLaplacianEdgeDetectionTool)
        self.ui.RobertsBtn.clicked.connect(self.setupRobertsEdgeDetectionTool)
        self.ui.SobelBtn.clicked.connect(self.setupSobelEdgeDetectionTool)
        self.ui.PrewittBtn.clicked.connect(self.setupPrewittEdgeDetectionTool)
        self.ui.CannyBtn.clicked.connect(self.setupCannyEdgeDetectionTool)
        self.ui.KirschBtn.clicked.connect(self.setupKirschEdgeDetectionTool)
        self.ui.RegionGrowingBtn.clicked.connect(self.setupRegionGrowingSegmentationTool)
        self.ui.RegionPartitionBtn.clicked.connect(self.setupRegionPartitioningSegmentationTool)
        self.ui.KMeansBtn.clicked.connect(self.setupKMeansSegmentationTool)
    
    def constructFrameToolWidget(self,objectname):
        frame = QFrame()
        frame.setObjectName(u""+objectname)
        frameLayout = QHBoxLayout()
        frame.setLayout(frameLayout)
        return frame,frameLayout
    
    def constructSliderToolWidget(self,objectname,label):
        
        frame,frameLayout = self.constructFrameToolWidget(u""+objectname+"Frame")
        
        toolLabel = QLabel()
        toolLabel.setText(label)
        toolLabel.setStyleSheet("color:white;font-size:16px;width:80px;margin-right:20px;")
        
        toolSlider = QSlider(Qt.Horizontal)
        toolSlider.setObjectName("ThresholdSlider")
        toolSlider.setEnabled(True)
        
        frameLayout.addWidget(toolLabel)
        frameLayout.addWidget(toolSlider)
        
        self.ui.AdjustToolFrameLayout.addWidget(frame)
                
        return toolSlider
        
    def clearAdjustToolFrame(self):
        for i in reversed(range(self.ui.AdjustToolFrameLayout.count())): 
            self.ui.AdjustToolFrameLayout.itemAt(i).widget().setParent(None)
    
    def setPicture(self,image,pixmap=None):
        self.tmp = image
        frame = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        image = QImage(frame,frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.pixmap = QPixmap.fromImage(image)
        ## under dev
        sclaedPixMap = self.pixmap.scaled(991, 631, Qt.KeepAspectRatio)
        # sclaedPixMap = self.pixmap.scaled(801, 481, Qt.KeepAspectRatio)
        self.ui.Image.setPixmap(QPixmap(sclaedPixMap))
        
        if pixmap != None:
            self.ui.Image_copy.setPixmap(QPixmap(sclaedPixMap))
            
    def loadImageFile(self):
        self.filename = QFileDialog.getOpenFileName(self,"Open File","C:\\Users\\amine\\OneDrive\\Desktop\\Programming\\Python\\workspace\\computer vision\\ComputerVisionApp\\AppVirtualEnv\\src\\assets","All Files (*)")
        
        if(self.filename[0]):
            self.image = cv2.imread(self.filename[0])
            self.imageCopy = np.copy(self.image)
            self.persistingImage = cv2.imread(self.filename[0])
            # self.pixmap = QPixmap(self.filename[0])
            # self.image = self.pixmap.toImage()
            # sclaedPixMap = self.pixmap.scaled(801, 481, Qt.KeepAspectRatio)
            # self.ui.Image.setPixmap(sclaedPixMap)
            # self.image = self.pixmap.toImage()
            self.picProcessingApp.setImage(self.image)
            self.noEffects()
            self.setPicture(self.image,pixmap=self.pixmapcopy)
        
    def saveImageFile(self):
        fileName = QFileDialog.getSaveFileName(self,"Save File","C:\\Users\\amine\\OneDrive\\Desktop\\Programming\\Python\\workspace\\computer vision\\ComputerVisionApp\\AppVirtualEnv\\src\\assets","All Files (*)")
        
        image = self.ui.Image_copy.pixmap().toImage()
        image = image.convertToFormat(QImage.Format_RGB888)
        image = np.array(image.bits()).reshape(image.height(),image.width(),3)
        
        cv2.imwrite(fileName[0], image)

    def resetChanges(self):
        self.image = np.copy(self.persistingImage)
        self.picProcessingApp.setImage(self.image)
        self.noEffects()
        self.setPicture(self.image)
    
    def noEffects(self):
        self.clearAdjustToolFrame()
        self.upadetCurrentFilterName("No Filters")
        
    def upadetCurrentFilterName(self,text):
        self.ui.FiltersBtn.setText(text)
        return
    
    ## processing callers
    
    def rotateHandler(self):
                
        self.image = self.picProcessingApp.rotate()
        self.setPicture(self.image)
    
    def flipHandler(self):
        self.image = self.picProcessingApp.flip()
        self.setPicture(self.image)
    
    def zoomInHandler(self):
        self.image = self.picProcessingApp.zoomIn()
        self.setPicture(self.image)
    
    def zoomOutHandler(self):
        self.image = self.picProcessingApp.zoomOut()
        self.setPicture(self.image)
       
    def histogramHandler(self):
                
        # histogram = self.picProcessingApp.histogram()
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

        colors = ("red", "green", "blue")
        channel_ids = (0, 1, 2)
        plt.figure()
        plt.xlim([0, 256])
        for (channel_id, c) in zip(channel_ids, colors):
            histogram  = [(image[:,:,channel_id]==v).sum() for v in range(256)]
            plt.plot(histogram, color=c)

        plt.xlabel("color value")
        plt.ylabel("pixel count")

        plt.show()
        
        return
            
    def histogramEqualizerHandler(self):
        
        self.imageCopy = np.copy(self.image)

        self.imageCopy = self.picProcessingApp.equalize()
        self.setPicture(self.imageCopy)
        
        return
    
    def histogramStretchHandler(self):
        self.imageCopy = np.copy(self.image)

        self.imageCopy = self.picProcessingApp.stretch()
        self.setPicture(self.imageCopy)
        
        return
        
    def brightnessHandler(self,value):
        self.imageCopy = np.copy(self.image)
        
        value = (value/20) + 1
                
        self.imageCopy[:,:,0] = self.imageCopy[:,:,0]/(value)
        self.imageCopy[:,:,1] = self.imageCopy[:,:,1]/(value)
        self.imageCopy[:,:,2] = self.imageCopy[:,:,2]/(value)
                                        
        self.setPicture(self.imageCopy)
   
    def contrastHandler(self,value):
        self.imageCopy = np.copy(self.image)
        self.imageCopy = self.picProcessingApp.contrast(value)                            
        self.setPicture(self.imageCopy)
    
    def warmthHandler(self,value):
        self.imageCopy = np.copy(self.image)
        self.imageCopy = self.picProcessingApp.warmth(value)                         
        self.setPicture(self.imageCopy)
    
    def saturationHandler(self,value):
        self.imageCopy = np.copy(self.image)
        self.imageCopy = self.picProcessingApp.saturation(value)                         
        self.setPicture(self.imageCopy)
    
    def highlightsHandler(self,value):
        self.imageCopy = np.copy(self.image)
        self.imageCopy = self.picProcessingApp.hightlights(value)                         
        self.setPicture(self.imageCopy) 
    
    def tintHandler(self,value):
        self.imageCopy = np.copy(self.image)
        self.imageCopy = self.picProcessingApp.tint(value)                         
        self.setPicture(self.imageCopy)
    
    def shadowsHandler(self,value):
        self.imageCopy = np.copy(self.image)
        self.imageCopy = self.picProcessingApp.shadows(value)                         
        self.setPicture(self.imageCopy)
    
    def sharpenHandler(self,value):
        self.imageCopy = np.copy(self.image)
        self.imageCopy = self.picProcessingApp.sharpen(value)                         
        self.setPicture(self.imageCopy)
    
    def invertHandler(self,value=0):
        self.imageCopy = np.copy(self.image)
        if self.imageCopy.ndim == 2:
            self.picProcessingApp.setImage(self.imageCopy)
        self.imageCopy = self.picProcessingApp.invert(value)
        self.setPicture(self.imageCopy)
    
    def grayScaleHandler(self):
        self.imageCopy = np.copy(self.image)
        self.imageCopy = self.picProcessingApp.grayscale()
        self.setPicture(self.imageCopy)
    
    def manualTreshlodHandler(self,value):
        self.imageCopy = np.copy(self.image)
        if self.imageCopy.ndim == 3:
            self.imageCopy = cv2.cvtColor(self.imageCopy,COLOR_RGB2GRAY)
            self.picProcessingApp.setImage(self.imageCopy)
            
        self.imageCopy = self.picProcessingApp.manualThresholding(threshold=value)
        self.setPicture(self.imageCopy)
    
    def otsuHandler(self):
        self.imageCopy = np.copy(self.image)
        if self.imageCopy.ndim == 3:
            self.imageCopy = cv2.cvtColor(self.imageCopy,COLOR_RGB2GRAY)
            
        self.picProcessingApp.setImage(self.imageCopy)
        self.imageCopy = self.picProcessingApp.otsu()
        self.setPicture(self.imageCopy)
        return
    
    def erosionHandler(self,kernel_size):
        kernel = np.ones((kernel_size,kernel_size),np.uint8)*255
        self.imageCopy = np.copy(self.image)
        self.picProcessingApp.setImage(self.imageCopy)
        self.imageCopy = self.picProcessingApp.erosion(kernel=kernel)
        self.setPicture(self.imageCopy)
        return

    def dilationHandler(self,kernel_size):
        kernel = np.ones((kernel_size,kernel_size),np.uint8)*255
        self.imageCopy = np.copy(self.image)
        self.picProcessingApp.setImage(self.imageCopy)
        self.imageCopy = self.picProcessingApp.dilation(kernel=kernel)
        self.setPicture(self.imageCopy)
        return

    def openingHandler(self,kernel_size):
        kernel = np.ones((kernel_size,kernel_size),np.uint8)*255
        
        self.imageCopy = np.copy(self.image)
        self.picProcessingApp.setImage(self.imageCopy)
        self.imageCopy = self.picProcessingApp.opening(kernel=kernel)
        self.setPicture(self.imageCopy)
        return
    
    def closingHandler(self,kernel_size):
        return
    
    def meanBlurHandler(self,kernel_size):
        self.imageCopy = np.copy(self.image)
        
        if kernel_size%2 == 0:
            kernel_size = kernel_size+1
        
        self.imageCopy = self.picProcessingApp.meanBlur(kernel_size=kernel_size)
        self.setPicture(self.imageCopy)
        return
    
    def medianBlurHandler(self,kernel_size):
        self.imageCopy = np.copy(self.image)
        
        if kernel_size%2 == 0:
            kernel_size = kernel_size+1
        
        self.imageCopy = self.picProcessingApp.medianBlur(kernel_size=kernel_size)
        self.setPicture(self.imageCopy)
        return
    
    def gaussianBlurHandler(self,kernel_size=3,sigma=0.01):      
        self.imageCopy = np.copy(self.image)
        
        if kernel_size%2 == 0:
            kernel_size = kernel_size+1
        
        self.imageCopy = self.picProcessingApp.gaussianBlur(kernel_size=kernel_size,sigma=sigma)
        self.setPicture(self.imageCopy)
        return
    
    def gradiantHandler(self):
        self.imageCopy = np.copy(self.image)
        
        self.imageCopy = self.picProcessingApp.gradiant()
        self.setPicture(self.imageCopy)
        return
    
    def sobelHandler(self):
        self.imageCopy = np.copy(self.image)
        
        self.imageCopy = self.picProcessingApp.sobel()
        self.setPicture(self.imageCopy)
        return
    
    def cannyHandler(self):
        self.imageCopy = np.copy(self.image)
        
        self.imageCopy = self.picProcessingApp.canny()
        self.setPicture(self.imageCopy)
        return
    
    def laplacianHandler(self):
        self.imageCopy = np.copy(self.image)
        
        self.imageCopy = self.picProcessingApp.laplacian()
        self.setPicture(self.imageCopy)
        return
    
    def kirschHandler(self):
        return
    
    def robertsHandler(self):
        self.imageCopy = np.copy(self.image)
        
        self.imageCopy = self.picProcessingApp.roberts()
        self.setPicture(self.imageCopy)
        return
    
    def prewittHandler(self):
        self.imageCopy = np.copy(self.image)
        
        self.imageCopy = self.picProcessingApp.prewitt()
        self.setPicture(self.imageCopy)
        return
    
    def siftHandler(self):
        return 
    
    def houghHandler(self):
        return 
    
    def harrisHandler(self):
        return 
    
    def snakesHandler(self):
        return 
    
    def watershedHandler(self):
        self.imageCopy = np.copy(self.image)
        
        self.imageCopy = self.picProcessingApp.watershed()
        self.setPicture(self.imageCopy)
        return
    
    def regionGrowingHandler(self):
        self.imageCopy = np.copy(self.image)
        
        self.imageCopy = self.picProcessingApp.regionGrowing()
        self.setPicture(self.imageCopy)
        return
    
    def regionSplittingHandler(self):
        self.imageCopy = np.copy(self.image)
        
        self.imageCopy = self.picProcessingApp.regionSplitting()
        self.setPicture(self.imageCopy)
        return
    
    def kmeansHandler(self):
        self.imageCopy = np.copy(self.image)
        
        self.imageCopy = self.picProcessingApp.KMeansSegmentation()
        self.setPicture(self.imageCopy)
        return
    
    ## setup tools
    
    def setupAdjustImageMenuToggleTool(self):
        
        if self._isImageAdjustMenuHidden == True:
            self.ui.AdjustMenu.show()
            self._isImageAdjustMenuHidden = False
        else:
            self.ui.AdjustMenu.hide()
            self._isImageAdjustMenuHidden = True
        
        return
    
    def setupEditImageMenuToggleTool(self):
        
        if self._isImageEditMenuHidden == True:
            self.ui.AdjustTopMenu.show()
            self._isImageEditMenuHidden = False
        else:
            self.ui.AdjustTopMenu.hide()
            self._isImageEditMenuHidden = True
        
        return

    def setupAdjustementMenuToggleTool(self):
        
        if self._isLightAndColorsMenuOpen == False:
            self.ui.FiltersScrollArea.hide()
            self._isFiltersMenuOpen = False
            self.ui.LightAndColorsScrollArea.show()
            self._isLightAndColorsMenuOpen = True
        else:
            self.ui.LightAndColorsScrollArea.hide()
            self._isLightAndColorsMenuOpen = False
            self.noEffects()
        
        return

    def setupApplyFiltersMenuToggleTool(self):
        
        if self._isFiltersMenuOpen == False:
            self.ui.LightAndColorsScrollArea.hide()
            self._isLightAndColorsMenuOpen = False
            self.ui.FiltersScrollArea.show()
            self._isFiltersMenuOpen = True
        else:
            self.ui.FiltersScrollArea.hide()
            self._isFiltersMenuOpen = False
            self.noEffects()
        
        return
    
    def setupSwitchViewTool(self):
        
        if self._isImageFiltredHidden == False:
            self.ui.Image.hide()
            self._isImageFiltredHidden = True
        else:
            self.ui.Image.show()
            self._isImageFiltredHidden = False
        
        # self.ui.Image.setGeometry(QRect(408, 0, 495, 631))
         
        return
    
    def setupFiltersToggleTool(self):
        
        if self._isFiltersMenuOpen == False:
            self.ui.FiltersScrollArea.show()
            self._isFiltersMenuOpen = True
        else:
            self.ui.FiltersScrollArea.hide()
            self._isFiltersMenuOpen = False
            self.noEffects()
        
        return
    
    def setupRotateTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
            
        self.rotateHandler()
        
        return
    
    def setupZoomInTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
            
        self.zoomInHandler()
        
        return
    
    def setupZoomOutTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
            
        self.zoomOutHandler()
        
        return
    
    def setupFlipTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
            
        self.flipHandler()
        
        return
    
    def setupCropTool(self):
        return
    
    def setupBrightnessTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        self.brightnessSlider = self.constructSliderToolWidget("BrightnessTool","Brightness")
        self.brightnessSlider.setMinimum(0)
        self.brightnessSlider.setMaximum(255)
        self.brightnessSlider.setValue(0)
        self.brightnessSlider.valueChanged['int'].connect(self.brightnessHandler)
        
        self.upadetCurrentFilterName(self.ui.BrightnessBtn.text())
        return
    
    def setupContrastTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        self.ContrastSlider = self.constructSliderToolWidget("ContrastTool","Contrast")
        self.ContrastSlider.setMinimum(0)
        self.ContrastSlider.setMaximum(255)
        self.ContrastSlider.setValue(0)
        self.ContrastSlider.valueChanged['int'].connect(self.contrastHandler)
        
        self.upadetCurrentFilterName(self.ui.ContrastBtn.text())
        return
            
    def setupHighlightsTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        self.HighlightsSlider = self.constructSliderToolWidget("HighlightsTool","Highlights")
        self.HighlightsSlider.setMinimum(0)
        self.HighlightsSlider.setMaximum(255)
        self.HighlightsSlider.setValue(0)
        self.HighlightsSlider.valueChanged['int'].connect(self.highlightsHandler)
        
        self.upadetCurrentFilterName(self.ui.HighlightsBtn.text())
        return
    
    def setupShadowsTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        self.ShadowsSlider = self.constructSliderToolWidget("ShadowsTool","Shadows")
        self.ShadowsSlider.setMinimum(0)
        self.ShadowsSlider.setMaximum(255)
        self.ShadowsSlider.setValue(0)
        self.ShadowsSlider.valueChanged['int'].connect(self.shadowsHandler)
        
        self.upadetCurrentFilterName(self.ui.ShadowsBtn.text())
        return  
        
    def setupWarmthTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        self.WarmthSlider = self.constructSliderToolWidget("WarmthTool","Warmth")
        self.WarmthSlider.setMinimum(0)
        self.WarmthSlider.setMaximum(255)
        self.WarmthSlider.setValue(0)
        self.WarmthSlider.valueChanged['int'].connect(self.warmthHandler)
        
        self.upadetCurrentFilterName(self.ui.WarmthBtn.text())
        return
    
    def setupSaturationTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        self.SaturationSlider = self.constructSliderToolWidget("SaturationTool","Saturation")
        self.SaturationSlider.setMinimum(0)
        self.SaturationSlider.setMaximum(255)
        self.SaturationSlider.setValue(0)
        self.SaturationSlider.valueChanged['int'].connect(self.saturationHandler)
        
        self.upadetCurrentFilterName(self.ui.HighlightsBtn.text())
        return
    
    def setupTintTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        self.TintSlider = self.constructSliderToolWidget("TintTool","Tint")
        self.TintSlider.setMinimum(0)
        self.TintSlider.setMaximum(255)
        self.TintSlider.setValue(0)
        self.TintSlider.valueChanged['int'].connect(self.tintHandler)
        
        self.upadetCurrentFilterName(self.ui.TintBtn.text())
        return
    
    def setupSharpenTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        self.SharpenSlider = self.constructSliderToolWidget("SharpenTool","Sharpen")
        self.SharpenSlider.setMinimum(0)
        self.SharpenSlider.setMaximum(255)
        self.SharpenSlider.setValue(0)
        self.SharpenSlider.valueChanged['int'].connect(self.sharpenHandler)
        
        self.upadetCurrentFilterName(self.ui.SharpenBtn.text())
        return
    
    def setupThresholdTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        self.thresholdSlider = self.constructSliderToolWidget("ThresholdTool","Threshold")
        self.thresholdSlider.setMinimum(0)
        self.thresholdSlider.setMaximum(255)
        self.thresholdSlider.setValue(0)
        self.thresholdSlider.valueChanged['int'].connect(self.manualTreshlodHandler)
        
        self.upadetCurrentFilterName(self.ui.ManualTresholdingBtn.text())
        return

    def setupOtsuTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        self.otsuHandler()
        
        self.upadetCurrentFilterName(self.ui.OtsuTresholdingBtn.text())
        return
    
    def setupInvertTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        self.invertHandler()
        
        self.upadetCurrentFilterName(self.ui.InvertBtn.text())
        return
        
    def setupHistogramTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        self.histogramHandler()
        
        self.upadetCurrentFilterName(self.ui.HistBtn.text())
        return
    
    def setupHistogramEqualizerTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        self.histogramEqualizerHandler()
        
        self.upadetCurrentFilterName(self.ui.HistEqualizerBtn.text())
        return
    
    def setupHistogramStretchTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        self.histogramStretchHandler()
        
        self.upadetCurrentFilterName(self.ui.HistStretchBtn.text())
        return
    
    def setupGrayScaleTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        self.grayScaleHandler()
        
        self.upadetCurrentFilterName(self.ui.GrayScaleBtn.text())
        return
    
    def setupErosionTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        self.erosionKernelSizeSlider = self.constructSliderToolWidget("ErosionTool","Kernel Size")
        self.erosionKernelSizeSlider.setMinimum(1)
        self.erosionKernelSizeSlider.setSingleStep(1)
        self.erosionKernelSizeSlider.setMaximum(33)
        self.erosionKernelSizeSlider.setValue(1)
        self.erosionKernelSizeSlider.valueChanged['int'].connect(self.erosionHandler)
        
        self.upadetCurrentFilterName(self.ui.ErosionBtn.text())
        return
    
    def setupDilationTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        self.dilationKernelSizeSlider = self.constructSliderToolWidget("DilationTool","Kernel Size")
        self.dilationKernelSizeSlider.setMinimum(1)
        self.dilationKernelSizeSlider.setSingleStep(1)
        self.dilationKernelSizeSlider.setMaximum(33)
        self.dilationKernelSizeSlider.setValue(1)
        self.dilationKernelSizeSlider.valueChanged['int'].connect(self.dilationHandler)
        
        self.upadetCurrentFilterName(self.ui.DilationBtn.text())
        return
    
    def setupOpeningTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        self.openingKernelSizeSlider = self.constructSliderToolWidget("OpeningTool","Kernel Size")
        self.openingKernelSizeSlider.setMinimum(1)
        self.openingKernelSizeSlider.setSingleStep(1)
        self.openingKernelSizeSlider.setMaximum(33)
        self.openingKernelSizeSlider.setValue(1)
        self.openingKernelSizeSlider.valueChanged['int'].connect(self.openingHandler)
        
        self.upadetCurrentFilterName(self.ui.OpeningBtn.text())
        return
    
    def setupClosingTool(self):
        
        self.upadetCurrentFilterName(self.ui.ClosingBtn.text())
        return

    def setupMeanBlurTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        self.meanBlurKernelSizeSlider = self.constructSliderToolWidget("MeanBlurTool","Kernel Size")
        self.meanBlurKernelSizeSlider.setMinimum(1)
        self.meanBlurKernelSizeSlider.setSingleStep(1)
        self.meanBlurKernelSizeSlider.setMaximum(200)
        self.meanBlurKernelSizeSlider.setValue(1)
        self.meanBlurKernelSizeSlider.valueChanged['int'].connect(self.meanBlurHandler)
        
        self.upadetCurrentFilterName(self.ui.MeanBlurBtn.text())
        return
    
    def setupMedianBlurTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        self.medianBlurKernelSizeSlider = self.constructSliderToolWidget("MedianBlurTool","Kernel Size")
        self.medianBlurKernelSizeSlider.setMinimum(1)
        self.medianBlurKernelSizeSlider.setSingleStep(1)
        self.medianBlurKernelSizeSlider.setMaximum(200)
        self.medianBlurKernelSizeSlider.setValue(1)
        self.medianBlurKernelSizeSlider.valueChanged['int'].connect(self.medianBlurHandler)
        
        self.upadetCurrentFilterName(self.ui.MedianBlurBtn.text())
        return
    
    def setupGaussianBlurTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
            
        self.gaussianBlurSigmaSlider = self.constructSliderToolWidget("GaussianBlurTool","Sigma")
        self.gaussianBlurSigmaSlider.setMinimum(1)
        self.gaussianBlurSigmaSlider.setSingleStep(1)
        self.gaussianBlurSigmaSlider.setMaximum(20)
        self.gaussianBlurSigmaSlider.setValue(1)
        
        self.gaussianBlurKernelSizeSlider = self.constructSliderToolWidget("GaussianBlurKernelSizeTool","Kernel Size")
        self.gaussianBlurKernelSizeSlider.setMinimum(1)
        self.gaussianBlurKernelSizeSlider.setSingleStep(1)
        self.gaussianBlurKernelSizeSlider.setMaximum(200)
        self.gaussianBlurKernelSizeSlider.setValue(1)
        
        self.gaussianBlurSigmaSlider.valueChanged['int'].connect(self.gaussianBlurHandler)
        self.gaussianBlurKernelSizeSlider.valueChanged['int'].connect(self.gaussianBlurHandler)
        
        self.upadetCurrentFilterName(self.ui.GaussienBlurBtn.text())
        return
    
    def setupGradiantEdgeDetectionTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        
        self.gradiantHandler()
        
        self.upadetCurrentFilterName(self.ui.GradiantBtn.text())
        return
    
    def setupSobelEdgeDetectionTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        
        self.sobelHandler()
        
        self.upadetCurrentFilterName(self.ui.SobelBtn.text())
        return
    
    def setupLaplacianEdgeDetectionTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        
        self.laplacianHandler()
        
        self.upadetCurrentFilterName(self.ui.LaplacianBtn.text())
        return
    
    def setupKirschEdgeDetectionTool(self):
        return
    
    def setupRobertsEdgeDetectionTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        
        self.robertsHandler()
        
        self.upadetCurrentFilterName(self.ui.RobertsBtn.text())
        return
    
    def setupPrewittEdgeDetectionTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        
        self.prewittHandler()
        
        self.upadetCurrentFilterName(self.ui.PrewittBtn.text())
        return
    
    def setupCannyEdgeDetectionTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        
        self.cannyHandler()
        
        self.upadetCurrentFilterName(self.ui.CannyBtn.text())
        return
    
    def setupSiftPOIDetectionTool(self):
        return
    
    def setupHoughPOIDetectionTool(self):
        return
    
    def setupHarrisPOIDetectionTool(self):
        return
    
    def setupRegionGrowingSegmentationTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        
        self.regionGrowingHandler()
        
        self.upadetCurrentFilterName(self.ui.RegionGrowingBtn.text())
        return
    
    def setupWatershedSegmentationTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        
        self.watershedHandler()
        
        self.upadetCurrentFilterName(self.ui.KMeansBtn.text())
        return
    
    def setupRegionPartitioningSegmentationTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        
        self.regionSplittingHandler()
        
        self.upadetCurrentFilterName(self.ui.RegionPartitionBtn.text())
        return
    
    def setupKMeansSegmentationTool(self):
        if self.ui.AdjustToolFrameLayout.children:
            self.clearAdjustToolFrame()
        
        self.kmeansHandler()
        
        self.upadetCurrentFilterName(self.ui.KMeansBtn.text())
        return
    
if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    sys.exit(app.exec())