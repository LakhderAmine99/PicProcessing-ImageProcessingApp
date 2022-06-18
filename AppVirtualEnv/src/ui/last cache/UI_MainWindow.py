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
        MainWindow.resize(1050, 650)
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
"	height:56px;\n"
"}\n"
"\n"
"#scrollAreaWidgetContents QLabel{\n"
"	color:rgba(0, 208, 255,0.7);\n"
"	font-size:18px;\n"
"	padding:20px;\n"
"	padding-left:13px;\n"
"	border-bottom:1px solid rgb(206, 206, 206);\n"
"}\n"
"\n"
"#SettingsSideBar QPushButton{\n"
"background-color: rgba(0, 0, 0,0);\n"
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
"background-color:rgb(12, 12, 12);")
        self.SettingsSideBar.setFrameShape(QFrame.StyledPanel)
        self.SettingsSideBar.setFrameShadow(QFrame.Raised)
        self.OpenImageBtn = QPushButton(self.SettingsSideBar)
        self.OpenImageBtn.setObjectName(u"OpenImageBtn")
        self.OpenImageBtn.setGeometry(QRect(0, 110, 201, 41))
        self.OpenImageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.OpenImageBtn.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0,0);\n"
"height:50px;\n"
"margin-bottom:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(0, 130, 220);\n"
"}")
        self.OpenImageBtn.setCheckable(False)
        self.OpenImageBtn.setAutoDefault(False)
        self.OpenImageBtn.setFlat(True)
        self.SaveImageBtn = QPushButton(self.SettingsSideBar)
        self.SaveImageBtn.setObjectName(u"SaveImageBtn")
        self.SaveImageBtn.setGeometry(QRect(0, 160, 201, 41))
        self.SaveImageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.SaveImageBtn.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0,0);\n"
"height:50px;\n"
"margin-bottom:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(0, 130, 220);\n"
"}")
        self.AdjustImageBtn = QPushButton(self.SettingsSideBar)
        self.AdjustImageBtn.setObjectName(u"AdjustImageBtn")
        self.AdjustImageBtn.setGeometry(QRect(0, 210, 201, 41))
        self.AdjustImageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.AdjustImageBtn.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0,0);\n"
"height:50px;\n"
"margin-bottom:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(0, 130, 220);\n"
"}")
        self.UndoBtn = QPushButton(self.SettingsSideBar)
        self.UndoBtn.setObjectName(u"UndoBtn")
        self.UndoBtn.setGeometry(QRect(0, 260, 201, 41))
        self.UndoBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.UndoBtn.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0,0);\n"
"height:50px;\n"
"margin-bottom:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(0, 130, 220);\n"
"}")
        self.ResetBtn = QPushButton(self.SettingsSideBar)
        self.ResetBtn.setObjectName(u"ResetBtn")
        self.ResetBtn.setGeometry(QRect(0, 310, 201, 41))
        self.ResetBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ResetBtn.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0,0);\n"
"height:50px;\n"
"margin-bottom:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(0, 130, 220);\n"
"}")
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
        self.SwitchViewBtn = QPushButton(self.SettingsSideBar)
        self.SwitchViewBtn.setObjectName(u"SwitchViewBtn")
        self.SwitchViewBtn.setGeometry(QRect(0, 360, 201, 41))
        self.SwitchViewBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.SwitchViewBtn.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0,0);\n"
"height:50px;\n"
"margin-bottom:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(0, 130, 220);\n"
"}")
        self.Image = QLabel(self.centralwidget)
        self.Image.setObjectName(u"Image")
        self.Image.setGeometry(QRect(208, 20, 801, 481))
        self.Image.setCursor(QCursor(Qt.SizeHorCursor))
        self.Image.setAlignment(Qt.AlignCenter)
        self.FiltersBtn = QPushButton(self.centralwidget)
        self.FiltersBtn.setObjectName(u"FiltersBtn")
        self.FiltersBtn.setGeometry(QRect(820, 590, 221, 51))
        self.FiltersBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.FiltersBtn.setStyleSheet(u"QPushButton{\n"
"border-radius:8px;\n"
"color:white;\n"
"font-size:16px;\n"
"background-color: rgb(0, 30, 50);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(0, 130, 220);\n"
"}\n"
"")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(820, 30, 231, 461))
        self.scrollArea.setStyleSheet(u"background-color:rgba(0, 0, 0,0.4);\n"
"border:none;\n"
"border-radius:12px;")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 227, 2128))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.NoEffectsBtn = QPushButton(self.scrollAreaWidgetContents)
        self.NoEffectsBtn.setObjectName(u"NoEffectsBtn")
        self.NoEffectsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.NoEffectsBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(1, 234, 255);\n"
