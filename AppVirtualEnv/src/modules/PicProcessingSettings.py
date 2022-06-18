
from PySide6.QtCore import (Qt)
from PySide6.QtWidgets import (QFileDialog)
from PySide6.QtGui import (QImage, QPixmap)
import cv2

class PicProcessingSettings(object):
    def __init__(self,image):
        self.actions = False
        self.image = image
        
        self.filename = None
        self.tmp = None
        self.pixmap = None
    
    def initApp(self):
        self.pixmap = self.ui.Image.pixmap()
        self.image = cv2.imread("C:\\Users\\amine\\OneDrive\\Desktop\\Programming\\Python\\workspace\\computer vision\\ComputerVisionApp\\AppVirtualEnv\\src\\assets\\as11.png")
        self.setPicture(self.image)

    def loadImageFile(self):
        self.filename = QFileDialog.getOpenFileName(self,"Open File","C:\\Users\\amine\\OneDrive\\Desktop\\Programming\\Python\\workspace\\computer vision\\ComputerVisionApp\\AppVirtualEnv\\src\\assets","All Files (*)")
        self.image = cv2.imread(self.filename[0])
        self.setImage(self.image)
    
    def saveImageFile(self):
        return
    
    def resetImage(self):
        return
    
    def addAction(self):
        return
    
    def undoLastImageAction(self):
        return
    
    def setImage(self,image):
        self.tmp = image
        frame = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        image = QImage(frame,frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.pixmap = QPixmap.fromImage(image)
        sclaedPixMap = self.pixmap.scaled(801, 481, Qt.KeepAspectRatio)
        self.ui.Image.setPixmap(QPixmap(sclaedPixMap))
    
    