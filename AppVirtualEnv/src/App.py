import math
import sys
import random
import cv2
from cv2 import threshold
from cv2 import COLOR_RGB2GRAY
from cv2 import sqrt
import numpy as np

from src.modules.PicProcessingApp import PicProcessingApp
from PySide6.QtCore import (Qt, QRect)
from PySide6.QtGui import (QImage, QPixmap)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel,
                               QMainWindow, QVBoxLayout, QFileDialog, 
                               QSlider, QHBoxLayout)
# from src.ui.UI_MainWindow import Ui_MainWindow
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
        self.ui.ResetBtn.clicked.connect(self.resetChanges)
        self.ui.NoEffectsBtn.clicked.connect(self.noEffects)
        
        self.ui.BrightnessBtn.clicked.connect(self.setupBrightnessTool)
        self.ui.InvertBtn.clicked.connect(self.setupInvertTool)
        self.ui.GrayScaleBtn.clicked.connect(self.setupGrayScaleTool)
        
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
        
    def resetChanges(self):
        self.image = np.copy(self.persistingImage)
        self.picProcessingApp.setImage(self.image)
        self.noEffects()
        self.setPicture(self.image)
    
    def noEffects(self):
        self.clearAdjustToolFrame()
        
    def upadetCurrentFilterName(self,text):
        self.ui.FiltersBtn.setText(text)
        return
    
    ## processing callers
    
    def rotateHandler(self):
        self.imageCopy = np.copy(self.image)
        self.imageCopy = self.picProcessingApp.rotate()
        self.setPicture(self.imageCopy)
    
    def flipHandler(self):
        return
    
    def zoomInHandler(self):
        return
    
    def zoomOutHandler(self):
        return
        
    def brightnessHandler(self,value):
        self.imageCopy = np.copy(self.image)
        
        value = (value/20) + 1
                
        self.imageCopy[:,:,0] = self.imageCopy[:,:,0]/(value)
        self.imageCopy[:,:,1] = self.imageCopy[:,:,1]/(value)
        self.imageCopy[:,:,2] = self.imageCopy[:,:,2]/(value)
                                        
        self.setPicture(self.imageCopy)
   
    def contrastHandler(self,value):
        return
    
    def warmthHandler(self,value):
        return
    
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
        return
    
    def regionGrowingHandler(self):
        return
    
    def regionPartitioningHandler(self):
        return
    
    def kmeansHandler(self):
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
        return
    
    def setupZoomOutTool(self):
        return
    
    def setupFlipTool(self):
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
        return
    
    def setupWatershedSegmentationTool(self):
        return
    
    def setupRegionPartitioningSegmentationTool(self):
        return
    
    def setupKMeansSegmentationTool(self):
        return
    
if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    sys.exit(app.exec())