"background-color:rgba(0, 179, 255, 50)\n"
"}")

        self.verticalLayout.addWidget(self.NoEffectsBtn)

        self.labelLight = QLabel(self.scrollAreaWidgetContents)
        self.labelLight.setObjectName(u"labelLight")
        self.labelLight.setStyleSheet(u"background-color:rgba(1, 230, 255, 40);")

        self.verticalLayout.addWidget(self.labelLight)

        self.BrightnessBtn = QPushButton(self.scrollAreaWidgetContents)
        self.BrightnessBtn.setObjectName(u"BrightnessBtn")
        self.BrightnessBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.BrightnessBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(1, 234, 255);\n"
"background-color:rgba(0, 179, 255, 50)\n"
"}")

        self.verticalLayout.addWidget(self.BrightnessBtn)

        self.ContrastBtn = QPushButton(self.scrollAreaWidgetContents)
        self.ContrastBtn.setObjectName(u"ContrastBtn")
        self.ContrastBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ContrastBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(1, 234, 255);\n"
"background-color:rgba(0, 179, 255, 50)\n"
"}")

        self.verticalLayout.addWidget(self.ContrastBtn)

        self.HighlightsBtn = QPushButton(self.scrollAreaWidgetContents)
        self.HighlightsBtn.setObjectName(u"HighlightsBtn")
        self.HighlightsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.HighlightsBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(1, 234, 255);\n"
"background-color:rgba(0, 179, 255, 50)\n"
"}")

        self.verticalLayout.addWidget(self.HighlightsBtn)

        self.ShadowsBtn = QPushButton(self.scrollAreaWidgetContents)
        self.ShadowsBtn.setObjectName(u"ShadowsBtn")
        self.ShadowsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ShadowsBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(1, 234, 255);\n"
"background-color:rgba(0, 179, 255, 50)\n"
"}")

        self.verticalLayout.addWidget(self.ShadowsBtn)

        self.labelColour = QLabel(self.scrollAreaWidgetContents)
        self.labelColour.setObjectName(u"labelColour")
        self.labelColour.setStyleSheet(u"background-color:rgba(1, 230, 255, 40);")

        self.verticalLayout.addWidget(self.labelColour)

        self.InvertBtn = QPushButton(self.scrollAreaWidgetContents)
        self.InvertBtn.setObjectName(u"InvertBtn")
        self.InvertBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(1, 234, 255);\n"
"background-color:rgba(0, 179, 255, 50)\n"
"}")

        self.verticalLayout.addWidget(self.InvertBtn)

        self.SaturationBtn = QPushButton(self.scrollAreaWidgetContents)
        self.SaturationBtn.setObjectName(u"SaturationBtn")
        self.SaturationBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(1, 234, 255);\n"
"background-color:rgba(0, 179, 255, 50)\n"
"}")

        self.verticalLayout.addWidget(self.SaturationBtn)

        self.WarmthBtn = QPushButton(self.scrollAreaWidgetContents)
        self.WarmthBtn.setObjectName(u"WarmthBtn")
        self.WarmthBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(1, 234, 255);\n"
"background-color:rgba(0, 179, 255, 50)\n"
"}")

        self.verticalLayout.addWidget(self.WarmthBtn)

        self.TintBtn = QPushButton(self.scrollAreaWidgetContents)
        self.TintBtn.setObjectName(u"TintBtn")
        self.TintBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(1, 234, 255);\n"
"background-color:rgba(0, 179, 255, 50)\n"
"}")

        self.verticalLayout.addWidget(self.TintBtn)

        self.GrayScaleBtn = QPushButton(self.scrollAreaWidgetContents)
        self.GrayScaleBtn.setObjectName(u"GrayScaleBtn")
        self.GrayScaleBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(1, 234, 255);\n"
"background-color:rgba(0, 179, 255, 50)\n"
"}")

        self.verticalLayout.addWidget(self.GrayScaleBtn)

        self.labelColour_2 = QLabel(self.scrollAreaWidgetContents)
        self.labelColour_2.setObjectName(u"labelColour_2")
        self.labelColour_2.setStyleSheet(u"background-color:rgba(1, 230, 255, 40);")

        self.verticalLayout.addWidget(self.labelColour_2)

        self.HistBtn = QPushButton(self.scrollAreaWidgetContents)
        self.HistBtn.setObjectName(u"HistBtn")
        self.HistBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(0, 255, 183);\n"
