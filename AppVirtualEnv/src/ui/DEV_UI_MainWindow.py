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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1207, 767)
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
"#lightColorScrollAreaWidgetContents  QPushButton{\n"
"	color:white;\n"
"	font-size:14px;\n"
"	text-align:left;\n"
"	padding-left:18px;\n"
"	height:56px;\n"
"}\n"
"\n"
"#lightColorScrollAreaWidgetContents QLabel{\n"
"	color:rgba(0, 208, 255,0.7);\n"
"	font-size:18px;\n"
"	padding:20px;\n"
"	padding-left:13px;\n"
"	border-bottom:1px solid rgb(206, 206, 206);\n"
"}\n"
"\n"
"\n"
"#scrollAreaWidgetContents QLabel{\n"
"	color:rgba(0, 208, 255,0.7);\n"
"	font-size:18px;\n"
""
                        "	padding:20px;\n"
"	padding-left:13px;\n"
"	border-bottom:1px solid rgb(206, 206, 206);\n"
"}\n"
"\n"
"#SettingsSideBar QPushButton{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:white;\n"
"text-align: left;\n"
"padding-left:25px;\n"
"}\n"
"")
        self.SettingsSideBar = QFrame(self.centralwidget)
        self.SettingsSideBar.setObjectName(u"SettingsSideBar")
        self.SettingsSideBar.setGeometry(QRect(-1, 9, 201, 761))
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
"background-color: rgba(0, 0, 0, 0);\n"
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
"background-color: rgba(0, 0, 0, 0);\n"
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
"background-color: rgba(0, 0, 0, 0);\n"
"height:50px;\n"
"margin-bottom:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(0, 130, 220);\n"
"}")
        self.UndoBtn = QPushButton(self.SettingsSideBar)
        self.UndoBtn.setObjectName(u"UndoBtn")
        self.UndoBtn.setGeometry(QRect(0, 310, 201, 41))
        self.UndoBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.UndoBtn.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"height:50px;\n"
"margin-bottom:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(0, 130, 220);\n"
"}")
        self.ResetBtn = QPushButton(self.SettingsSideBar)
        self.ResetBtn.setObjectName(u"ResetBtn")
        self.ResetBtn.setGeometry(QRect(0, 360, 201, 41))
        self.ResetBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ResetBtn.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 0);\n"
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
        self.SwitchViewBtn.setGeometry(QRect(0, 410, 201, 41))
        self.SwitchViewBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.SwitchViewBtn.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"height:50px;\n"
"margin-bottom:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(0, 130, 220);\n"
"}")
        self.EditImageBtn = QPushButton(self.SettingsSideBar)
        self.EditImageBtn.setObjectName(u"EditImageBtn")
        self.EditImageBtn.setGeometry(QRect(0, 260, 201, 41))
        self.EditImageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.EditImageBtn.setStyleSheet(u"QPushButton{\n"
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
        self.Image.setGeometry(QRect(208, 0, 991, 631))
        self.Image.setCursor(QCursor(Qt.SizeHorCursor))
        self.Image.setAlignment(Qt.AlignCenter)
        self.FiltersBtn = QPushButton(self.centralwidget)
        self.FiltersBtn.setObjectName(u"FiltersBtn")
        self.FiltersBtn.setGeometry(QRect(980, 710, 221, 51))
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
        self.FiltersScrollArea = QScrollArea(self.centralwidget)
        self.FiltersScrollArea.setObjectName(u"FiltersScrollArea")
        self.FiltersScrollArea.setEnabled(True)
        self.FiltersScrollArea.setGeometry(QRect(940, 20, 261, 591))
        self.FiltersScrollArea.setStyleSheet(u"background-color:rgba(0, 0, 0,0.4);\n"
"border:none;\n"
"border-radius:12px;")
        self.FiltersScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.FiltersScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.FiltersScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 257, 1264))
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
        
        self.PrewittBtn = QPushButton(self.scrollAreaWidgetContents)
        self.PrewittBtn.setObjectName(u"ِPrewittBtn")
        self.PrewittBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(76, 255, 0);\n"
