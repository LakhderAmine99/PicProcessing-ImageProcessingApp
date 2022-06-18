# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLayout,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1053, 650)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget\n"
"{\n"
"	background-color:rgb(0, 0, 0);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	width: 4px;\n"
"	margin: 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	min-height: 10px;\n"
"	background-color:rgb(27, 27, 27);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	background: none;\n"
"	height: 45px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"#scrollAreaWidgetContents QPushButton{\n"
"	color:white;\n"
"	font-size:14px;\n"
"	text-align:left;\n"
"	padding-left:18px;\n"
"	border-radius:4px;\n"
"	height:64px;\n"
"}\n"
"\n"
"#scrollAreaWidgetContents QPushButton::hover{\n"
"	background-color: rgba(0, 230, 255, 1);\n"
"}\n"
"\n"
"#SettingsSideBar QPushButton{\n"
"color:white;\n"
"text-align: left;\n"
"padding-left:25px;\n"
"}\n"
"")
        self.SettingsSideBar = QFrame(self.centralwidget)
        self.SettingsSideBar.setObjectName(u"SettingsSideBar")
        self.SettingsSideBar.setGeometry(QRect(-1, 9, 201, 641))
        self.SettingsSideBar.setStyleSheet(u"/**background-color:qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.517091, y2:1, stop:0 rgba(0, 0, 0, 215), stop:1 rgba(64, 64, 64, 213));**/\n"
"border:none;\n"
"border-radius:5px;\n"
"background-color:rgb(12, 12, 12);\n"
"")
        self.SettingsSideBar.setFrameShape(QFrame.StyledPanel)
        self.SettingsSideBar.setFrameShadow(QFrame.Raised)
        self.OpenImageBtn = QPushButton(self.SettingsSideBar)
        self.OpenImageBtn.setObjectName(u"OpenImageBtn")
        self.OpenImageBtn.setGeometry(QRect(0, 110, 201, 41))
        self.OpenImageBtn.setStyleSheet(u"height:50px;\n"
"padding-bottom:8px;\n"
"QPushButton::hover#OpenImageBtn{\n"
"background-color:rgb(150,12,12);\n"
"};\n"
"")
        self.OpenImageBtn.setAutoDefault(False)
        self.OpenImageBtn.setFlat(True)
        self.OpenImageBtn.setCursor(Qt.PointingHandCursor)
        self.SaveImageBtn = QPushButton(self.SettingsSideBar)
        self.SaveImageBtn.setObjectName(u"SaveImageBtn")
        self.SaveImageBtn.setCursor(Qt.PointingHandCursor)
        self.SaveImageBtn.setGeometry(QRect(0, 160, 201, 41))
        self.SaveImageBtn.setStyleSheet(u"height:50px;\n"
"padding-bottom:8px;\n"
"")
        self.AdjustImageBtn = QPushButton(self.SettingsSideBar)
        self.AdjustImageBtn.setCursor(Qt.PointingHandCursor)
        self.AdjustImageBtn.setObjectName(u"AdjustImageBtn")
        self.AdjustImageBtn.setGeometry(QRect(0, 210, 201, 41))
        self.AdjustImageBtn.setStyleSheet(u"height:50px;\n"
"padding-bottom:8px;\n"
"")
        self.UndoBtn = QPushButton(self.SettingsSideBar)
        self.UndoBtn.setCursor(Qt.PointingHandCursor)
        self.UndoBtn.setObjectName(u"UndoBtn")
        self.UndoBtn.setGeometry(QRect(0, 260, 201, 41))
        self.UndoBtn.setStyleSheet(u"height:50px;\n"
"padding-bottom:8px;\n"
"")
        self.ResetBtn = QPushButton(self.SettingsSideBar)
        self.ResetBtn.setCursor(Qt.PointingHandCursor)
        self.ResetBtn.setObjectName(u"ResetBtn")
        self.ResetBtn.setGeometry(QRect(0, 310, 201, 41))
        self.ResetBtn.setStyleSheet(u"height:50px;\n"
"padding-bottom:8px;\n"
"")
        self.MenuToggleBtn = QPushButton(self.SettingsSideBar)
        self.MenuToggleBtn.setObjectName(u"MenuToggleBtn")
        self.MenuToggleBtn.setGeometry(QRect(20, 20, 41, 31))
        self.MenuToggleBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.MenuToggleBtn.setStyleSheet(u"border:none;\n"
"background-color:none;\n"
"padding:0;\n"
"text-align:center")
        icon = QIcon()
        icon.addFile(u"D:/Programmation/DEV WEB/web dev mine/learn html css js only/images/icons desktop/icons8-menu-240.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MenuToggleBtn.setIcon(icon)
        self.MenuToggleBtn.setIconSize(QSize(32, 32))
        self.Image = QLabel(self.centralwidget)
        self.Image.setObjectName(u"Image")
        self.Image.setGeometry(QRect(208, 20, 801, 481))
        self.Image.setCursor(QCursor(Qt.SizeHorCursor))
        self.Image.setAlignment(Qt.AlignCenter)
        # pixmap = QPixmap(u"C:\\Users\\amine\\OneDrive\\Desktop\\Programming\\Python\\workspace\\computer vision\\ComputerVisionApp\\AppVirtualEnv\\src\\assets\\as11.png")
        # scaledPixMap = pixmap.scaled(801, 481, Qt.KeepAspectRatio)
        # self.Image.setPixmap(scaledPixMap)
        self.FiltersBtn = QPushButton(self.centralwidget)
        self.FiltersBtn.setObjectName(u"FiltersBtn")
        self.FiltersBtn.setGeometry(QRect(820, 590, 221, 51))
        self.FiltersBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.FiltersBtn.setStyleSheet(u"border-radius:8px;\n"
"color:white;\n"
"font-size:18px;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(82, 82, 82, 213));")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(820, 30, 221, 461))
        self.scrollArea.setStyleSheet(u"background-color:rgba(0, 0, 0,0.4);\n"
"border:none;\n"
"border-radius:12px;")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 217, 1408))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.NoEffectsBtn = QPushButton(self.scrollAreaWidgetContents)
        self.NoEffectsBtn.setObjectName(u"NoEffectsBtn")
        self.NoEffectsBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.NoEffectsBtn)

        self.BrightnessBtn = QPushButton(self.scrollAreaWidgetContents)
        self.BrightnessBtn.setObjectName(u"BrightnessBtn")
        self.BrightnessBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.BrightnessBtn)
        
        self.InvertBtn = QPushButton(self.scrollAreaWidgetContents)
        self.InvertBtn.setObjectName(u"InvertBtn")
        self.InvertBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.InvertBtn)

        self.HistBtn = QPushButton(self.scrollAreaWidgetContents)
        self.HistBtn.setObjectName(u"HistBtn")
        self.HistBtn.setStyleSheet(u"")
        self.HistBtn.setAutoDefault(False)

        self.verticalLayout.addWidget(self.HistBtn)

        self.GaussienBlurBtn = QPushButton(self.scrollAreaWidgetContents)
        self.GaussienBlurBtn.setObjectName(u"GaussienBlurBtn")
        self.GaussienBlurBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.GaussienBlurBtn)

        self.MeanBlurBtn = QPushButton(self.scrollAreaWidgetContents)
        self.MeanBlurBtn.setObjectName(u"MeanBlurBtn")
        self.MeanBlurBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.MeanBlurBtn)

        self.MedianBlurBtn = QPushButton(self.scrollAreaWidgetContents)
        self.MedianBlurBtn.setObjectName(u"MedianBlurBtn")
        self.MedianBlurBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.MedianBlurBtn)

        self.HistEqualizerBtn = QPushButton(self.scrollAreaWidgetContents)
        self.HistEqualizerBtn.setObjectName(u"HistEqualizerBtn")
        self.HistEqualizerBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.HistEqualizerBtn)

        self.HistStretchBtn = QPushButton(self.scrollAreaWidgetContents)
        self.HistStretchBtn.setObjectName(u"HistStretchBtn")
        self.HistStretchBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.HistStretchBtn)

        self.GrayScaleBtn = QPushButton(self.scrollAreaWidgetContents)
        self.GrayScaleBtn.setObjectName(u"GrayScaleBtn")
        self.GrayScaleBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.GrayScaleBtn)
        
        self.ManualTresholdingBtn = QPushButton(self.scrollAreaWidgetContents)
        self.ManualTresholdingBtn.setObjectName(u"ManualTresholdingBtn")
        self.ManualTresholdingBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.ManualTresholdingBtn) 

        self.OtsuTresholdingBtn = QPushButton(self.scrollAreaWidgetContents)
        self.OtsuTresholdingBtn.setObjectName(u"OtsuTresholdingBtn")
        self.OtsuTresholdingBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.OtsuTresholdingBtn)

        self.ErosionBtn = QPushButton(self.scrollAreaWidgetContents)
        self.ErosionBtn.setObjectName(u"ErosionBtn")
        self.ErosionBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.ErosionBtn)

        self.DilationBtn = QPushButton(self.scrollAreaWidgetContents)
        self.DilationBtn.setObjectName(u"DilationBtn")
        self.DilationBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.DilationBtn)

        self.OpeningBtn = QPushButton(self.scrollAreaWidgetContents)
        self.OpeningBtn.setObjectName(u"OpeningBtn")
        self.OpeningBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.OpeningBtn)

        self.ClosingBtn = QPushButton(self.scrollAreaWidgetContents)
        self.ClosingBtn.setObjectName(u"ClosingBtn")
        self.ClosingBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.ClosingBtn)

        self.GradiantBtn = QPushButton(self.scrollAreaWidgetContents)
        self.GradiantBtn.setObjectName(u"GradiantBtn")
        self.GradiantBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.GradiantBtn)

        self.SobelBtn = QPushButton(self.scrollAreaWidgetContents)
        self.SobelBtn.setObjectName(u"SobelBtn")
        self.SobelBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.SobelBtn)

        self.KirschBtn = QPushButton(self.scrollAreaWidgetContents)
        self.KirschBtn.setObjectName(u"KirschBtn")
        self.KirschBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.KirschBtn)

        self.RobinsonBtn = QPushButton(self.scrollAreaWidgetContents)
        self.RobinsonBtn.setObjectName(u"RobinsonBtn")
        self.RobinsonBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.RobinsonBtn)

        self.LaplacianBtn = QPushButton(self.scrollAreaWidgetContents)
        self.LaplacianBtn.setObjectName(u"LaplacianBtn")
        self.LaplacianBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.LaplacianBtn)

        self.SiftBtn = QPushButton(self.scrollAreaWidgetContents)
        self.SiftBtn.setObjectName(u"SiftBtn")
        self.SiftBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.SiftBtn)

        self.HarrisBtn = QPushButton(self.scrollAreaWidgetContents)
        self.HarrisBtn.setObjectName(u"HarrisBtn")
        self.HarrisBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.HarrisBtn)

        self.HoughBtn = QPushButton(self.scrollAreaWidgetContents)
        self.HoughBtn.setObjectName(u"HoughBtn")
        self.HoughBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.HoughBtn)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.AdjustArea = QFrame(self.centralwidget)
        self.AdjustArea.setObjectName(u"AdjustArea")
        self.AdjustArea.setEnabled(True)
        self.AdjustArea.setGeometry(QRect(209, 509, 601, 131))
        self.AdjustArea.setStyleSheet(u"border:none;")
        self.AdjustArea.setFrameShape(QFrame.StyledPanel)
        self.AdjustArea.setFrameShadow(QFrame.Raised)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Computer Vision ", None))
        self.OpenImageBtn.setText(QCoreApplication.translate("MainWindow", u"Open Image", None))
        self.SaveImageBtn.setText(QCoreApplication.translate("MainWindow", u"Save Image", None))
        self.AdjustImageBtn.setText(QCoreApplication.translate("MainWindow", u"Adjust", None))
        self.UndoBtn.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.ResetBtn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.MenuToggleBtn.setText("")
        self.Image.setText("")
        self.FiltersBtn.setText(QCoreApplication.translate("MainWindow", u"No Filters", None))
        self.NoEffectsBtn.setText(QCoreApplication.translate("MainWindow", u"No Effects", None))
        self.BrightnessBtn.setText(QCoreApplication.translate("MainWindow", u"Brightness", None))
        self.InvertBtn.setText(QCoreApplication.translate("MainWindow", u"Invert", None))
        self.HistBtn.setText(QCoreApplication.translate("MainWindow", u"Histogram", None))
        self.GaussienBlurBtn.setText(QCoreApplication.translate("MainWindow", u"Gaussien Blur", None))
        self.MeanBlurBtn.setText(QCoreApplication.translate("MainWindow", u"Mean Blur", None))
        self.MedianBlurBtn.setText(QCoreApplication.translate("MainWindow", u"Median Blur", None))
        self.HistEqualizerBtn.setText(QCoreApplication.translate("MainWindow", u"Equalizer", None))
        self.HistStretchBtn.setText(QCoreApplication.translate("MainWindow", u"Stretch", None))
        self.GrayScaleBtn.setText(QCoreApplication.translate("MainWindow", u"GrayScale", None))
        self.ManualTresholdingBtn.setText(QCoreApplication.translate("MainWindow", u"Manual Binarize", None))
        self.OtsuTresholdingBtn.setText(QCoreApplication.translate("MainWindow", u"Otsu Binarize", None))
        self.ErosionBtn.setText(QCoreApplication.translate("MainWindow", u"Erosion", None))
        self.DilationBtn.setText(QCoreApplication.translate("MainWindow", u"Dilation", None))
        self.OpeningBtn.setText(QCoreApplication.translate("MainWindow", u"Opening", None))
        self.ClosingBtn.setText(QCoreApplication.translate("MainWindow", u"Closing", None))
        self.GradiantBtn.setText(QCoreApplication.translate("MainWindow", u"Gradiant", None))
        self.SobelBtn.setText(QCoreApplication.translate("MainWindow", u"Sobel", None))
        self.KirschBtn.setText(QCoreApplication.translate("MainWindow", u"Kirsch", None))
        self.RobinsonBtn.setText(QCoreApplication.translate("MainWindow", u"Robinson", None))
        self.LaplacianBtn.setText(QCoreApplication.translate("MainWindow", u"Laplacian", None))
        self.SiftBtn.setText(QCoreApplication.translate("MainWindow", u"Sift", None))
        self.HarrisBtn.setText(QCoreApplication.translate("MainWindow", u"Harris", None))
        self.HoughBtn.setText(QCoreApplication.translate("MainWindow", u"hough", None))
    # retranslateUi