"background-color:rgba(0, 255, 217, 40)\n"
"}")
        self.HistBtn.setAutoDefault(False)

        self.verticalLayout.addWidget(self.HistBtn)

        self.HistEqualizerBtn = QPushButton(self.scrollAreaWidgetContents)
        self.HistEqualizerBtn.setObjectName(u"HistEqualizerBtn")
        self.HistEqualizerBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(0, 255, 183);\n"
"background-color:rgba(0, 255, 217, 40)\n"
"}")

        self.verticalLayout.addWidget(self.HistEqualizerBtn)

        self.HistStretchBtn = QPushButton(self.scrollAreaWidgetContents)
        self.HistStretchBtn.setObjectName(u"HistStretchBtn")
        self.HistStretchBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(0, 255, 183);\n"
"background-color:rgba(0, 255, 217, 40)\n"
"}")

        self.verticalLayout.addWidget(self.HistStretchBtn)

        self.labelColour_3 = QLabel(self.scrollAreaWidgetContents)
        self.labelColour_3.setObjectName(u"labelColour_3")
        self.labelColour_3.setStyleSheet(u"background-color:rgba(1, 230, 255, 40);")

        self.verticalLayout.addWidget(self.labelColour_3)

        self.ManualTresholdingBtn = QPushButton(self.scrollAreaWidgetContents)
        self.ManualTresholdingBtn.setObjectName(u"ManualTresholdingBtn")
        self.ManualTresholdingBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(0, 255, 183);\n"
"background-color:rgba(0, 255, 217, 40)\n"
"}")

        self.verticalLayout.addWidget(self.ManualTresholdingBtn)

        self.OtsuTresholdingBtn = QPushButton(self.scrollAreaWidgetContents)
        self.OtsuTresholdingBtn.setObjectName(u"OtsuTresholdingBtn")
        self.OtsuTresholdingBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(0, 255, 183);\n"
"background-color:rgba(0, 255, 217, 40)\n"
"}")

        self.verticalLayout.addWidget(self.OtsuTresholdingBtn)

        self.labelColour_4 = QLabel(self.scrollAreaWidgetContents)
        self.labelColour_4.setObjectName(u"labelColour_4")
        self.labelColour_4.setStyleSheet(u"background-color:rgba(1, 230, 255, 40);")

        self.verticalLayout.addWidget(self.labelColour_4)

        self.GaussienBlurBtn = QPushButton(self.scrollAreaWidgetContents)
        self.GaussienBlurBtn.setObjectName(u"GaussienBlurBtn")
        self.GaussienBlurBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(255, 0, 242);\n"
"background-color:rgba(183, 0, 255, 40)\n"
"}")

        self.verticalLayout.addWidget(self.GaussienBlurBtn)

        self.MeanBlurBtn = QPushButton(self.scrollAreaWidgetContents)
        self.MeanBlurBtn.setObjectName(u"MeanBlurBtn")
        self.MeanBlurBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(255, 0, 242);\n"
"background-color:rgba(183, 0, 255, 40)\n"
"}")

        self.verticalLayout.addWidget(self.MeanBlurBtn)

        self.MedianBlurBtn = QPushButton(self.scrollAreaWidgetContents)
        self.MedianBlurBtn.setObjectName(u"MedianBlurBtn")
        self.MedianBlurBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(255, 0, 242);\n"
"background-color:rgba(183, 0, 255, 40)\n"
"}")

        self.verticalLayout.addWidget(self.MedianBlurBtn)

        self.labelColour_5 = QLabel(self.scrollAreaWidgetContents)
        self.labelColour_5.setObjectName(u"labelColour_5")
        self.labelColour_5.setStyleSheet(u"background-color:rgba(1, 230, 255, 40);")

        self.verticalLayout.addWidget(self.labelColour_5)

        self.ErosionBtn = QPushButton(self.scrollAreaWidgetContents)
        self.ErosionBtn.setObjectName(u"ErosionBtn")
        self.ErosionBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(255, 200, 0);\n"
"background-color:rgba(255, 162, 0, 40)\n"
"}")

        self.verticalLayout.addWidget(self.ErosionBtn)

        self.DilationBtn = QPushButton(self.scrollAreaWidgetContents)
        self.DilationBtn.setObjectName(u"DilationBtn")
        self.DilationBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(255, 200, 0);\n"