"background-color:rgba(49, 255, 3, 40)\n"
"}")

        self.verticalLayout.addWidget(self.PrewittBtn)
        
        self.CannyBtn = QPushButton(self.scrollAreaWidgetContents)
        self.CannyBtn.setObjectName(u"ِCannyBtn")
        self.CannyBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(76, 255, 0);\n"
"background-color:rgba(49, 255, 3, 40)\n"
"}")

        self.verticalLayout.addWidget(self.CannyBtn)

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
        
        self.labelColour_7 = QLabel(self.scrollAreaWidgetContents)
        self.labelColour_7.setObjectName(u"labelColour_7")
        self.labelColour_7.setStyleSheet(u"background-color:rgba(1, 230, 255, 40);")

        self.verticalLayout.addWidget(self.labelColour_7)
        
        self.RegionGrowingBtn = QPushButton(self.scrollAreaWidgetContents)
        self.RegionGrowingBtn.setObjectName(u"RegionGrowingBtn")
        self.RegionGrowingBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.RegionGrowingBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(76, 90, 255);\n"
"background-color:rgba(49, 49, 255, 40)\n"
"}")

        self.verticalLayout.addWidget(self.RegionGrowingBtn)

        self.FiltersScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.AdjustArea = QFrame(self.centralwidget)
        self.AdjustArea.setObjectName(u"AdjustArea")
        self.AdjustArea.setEnabled(True)
        self.AdjustArea.setGeometry(QRect(209, 639, 761, 131))
        self.AdjustArea.setStyleSheet(u"border:none;")
        self.AdjustArea.setFrameShape(QFrame.StyledPanel)
        self.AdjustArea.setFrameShadow(QFrame.Raised)
        self.AdjustToolFrameLayout = QVBoxLayout(self.AdjustArea)
        self.AdjustToolFrameLayout.setObjectName(u"AdjustToolFrameLayout")
        self.Image_copy = QLabel(self.centralwidget)
        self.Image_copy.setObjectName(u"Image_copy")
        self.Image_copy.setGeometry(QRect(208, 0, 991, 631))
        self.Image_copy.setCursor(QCursor(Qt.SizeHorCursor))
        self.Image_copy.setAlignment(Qt.AlignCenter)
        self.AdjustMenu = QFrame(self.centralwidget)
        self.AdjustMenu.setObjectName(u"AdjustMenu")
        self.AdjustMenu.setEnabled(True)
        self.AdjustMenu.setGeometry(QRect(220, 220, 61, 281))
        self.AdjustMenu.setStyleSheet(u"border:none;\n"
"border-radius:12px;\n"
"background-color: rgba(0, 0, 0, 0.7);")
        self.AdjustMenu.setFrameShape(QFrame.StyledPanel)
        self.AdjustMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.AdjustMenu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.RotateBtn = QPushButton(self.AdjustMenu)
        self.RotateBtn.setObjectName(u"RotateBtn")
        self.RotateBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.RotateBtn.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"height:100px;\n"
"border-radius:12px;\n"
"background-color:rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"D:/designs-web/z14.png", QSize(), QIcon.Normal, QIcon.Off)
        self.RotateBtn.setIcon(icon1)
        self.RotateBtn.setIconSize(QSize(30, 32))
        self.RotateBtn.setCheckable(False)
        self.RotateBtn.setAutoDefault(False)
        self.RotateBtn.setFlat(True)

        self.verticalLayout_2.addWidget(self.RotateBtn)

        self.ZoomInBtn = QPushButton(self.AdjustMenu)
        self.ZoomInBtn.setObjectName(u"ZoomInBtn")
        self.ZoomInBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ZoomInBtn.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"height:100px;\n"
"border-radius:12px;\n"
"background-color:rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"D:/designs-web/z2 - Copy1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ZoomInBtn.setIcon(icon2)
        self.ZoomInBtn.setIconSize(QSize(32, 40))
        self.ZoomInBtn.setCheckable(False)
        self.ZoomInBtn.setAutoDefault(False)
        self.ZoomInBtn.setFlat(True)

        self.verticalLayout_2.addWidget(self.ZoomInBtn)

        self.ZoomOutBtn = QPushButton(self.AdjustMenu)
        self.ZoomOutBtn.setObjectName(u"ZoomOutBtn")
        self.ZoomOutBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ZoomOutBtn.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"height:100px;\n"
"border-radius:12px;\n"
"background-color:rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"D:/designs-web/z2 - Copy3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ZoomOutBtn.setIcon(icon3)
        self.ZoomOutBtn.setIconSize(QSize(32, 40))
        self.ZoomOutBtn.setCheckable(False)
        self.ZoomOutBtn.setAutoDefault(False)
        self.ZoomOutBtn.setFlat(True)

        self.verticalLayout_2.addWidget(self.ZoomOutBtn)

        self.FlipBtn = QPushButton(self.AdjustMenu)
        self.FlipBtn.setObjectName(u"FlipBtn")
        self.FlipBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.FlipBtn.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"height:100px;\n"
"border-radius:12px;\n"
"background-color:rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"D:/designs-web/z5.png", QSize(), QIcon.Normal, QIcon.Off)
        self.FlipBtn.setIcon(icon4)
        self.FlipBtn.setIconSize(QSize(32, 40))
        self.FlipBtn.setCheckable(False)
        self.FlipBtn.setAutoDefault(False)
        self.FlipBtn.setFlat(True)

        self.verticalLayout_2.addWidget(self.FlipBtn)

        self.CropBtn = QPushButton(self.AdjustMenu)
        self.CropBtn.setObjectName(u"CropBtn")
        self.CropBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.CropBtn.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"height:100px;\n"
"border-radius:12px;\n"
"background-color:rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"D:/designs-web/z12.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CropBtn.setIcon(icon5)
        self.CropBtn.setIconSize(QSize(28, 28))
        self.CropBtn.setCheckable(False)
        self.CropBtn.setAutoDefault(False)
        self.CropBtn.setFlat(True)

        self.verticalLayout_2.addWidget(self.CropBtn)

        self.ViewSwitchedBtn = QPushButton(self.AdjustMenu)
        self.ViewSwitchedBtn.setObjectName(u"ViewSwitchedBtn")
        self.ViewSwitchedBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ViewSwitchedBtn.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"height:100px;\n"