"background-color:rgba(255, 162, 0, 40)\n"
"}")

        self.verticalLayout.addWidget(self.DilationBtn)

        self.OpeningBtn = QPushButton(self.scrollAreaWidgetContents)
        self.OpeningBtn.setObjectName(u"OpeningBtn")
        self.OpeningBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(255, 200, 0);\n"
"background-color:rgba(255, 162, 0, 40)\n"
"}")

        self.verticalLayout.addWidget(self.OpeningBtn)

        self.ClosingBtn = QPushButton(self.scrollAreaWidgetContents)
        self.ClosingBtn.setObjectName(u"ClosingBtn")
        self.ClosingBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(255, 200, 0);\n"
"background-color:rgba(255, 162, 0, 40)\n"
"}")

        self.verticalLayout.addWidget(self.ClosingBtn)

        self.labelColour_6 = QLabel(self.scrollAreaWidgetContents)
        self.labelColour_6.setObjectName(u"labelColour_6")
        self.labelColour_6.setStyleSheet(u"background-color:rgba(1, 230, 255, 40);")

        self.verticalLayout.addWidget(self.labelColour_6)

        self.GradiantBtn = QPushButton(self.scrollAreaWidgetContents)
        self.GradiantBtn.setObjectName(u"GradiantBtn")
        self.GradiantBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(76, 255, 0);\n"
"background-color:rgba(49, 255, 3, 40)\n"
"}")

        self.verticalLayout.addWidget(self.GradiantBtn)

        self.SobelBtn = QPushButton(self.scrollAreaWidgetContents)
        self.SobelBtn.setObjectName(u"SobelBtn")
        self.SobelBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(76, 255, 0);\n"
"background-color:rgba(49, 255, 3, 40)\n"
"}")

        self.verticalLayout.addWidget(self.SobelBtn)

        self.KirschBtn = QPushButton(self.scrollAreaWidgetContents)
        self.KirschBtn.setObjectName(u"KirschBtn")
        self.KirschBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(76, 255, 0);\n"
"background-color:rgba(49, 255, 3, 40)\n"
"}")

        self.verticalLayout.addWidget(self.KirschBtn)

        self.RobinsonBtn = QPushButton(self.scrollAreaWidgetContents)
        self.RobinsonBtn.setObjectName(u"RobinsonBtn")
        self.RobinsonBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(76, 255, 0);\n"
"background-color:rgba(49, 255, 3, 40)\n"
"}")

        self.verticalLayout.addWidget(self.RobinsonBtn)

        self.LaplacianBtn = QPushButton(self.scrollAreaWidgetContents)
        self.LaplacianBtn.setObjectName(u"LaplacianBtn")
        self.LaplacianBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(76, 255, 0);\n"
"background-color:rgba(49, 255, 3, 40)\n"
"}")

        self.verticalLayout.addWidget(self.LaplacianBtn)

        self.SiftBtn = QPushButton(self.scrollAreaWidgetContents)
        self.SiftBtn.setObjectName(u"SiftBtn")
        self.SiftBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(76, 255, 0);\n"
"background-color:rgba(49, 255, 3, 40)\n"
"}")

        self.verticalLayout.addWidget(self.SiftBtn)

        self.HarrisBtn = QPushButton(self.scrollAreaWidgetContents)
        self.HarrisBtn.setObjectName(u"HarrisBtn")
        self.HarrisBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(76, 255, 0);\n"
"background-color:rgba(49, 255, 3, 40)\n"
"}")

        self.verticalLayout.addWidget(self.HarrisBtn)

        self.HoughBtn = QPushButton(self.scrollAreaWidgetContents)
        self.HoughBtn.setObjectName(u"HoughBtn")
        self.HoughBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.HoughBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(76, 255, 0);\n"