"border-radius:12px;\n"
"background-color:rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"D:/designs-web/z6.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ViewSwitchedBtn.setIcon(icon6)
        self.ViewSwitchedBtn.setIconSize(QSize(35, 28))
        self.ViewSwitchedBtn.setCheckable(False)
        self.ViewSwitchedBtn.setAutoDefault(False)
        self.ViewSwitchedBtn.setFlat(True)

        self.verticalLayout_2.addWidget(self.ViewSwitchedBtn)

        self.AdjustTopMenu = QFrame(self.centralwidget)
        self.AdjustTopMenu.setObjectName(u"AdjustTopMenu")
        self.AdjustTopMenu.setEnabled(True)
        self.AdjustTopMenu.setGeometry(QRect(370, 20, 561, 61))
        self.AdjustTopMenu.setStyleSheet(u"border:none;\n"
"border-radius:12px;\n"
"background-color: rgba(0, 0, 0, 0.7);")
        self.AdjustTopMenu.setFrameShape(QFrame.StyledPanel)
        self.AdjustTopMenu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.AdjustTopMenu)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.AdjustementBtn = QPushButton(self.AdjustTopMenu)
        self.AdjustementBtn.setObjectName(u"AdjustementBtn")
        self.AdjustementBtn.setEnabled(True)
        self.AdjustementBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.AdjustementBtn.setStyleSheet(u"QPushButton{\n"
"color: rgba(255, 255, 255, 0.6);\n"
"border-radius:12px;\n"
"background-color:rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"D:/designs-web/b2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AdjustementBtn.setIcon(icon7)
        self.AdjustementBtn.setIconSize(QSize(44, 50))
        self.AdjustementBtn.setCheckable(False)
        self.AdjustementBtn.setAutoDefault(False)
        self.AdjustementBtn.setFlat(True)

        self.horizontalLayout.addWidget(self.AdjustementBtn)

        self.ApplyFiltersBtn = QPushButton(self.AdjustTopMenu)
        self.ApplyFiltersBtn.setObjectName(u"ApplyFiltersBtn")
        self.ApplyFiltersBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ApplyFiltersBtn.setStyleSheet(u"QPushButton{\n"
"color: rgba(255, 255, 255, 0.6);\n"
"border-radius:12px;\n"
"background-color:rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"D:/designs-web/ce18e535675c436e1bc2ed4663ebbdea.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ApplyFiltersBtn.setIcon(icon8)
        self.ApplyFiltersBtn.setIconSize(QSize(26, 50))
        self.ApplyFiltersBtn.setCheckable(False)
        self.ApplyFiltersBtn.setAutoDefault(False)
        self.ApplyFiltersBtn.setFlat(True)

        self.horizontalLayout.addWidget(self.ApplyFiltersBtn)

        self.LightAndColorsBtn = QPushButton(self.AdjustTopMenu)
        self.LightAndColorsBtn.setObjectName(u"LightAndColorsBtn")
        self.LightAndColorsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.LightAndColorsBtn.setStyleSheet(u"QPushButton{\n"
"color: rgba(255, 255, 255, 0.6);\n"
"border-radius:12px;\n"
"background-color:rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"D:/designs-web/36.png", QSize(), QIcon.Normal, QIcon.Off)
        self.LightAndColorsBtn.setIcon(icon9)
        self.LightAndColorsBtn.setIconSize(QSize(32, 50))
        self.LightAndColorsBtn.setCheckable(False)
        self.LightAndColorsBtn.setAutoDefault(False)
        self.LightAndColorsBtn.setFlat(True)

        self.horizontalLayout.addWidget(self.LightAndColorsBtn)

        self.ResetChangesBtn = QPushButton(self.AdjustTopMenu)
        self.ResetChangesBtn.setObjectName(u"ResetChangesBtn")
        self.ResetChangesBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ResetChangesBtn.setStyleSheet(u"QPushButton{\n"
"color: rgba(255, 255, 255, 0.6);\n"
"border-radius:12px;\n"
"background-color:rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"D:/Programmation/DEV WEB/web dev mine/learn html css js only/images/icons desktop/icons8-xcode-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ResetChangesBtn.setIcon(icon10)
        self.ResetChangesBtn.setIconSize(QSize(31, 50))
        self.ResetChangesBtn.setCheckable(False)
        self.ResetChangesBtn.setAutoDefault(False)
        self.ResetChangesBtn.setFlat(True)

        self.horizontalLayout.addWidget(self.ResetChangesBtn)

        self.LightAndColorsScrollArea = QScrollArea(self.centralwidget)
        self.LightAndColorsScrollArea.setObjectName(u"LightAndColorsScrollArea")
        self.LightAndColorsScrollArea.setEnabled(True)
        self.LightAndColorsScrollArea.setGeometry(QRect(940, 20, 261, 591))
        self.LightAndColorsScrollArea.setStyleSheet(u"background-color:rgba(0, 0, 0,0.4);\n"
"border:none;\n"
"border-radius:12px;")
        self.LightAndColorsScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.LightAndColorsScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.LightAndColorsScrollArea.setWidgetResizable(True)
        self.lightColorScrollAreaWidgetContents = QWidget()
        self.lightColorScrollAreaWidgetContents.setObjectName(u"lightColorScrollAreaWidgetContents")
        self.lightColorScrollAreaWidgetContents.setGeometry(QRect(0, 0, 257, 864))
        self.verticalLayout_4 = QVBoxLayout(self.lightColorScrollAreaWidgetContents)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.labelLight = QLabel(self.lightColorScrollAreaWidgetContents)
        self.labelLight.setObjectName(u"labelLight")
        self.labelLight.setStyleSheet(u"background-color:rgba(1, 230, 255, 40);")

        self.verticalLayout_4.addWidget(self.labelLight)

        self.BrightnessBtn = QPushButton(self.lightColorScrollAreaWidgetContents)
        self.BrightnessBtn.setObjectName(u"BrightnessBtn")
        self.BrightnessBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.BrightnessBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(1, 234, 255);\n"
"background-color:rgba(0, 179, 255, 50)\n"
"}")

        self.verticalLayout_4.addWidget(self.BrightnessBtn)

        self.ContrastBtn = QPushButton(self.lightColorScrollAreaWidgetContents)
        self.ContrastBtn.setObjectName(u"ContrastBtn")
        self.ContrastBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ContrastBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(1, 234, 255);\n"
"background-color:rgba(0, 179, 255, 50)\n"
"}")

        self.verticalLayout_4.addWidget(self.ContrastBtn)

        self.HighlightsBtn = QPushButton(self.lightColorScrollAreaWidgetContents)
        self.HighlightsBtn.setObjectName(u"HighlightsBtn")
        self.HighlightsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.HighlightsBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(1, 234, 255);\n"
"background-color:rgba(0, 179, 255, 50)\n"
"}")

        self.verticalLayout_4.addWidget(self.HighlightsBtn)

        self.ShadowsBtn = QPushButton(self.lightColorScrollAreaWidgetContents)
        self.ShadowsBtn.setObjectName(u"ShadowsBtn")
        self.ShadowsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ShadowsBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(1, 234, 255);\n"
"background-color:rgba(0, 179, 255, 50)\n"
"}")

        self.verticalLayout_4.addWidget(self.ShadowsBtn)

        self.labelColour = QLabel(self.lightColorScrollAreaWidgetContents)
        self.labelColour.setObjectName(u"labelColour")
        self.labelColour.setStyleSheet(u"background-color:rgba(1, 230, 255, 40);")

        self.verticalLayout_4.addWidget(self.labelColour)

        self.InvertBtn = QPushButton(self.lightColorScrollAreaWidgetContents)
        self.InvertBtn.setObjectName(u"InvertBtn")
        self.InvertBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(1, 234, 255);\n"
"background-color:rgba(0, 179, 255, 50)\n"
"}")

        self.verticalLayout_4.addWidget(self.InvertBtn)

        self.SaturationBtn = QPushButton(self.lightColorScrollAreaWidgetContents)
        self.SaturationBtn.setObjectName(u"SaturationBtn")
        self.SaturationBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(1, 234, 255);\n"
"background-color:rgba(0, 179, 255, 50)\n"
"}")

        self.verticalLayout_4.addWidget(self.SaturationBtn)

        self.WarmthBtn = QPushButton(self.lightColorScrollAreaWidgetContents)
        self.WarmthBtn.setObjectName(u"WarmthBtn")
        self.WarmthBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(1, 234, 255);\n"
"background-color:rgba(0, 179, 255, 50)\n"
"}")

        self.verticalLayout_4.addWidget(self.WarmthBtn)

        self.TintBtn = QPushButton(self.lightColorScrollAreaWidgetContents)
        self.TintBtn.setObjectName(u"TintBtn")
        self.TintBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(1, 234, 255);\n"
"background-color:rgba(0, 179, 255, 50)\n"
"}")

        self.verticalLayout_4.addWidget(self.TintBtn)

        self.GrayScaleBtn = QPushButton(self.lightColorScrollAreaWidgetContents)
        self.GrayScaleBtn.setObjectName(u"GrayScaleBtn")
        self.GrayScaleBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(1, 234, 255);\n"
"background-color:rgba(0, 179, 255, 50)\n"
"}")

        self.verticalLayout_4.addWidget(self.GrayScaleBtn)

        self.labelHisto = QLabel(self.lightColorScrollAreaWidgetContents)
        self.labelHisto.setObjectName(u"labelHisto")
        self.labelHisto.setStyleSheet(u"background-color:rgba(1, 230, 255, 40);")

        self.verticalLayout_4.addWidget(self.labelHisto)

        self.HistBtn = QPushButton(self.lightColorScrollAreaWidgetContents)
        self.HistBtn.setObjectName(u"HistBtn")
        self.HistBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(0, 255, 183);\n"
"background-color:rgba(0, 255, 217, 40)\n"
"}")
        self.HistBtn.setAutoDefault(False)

        self.verticalLayout_4.addWidget(self.HistBtn)

        self.HistEqualizerBtn = QPushButton(self.lightColorScrollAreaWidgetContents)
        self.HistEqualizerBtn.setObjectName(u"HistEqualizerBtn")
        self.HistEqualizerBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(0, 255, 183);\n"