"background-color:rgba(49, 255, 3, 40)\n"
"}")

        self.verticalLayout.addWidget(self.HoughBtn)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.AdjustArea = QFrame(self.centralwidget)
        self.AdjustArea.setObjectName(u"AdjustArea")
        self.AdjustArea.setEnabled(True)
        self.AdjustArea.setGeometry(QRect(209, 509, 601, 131))
        self.AdjustArea.setStyleSheet(u"border:none;")
        self.AdjustArea.setFrameShape(QFrame.StyledPanel)
        self.AdjustArea.setFrameShadow(QFrame.Raised)
        self.Image_copy = QLabel(self.centralwidget)
        self.Image_copy.setObjectName(u"Image_copy")
        self.Image_copy.setGeometry(QRect(208, 20, 801, 481))
        self.Image_copy.setCursor(QCursor(Qt.SizeHorCursor))
        self.Image_copy.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.Image_copy.raise_()
        self.SettingsSideBar.raise_()
        self.Image.raise_()
        self.FiltersBtn.raise_()
        self.scrollArea.raise_()
        self.AdjustArea.raise_()

        self.retranslateUi(MainWindow)

        self.OpenImageBtn.setDefault(False)


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
        self.SwitchViewBtn.setText(QCoreApplication.translate("MainWindow", u"Switch View", None))
        self.Image.setText("")
        self.FiltersBtn.setText(QCoreApplication.translate("MainWindow", u"No Filters", None))
        self.NoEffectsBtn.setText(QCoreApplication.translate("MainWindow", u"No Effects", None))
        self.labelLight.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.BrightnessBtn.setText(QCoreApplication.translate("MainWindow", u"Brightness", None))
        self.ContrastBtn.setText(QCoreApplication.translate("MainWindow", u"Contrast", None))
        self.HighlightsBtn.setText(QCoreApplication.translate("MainWindow", u"Highlights", None))
        self.ShadowsBtn.setText(QCoreApplication.translate("MainWindow", u"Shadows", None))
        self.labelColour.setText(QCoreApplication.translate("MainWindow", u"Colour", None))
        self.InvertBtn.setText(QCoreApplication.translate("MainWindow", u"Invert", None))
        self.SaturationBtn.setText(QCoreApplication.translate("MainWindow", u"Saturation", None))
        self.WarmthBtn.setText(QCoreApplication.translate("MainWindow", u"Warmth", None))
        self.TintBtn.setText(QCoreApplication.translate("MainWindow", u"Tint", None))
        self.GrayScaleBtn.setText(QCoreApplication.translate("MainWindow", u"GrayScale", None))
        self.labelColour_2.setText(QCoreApplication.translate("MainWindow", u"Histogram", None))
        self.HistBtn.setText(QCoreApplication.translate("MainWindow", u"Histogram", None))
        self.HistEqualizerBtn.setText(QCoreApplication.translate("MainWindow", u"Equalizer", None))
        self.HistStretchBtn.setText(QCoreApplication.translate("MainWindow", u"Stretch", None))
        self.labelColour_3.setText(QCoreApplication.translate("MainWindow", u"Binarization", None))
        self.ManualTresholdingBtn.setText(QCoreApplication.translate("MainWindow", u"Manual Binarize", None))
        self.OtsuTresholdingBtn.setText(QCoreApplication.translate("MainWindow", u"Otsu Binarize", None))
        self.labelColour_4.setText(QCoreApplication.translate("MainWindow", u"Blur Filters", None))
        self.GaussienBlurBtn.setText(QCoreApplication.translate("MainWindow", u"Gaussien Blur", None))
        self.MeanBlurBtn.setText(QCoreApplication.translate("MainWindow", u"Mean Blur", None))
        self.MedianBlurBtn.setText(QCoreApplication.translate("MainWindow", u"Median Blur", None))
        self.labelColour_5.setText(QCoreApplication.translate("MainWindow", u"Morphology", None))
        self.ErosionBtn.setText(QCoreApplication.translate("MainWindow", u"Erosion", None))
        self.DilationBtn.setText(QCoreApplication.translate("MainWindow", u"Dilation", None))
        self.OpeningBtn.setText(QCoreApplication.translate("MainWindow", u"Opening", None))
        self.ClosingBtn.setText(QCoreApplication.translate("MainWindow", u"Closing", None))
        self.labelColour_6.setText(QCoreApplication.translate("MainWindow", u"Edge Extraction", None))
        self.GradiantBtn.setText(QCoreApplication.translate("MainWindow", u"Gradiant", None))
        self.SobelBtn.setText(QCoreApplication.translate("MainWindow", u"Sobel", None))
        self.KirschBtn.setText(QCoreApplication.translate("MainWindow", u"Kirsch", None))
        self.RobinsonBtn.setText(QCoreApplication.translate("MainWindow", u"Robinson", None))
        self.LaplacianBtn.setText(QCoreApplication.translate("MainWindow", u"Laplacian", None))
        self.SiftBtn.setText(QCoreApplication.translate("MainWindow", u"Sift", None))
        self.HarrisBtn.setText(QCoreApplication.translate("MainWindow", u"Harris", None))
        self.HoughBtn.setText(QCoreApplication.translate("MainWindow", u"hough", None))
        self.Image_copy.setText("")
    # retranslateUi