"background-color:rgba(0, 255, 217, 40)\n"
"}")

        self.verticalLayout_4.addWidget(self.HistEqualizerBtn)

        self.HistStretchBtn = QPushButton(self.lightColorScrollAreaWidgetContents)
        self.HistStretchBtn.setObjectName(u"HistStretchBtn")
        self.HistStretchBtn.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(0, 255, 183);\n"
"background-color:rgba(0, 255, 217, 40)\n"
"}")

        self.verticalLayout_4.addWidget(self.HistStretchBtn)

        self.LightAndColorsScrollArea.setWidget(self.lightColorScrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.Image_copy.raise_()
        self.SettingsSideBar.raise_()
        self.Image.raise_()
        self.FiltersBtn.raise_()
        self.AdjustArea.raise_()
        self.AdjustMenu.raise_()
        self.AdjustTopMenu.raise_()
        self.LightAndColorsScrollArea.raise_()
        self.FiltersScrollArea.raise_()

        self.retranslateUi(MainWindow)

        self.OpenImageBtn.setDefault(False)
        self.RotateBtn.setDefault(False)
        self.ZoomInBtn.setDefault(False)
        self.ZoomOutBtn.setDefault(False)
        self.FlipBtn.setDefault(False)
        self.CropBtn.setDefault(False)
        self.ViewSwitchedBtn.setDefault(False)
        self.AdjustementBtn.setDefault(False)
        self.ApplyFiltersBtn.setDefault(False)
        self.LightAndColorsBtn.setDefault(False)
        self.ResetChangesBtn.setDefault(False)


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
        self.EditImageBtn.setText(QCoreApplication.translate("MainWindow", u"Edit Image", None))
        self.Image.setText("")
        self.FiltersBtn.setText(QCoreApplication.translate("MainWindow", u"No Filters", None))
        self.NoEffectsBtn.setText(QCoreApplication.translate("MainWindow", u"No Effects", None))
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
        self.PrewittBtn.setText(QCoreApplication.translate("MainWindow", u"Prewitt", None))
        self.CannyBtn.setText(QCoreApplication.translate("MainWindow", u"Canny", None))
        self.KirschBtn.setText(QCoreApplication.translate("MainWindow", u"Kirsch", None))
        self.RobinsonBtn.setText(QCoreApplication.translate("MainWindow", u"Robinson", None))
        self.LaplacianBtn.setText(QCoreApplication.translate("MainWindow", u"Laplacian", None))
        self.SiftBtn.setText(QCoreApplication.translate("MainWindow", u"Sift", None))
        self.HarrisBtn.setText(QCoreApplication.translate("MainWindow", u"Harris", None))
        self.HoughBtn.setText(QCoreApplication.translate("MainWindow", u"hough", None))
        self.labelColour_7.setText(QCoreApplication.translate("MainWindow", u"Segmentation", None))
        self.RegionGrowingBtn.setText(QCoreApplication.translate("MainWindow", u"region growing", None))
        self.Image_copy.setText("")
        self.RotateBtn.setText("")
        self.ZoomInBtn.setText("")
        self.ZoomOutBtn.setText("")
        self.FlipBtn.setText("")
        self.CropBtn.setText("")
        self.ViewSwitchedBtn.setText("")
        self.AdjustementBtn.setText(QCoreApplication.translate("MainWindow", u"Adjustement", None))
        self.ApplyFiltersBtn.setText(QCoreApplication.translate("MainWindow", u"    Apply Filters", None))
        self.LightAndColorsBtn.setText(QCoreApplication.translate("MainWindow", u"  Light / Colors", None))
        self.ResetChangesBtn.setText(QCoreApplication.translate("MainWindow", u" Reset Changes ", None))
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
        self.labelHisto.setText(QCoreApplication.translate("MainWindow", u"Histogram", None))
        self.HistBtn.setText(QCoreApplication.translate("MainWindow", u"Histogram", None))
        self.HistEqualizerBtn.setText(QCoreApplication.translate("MainWindow", u"Equalizer", None))
        self.HistStretchBtn.setText(QCoreApplication.translate("MainWindow", u"Stretch", None))
    # retranslateUi

