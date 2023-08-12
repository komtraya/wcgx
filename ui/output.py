# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainR1.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QStatusBar,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)
import Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1622, 1205)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 200))
        MainWindow.setBaseSize(QSize(1599, 1180))
        icon = QIcon()
        icon.addFile(u":/Icon/WCGXicon2.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.actionShit = QAction(MainWindow)
        self.actionShit.setObjectName(u"actionShit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.FRAME_X = QFrame(self.centralwidget)
        self.FRAME_X.setObjectName(u"FRAME_X")
        self.FRAME_X.setMinimumSize(QSize(1561, 1049))
        self.verticalLayout_25 = QVBoxLayout(self.FRAME_X)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.TitleContainer = QFrame(self.FRAME_X)
        self.TitleContainer.setObjectName(u"TitleContainer")
        self.TitleContainer.setMinimumSize(QSize(787, 76))
        self.TitleContainer.setFrameShape(QFrame.StyledPanel)
        self.TitleContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.TitleContainer)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.app_title = QLabel(self.TitleContainer)
        self.app_title.setObjectName(u"app_title")
        self.app_title.setMinimumSize(QSize(0, 76))
        self.app_title.setMaximumSize(QSize(768, 100))
        font = QFont()
        font.setFamilies([u"Stick"])
        font.setPointSize(40)
        font.setBold(True)
        font.setUnderline(False)
        font.setKerning(False)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.app_title.setFont(font)

        self.horizontalLayout_24.addWidget(self.app_title)


        self.verticalLayout_25.addWidget(self.TitleContainer)

        self.frame_main1 = QFrame(self.FRAME_X)
        self.frame_main1.setObjectName(u"frame_main1")
        self.horizontalLayout_23 = QHBoxLayout(self.frame_main1)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.pathsAndparameters = QHBoxLayout()
        self.pathsAndparameters.setObjectName(u"pathsAndparameters")
        self.frame_11 = QFrame(self.frame_main1)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 630))
        self.frame_11.setMaximumSize(QSize(855, 630))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_11)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.All_ResourcePaths_Frame = QFrame(self.frame_11)
        self.All_ResourcePaths_Frame.setObjectName(u"All_ResourcePaths_Frame")
        self.verticalLayout_27 = QVBoxLayout(self.All_ResourcePaths_Frame)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.resource_paths_frame = QFrame(self.All_ResourcePaths_Frame)
        self.resource_paths_frame.setObjectName(u"resource_paths_frame")
        self.resource_paths_frame.setMinimumSize(QSize(820, 98))
        self.resource_paths_frame.setFrameShape(QFrame.StyledPanel)
        self.resource_paths_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.resource_paths_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.resource_paths_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(150, 0))
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.mask_select_button = QPushButton(self.frame)
        self.mask_select_button.setObjectName(u"mask_select_button")
        self.mask_select_button.setMinimumSize(QSize(150, 50))
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.mask_select_button.setFont(font1)
        self.mask_select_button.setStyleSheet(u"background-color: #7754c8;\n"
"color:#3cf3b6;\n"
"border-radius:10px;\n"
"border:2px solid red; ")

        self.verticalLayout_4.addWidget(self.mask_select_button)


        self.horizontalLayout.addWidget(self.frame)

        self.select_destination_button = QPushButton(self.resource_paths_frame)
        self.select_destination_button.setObjectName(u"select_destination_button")
        self.select_destination_button.setEnabled(True)
        self.select_destination_button.setMinimumSize(QSize(150, 50))
        self.select_destination_button.setFont(font1)
        self.select_destination_button.setStyleSheet(u"background-color: #7754c8;\n"
"color:#3cf3b6;\n"
"border-radius:10px;\n"
"border:2px solid red; ")

        self.horizontalLayout.addWidget(self.select_destination_button)

        self.open_destination_folder = QPushButton(self.resource_paths_frame)
        self.open_destination_folder.setObjectName(u"open_destination_folder")
        self.open_destination_folder.setMinimumSize(QSize(0, 0))
        self.open_destination_folder.setMaximumSize(QSize(40, 50))
        font2 = QFont()
        font2.setPointSize(14)
        self.open_destination_folder.setFont(font2)
        self.open_destination_folder.setStyleSheet(u"color: rgb(0, 170, 0);\n"
"background-color: #7754c8;\n"
"border-radius:5px;")

        self.horizontalLayout.addWidget(self.open_destination_folder, 0, Qt.AlignVCenter)


        self.verticalLayout_27.addWidget(self.resource_paths_frame)


        self.verticalLayout_7.addWidget(self.All_ResourcePaths_Frame)

        self.frame_2 = QFrame(self.frame_11)
        self.frame_2.setObjectName(u"frame_2")
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Parameters_Title_label = QLabel(self.frame_2)
        self.Parameters_Title_label.setObjectName(u"Parameters_Title_label")
        self.Parameters_Title_label.setMaximumSize(QSize(400, 50))
        font3 = QFont()
        font3.setFamilies([u"IBM Plex Sans SemiBold"])
        font3.setPointSize(25)
        font3.setBold(True)
        self.Parameters_Title_label.setFont(font3)

        self.verticalLayout_2.addWidget(self.Parameters_Title_label, 0, Qt.AlignHCenter)

        self.Parameters_Main_Frame = QFrame(self.frame_2)
        self.Parameters_Main_Frame.setObjectName(u"Parameters_Main_Frame")
        self.Parameters_Main_Frame.setMaximumSize(QSize(900, 500))
        self.Parameters_Main_Frame.setFrameShape(QFrame.StyledPanel)
        self.Parameters_Main_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.Parameters_Main_Frame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.Parameters_Main = QHBoxLayout()
        self.Parameters_Main.setObjectName(u"Parameters_Main")
        self.parameters_list = QListWidget(self.Parameters_Main_Frame)
        QListWidgetItem(self.parameters_list)
        QListWidgetItem(self.parameters_list)
        QListWidgetItem(self.parameters_list)
        QListWidgetItem(self.parameters_list)
        __qlistwidgetitem = QListWidgetItem(self.parameters_list)
        __qlistwidgetitem.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable);
        __qlistwidgetitem1 = QListWidgetItem(self.parameters_list)
        __qlistwidgetitem1.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable);
        __qlistwidgetitem2 = QListWidgetItem(self.parameters_list)
        __qlistwidgetitem2.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable);
        __qlistwidgetitem3 = QListWidgetItem(self.parameters_list)
        __qlistwidgetitem3.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable);
        QListWidgetItem(self.parameters_list)
        __qlistwidgetitem4 = QListWidgetItem(self.parameters_list)
        __qlistwidgetitem4.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable);
        __qlistwidgetitem5 = QListWidgetItem(self.parameters_list)
        __qlistwidgetitem5.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable);
        QListWidgetItem(self.parameters_list)
        QListWidgetItem(self.parameters_list)
        font4 = QFont()
        font4.setStrikeOut(False)
        __qlistwidgetitem6 = QListWidgetItem(self.parameters_list)
        __qlistwidgetitem6.setFont(font4);
        __qlistwidgetitem6.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable);
        QListWidgetItem(self.parameters_list)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.NoBrush)
        __qlistwidgetitem7 = QListWidgetItem(self.parameters_list)
        __qlistwidgetitem7.setForeground(brush);
        self.parameters_list.setObjectName(u"parameters_list")
        self.parameters_list.setMinimumSize(QSize(221, 391))
        self.parameters_list.setMaximumSize(QSize(221, 391))
        font5 = QFont()
        font5.setFamilies([u"IBM Plex Sans"])
        font5.setPointSize(11)
        font5.setBold(True)
        self.parameters_list.setFont(font5)
        self.parameters_list.setAcceptDrops(False)
        self.parameters_list.setFrameShadow(QFrame.Plain)
        self.parameters_list.setLineWidth(1)
        self.parameters_list.setAutoScrollMargin(20)
        self.parameters_list.setViewMode(QListView.ListMode)
        self.parameters_list.setSortingEnabled(False)

        self.Parameters_Main.addWidget(self.parameters_list)

        self.parameters_window = QTabWidget(self.Parameters_Main_Frame)
        self.parameters_window.setObjectName(u"parameters_window")
        self.parameters_window.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.parameters_window.sizePolicy().hasHeightForWidth())
        self.parameters_window.setSizePolicy(sizePolicy1)
        self.parameters_window.setMinimumSize(QSize(341, 231))
        self.parameters_window.setMaximumSize(QSize(600, 500))
        font6 = QFont()
        font6.setPointSize(8)
        font6.setKerning(True)
        self.parameters_window.setFont(font6)
        self.parameters_window.setTabPosition(QTabWidget.North)
        self.parameters_window.setTabShape(QTabWidget.Rounded)
        self.parameters_window.setIconSize(QSize(24, 24))
        self.parameters_windowPage1 = QWidget()
        self.parameters_windowPage1.setObjectName(u"parameters_windowPage1")
        self.verticalLayout_16 = QVBoxLayout(self.parameters_windowPage1)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_3 = QFrame(self.parameters_windowPage1)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font7 = QFont()
        font7.setFamilies([u"IBM Plex Sans"])
        font7.setPointSize(11)
        font7.setBold(True)
        font7.setKerning(True)
        self.label.setFont(font7)

        self.verticalLayout_6.addWidget(self.label, 0, Qt.AlignHCenter)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_14)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.repeat_words_label = QLabel(self.frame_3)
        self.repeat_words_label.setObjectName(u"repeat_words_label")
        self.repeat_words_label.setMaximumSize(QSize(150, 16777215))
        font8 = QFont()
        font8.setFamilies([u"Play"])
        font8.setPointSize(14)
        font8.setBold(True)
        font8.setKerning(True)
        self.repeat_words_label.setFont(font8)

        self.horizontalLayout_5.addWidget(self.repeat_words_label)

        self.repeat_checkbox = QRadioButton(self.frame_3)
        self.repeat_checkbox.setObjectName(u"repeat_checkbox")
        self.repeat_checkbox.setMinimumSize(QSize(50, 0))
        self.repeat_checkbox.setMaximumSize(QSize(50, 20))
        self.repeat_checkbox.setSizeIncrement(QSize(0, 0))
        self.repeat_checkbox.setBaseSize(QSize(0, 0))
        font9 = QFont()
        font9.setFamilies([u"Segoe UI"])
        font9.setPointSize(10)
        font9.setBold(True)
        font9.setKerning(True)
        self.repeat_checkbox.setFont(font9)
        self.repeat_checkbox.setIconSize(QSize(24, 24))
        self.repeat_checkbox.setCheckable(True)
        self.repeat_checkbox.setChecked(True)
        self.repeat_checkbox.setAutoRepeat(False)

        self.horizontalLayout_5.addWidget(self.repeat_checkbox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_13)


        self.verticalLayout_16.addWidget(self.frame_3, 0, Qt.AlignHCenter)

        self.parameters_window.addTab(self.parameters_windowPage1, "")
        self.parameters_windowPage2 = QWidget()
        self.parameters_windowPage2.setObjectName(u"parameters_windowPage2")
        self.verticalLayout_5 = QVBoxLayout(self.parameters_windowPage2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_4 = QFrame(self.parameters_windowPage2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font7)

        self.verticalLayout_8.addWidget(self.label_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.min_font_size_label = QLabel(self.frame_4)
        self.min_font_size_label.setObjectName(u"min_font_size_label")
        self.min_font_size_label.setMaximumSize(QSize(150, 100))
        self.min_font_size_label.setFont(font8)

        self.horizontalLayout_6.addWidget(self.min_font_size_label)

        self.min_font_size_slider = QSlider(self.frame_4)
        self.min_font_size_slider.setObjectName(u"min_font_size_slider")
        self.min_font_size_slider.setEnabled(True)
        self.min_font_size_slider.setMinimumSize(QSize(30, 0))
        self.min_font_size_slider.setMaximumSize(QSize(30, 16777215))
        self.min_font_size_slider.setSizeIncrement(QSize(10, 0))
        font10 = QFont()
        font10.setFamilies([u"Segoe UI"])
        font10.setPointSize(8)
        font10.setBold(False)
        font10.setKerning(True)
        self.min_font_size_slider.setFont(font10)
        self.min_font_size_slider.setMouseTracking(False)
        self.min_font_size_slider.setFocusPolicy(Qt.ClickFocus)
        self.min_font_size_slider.setMinimum(1)
        self.min_font_size_slider.setMaximum(100)
        self.min_font_size_slider.setPageStep(1)
        self.min_font_size_slider.setValue(10)
        self.min_font_size_slider.setOrientation(Qt.Vertical)

        self.horizontalLayout_6.addWidget(self.min_font_size_slider)

        self.label_min_font_size_slider = QLabel(self.frame_4)
        self.label_min_font_size_slider.setObjectName(u"label_min_font_size_slider")
        self.label_min_font_size_slider.setMinimumSize(QSize(50, 0))
        self.label_min_font_size_slider.setMaximumSize(QSize(50, 50))
        font11 = QFont()
        font11.setFamilies([u"Montserrat"])
        font11.setPointSize(14)
        font11.setBold(True)
        font11.setKerning(True)
        self.label_min_font_size_slider.setFont(font11)

        self.horizontalLayout_6.addWidget(self.label_min_font_size_slider)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.max_font_size_label = QLabel(self.frame_4)
        self.max_font_size_label.setObjectName(u"max_font_size_label")
        self.max_font_size_label.setMaximumSize(QSize(150, 100))
        self.max_font_size_label.setFont(font8)

        self.horizontalLayout_7.addWidget(self.max_font_size_label)

        self.max_font_size_slider = QSlider(self.frame_4)
        self.max_font_size_slider.setObjectName(u"max_font_size_slider")
        self.max_font_size_slider.setEnabled(True)
        self.max_font_size_slider.setMinimumSize(QSize(30, 0))
        self.max_font_size_slider.setMaximumSize(QSize(30, 16777215))
        self.max_font_size_slider.setSizeIncrement(QSize(10, 0))
        self.max_font_size_slider.setFont(font10)
        self.max_font_size_slider.setMouseTracking(False)
        self.max_font_size_slider.setFocusPolicy(Qt.ClickFocus)
        self.max_font_size_slider.setMinimum(5)
        self.max_font_size_slider.setMaximum(500)
        self.max_font_size_slider.setPageStep(1)
        self.max_font_size_slider.setValue(100)
        self.max_font_size_slider.setOrientation(Qt.Vertical)

        self.horizontalLayout_7.addWidget(self.max_font_size_slider)

        self.label_max_font_size_slider = QLabel(self.frame_4)
        self.label_max_font_size_slider.setObjectName(u"label_max_font_size_slider")
        self.label_max_font_size_slider.setMinimumSize(QSize(50, 0))
        self.label_max_font_size_slider.setMaximumSize(QSize(50, 50))
        self.label_max_font_size_slider.setFont(font11)

        self.horizontalLayout_7.addWidget(self.label_max_font_size_slider)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)


        self.verticalLayout_5.addWidget(self.frame_4, 0, Qt.AlignHCenter)

        self.parameters_window.addTab(self.parameters_windowPage2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_28 = QVBoxLayout(self.tab)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_font_step = QFrame(self.tab)
        self.frame_font_step.setObjectName(u"frame_font_step")
        self.gridLayout = QGridLayout(self.frame_font_step)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_10 = QLabel(self.frame_font_step)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font7)

        self.gridLayout.addWidget(self.label_10, 0, 1, 1, 1)

        self.frame1 = QFrame(self.frame_font_step)
        self.frame1.setObjectName(u"frame1")
        self.horizontalLayout_4 = QHBoxLayout(self.frame1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_11)

        self.fontstep_label = QLabel(self.frame1)
        self.fontstep_label.setObjectName(u"fontstep_label")
        self.fontstep_label.setMaximumSize(QSize(16777215, 50))
        self.fontstep_label.setFont(font8)

        self.horizontalLayout_4.addWidget(self.fontstep_label)

        self.font_step_slider = QSlider(self.frame1)
        self.font_step_slider.setObjectName(u"font_step_slider")
        self.font_step_slider.setMinimumSize(QSize(30, 150))
        self.font_step_slider.setMaximumSize(QSize(30, 150))
        self.font_step_slider.setMinimum(1)
        self.font_step_slider.setMaximum(100)
        self.font_step_slider.setSingleStep(10)
        self.font_step_slider.setPageStep(10)
        self.font_step_slider.setValue(1)
        self.font_step_slider.setOrientation(Qt.Vertical)

        self.horizontalLayout_4.addWidget(self.font_step_slider, 0, Qt.AlignHCenter)

        self.font_step_indicator_label = QLabel(self.frame1)
        self.font_step_indicator_label.setObjectName(u"font_step_indicator_label")
        self.font_step_indicator_label.setMinimumSize(QSize(50, 0))
        self.font_step_indicator_label.setMaximumSize(QSize(50, 50))
        self.font_step_indicator_label.setFont(font11)

        self.horizontalLayout_4.addWidget(self.font_step_indicator_label, 0, Qt.AlignHCenter)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_16)


        self.gridLayout.addWidget(self.frame1, 1, 1, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_17, 0, 2, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_18, 0, 0, 1, 1)


        self.verticalLayout_28.addWidget(self.frame_font_step)

        self.parameters_window.addTab(self.tab, "")
        self.parameters_windowPage3 = QWidget()
        self.parameters_windowPage3.setObjectName(u"parameters_windowPage3")
        self.verticalLayout_9 = QVBoxLayout(self.parameters_windowPage3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_3 = QLabel(self.parameters_windowPage3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(305, 95))
        self.label_3.setFont(font7)

        self.verticalLayout_9.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.margin_label_2 = QLabel(self.parameters_windowPage3)
        self.margin_label_2.setObjectName(u"margin_label_2")
        self.margin_label_2.setMaximumSize(QSize(250, 100))
        self.margin_label_2.setFont(font8)
        self.margin_label_2.setWordWrap(False)
        self.margin_label_2.setMargin(0)

        self.horizontalLayout_8.addWidget(self.margin_label_2)

        self.margin_slider = QSlider(self.parameters_windowPage3)
        self.margin_slider.setObjectName(u"margin_slider")
        self.margin_slider.setEnabled(True)
        self.margin_slider.setMinimumSize(QSize(30, 0))
        self.margin_slider.setMaximumSize(QSize(30, 16777215))
        self.margin_slider.setSizeIncrement(QSize(10, 0))
        self.margin_slider.setFont(font10)
        self.margin_slider.setMouseTracking(False)
        self.margin_slider.setFocusPolicy(Qt.ClickFocus)
        self.margin_slider.setMinimum(0)
        self.margin_slider.setMaximum(50)
        self.margin_slider.setPageStep(1)
        self.margin_slider.setValue(5)
        self.margin_slider.setOrientation(Qt.Vertical)

        self.horizontalLayout_8.addWidget(self.margin_slider)

        self.label_margin_slider = QLabel(self.parameters_windowPage3)
        self.label_margin_slider.setObjectName(u"label_margin_slider")
        self.label_margin_slider.setMinimumSize(QSize(50, 0))
        self.label_margin_slider.setMaximumSize(QSize(50, 50))
        self.label_margin_slider.setFont(font11)
        self.label_margin_slider.setMargin(0)

        self.horizontalLayout_8.addWidget(self.label_margin_slider)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)

        self.parameters_window.addTab(self.parameters_windowPage3, "")
        self.parameters_windowPage4 = QWidget()
        self.parameters_windowPage4.setObjectName(u"parameters_windowPage4")
        self.verticalLayout_10 = QVBoxLayout(self.parameters_windowPage4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_5 = QFrame(self.parameters_windowPage4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font7)

        self.verticalLayout_11.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_12)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)

        self.prefer_horizontal_label = QLabel(self.frame_5)
        self.prefer_horizontal_label.setObjectName(u"prefer_horizontal_label")
        self.prefer_horizontal_label.setMaximumSize(QSize(250, 100))
        self.prefer_horizontal_label.setFont(font8)

        self.horizontalLayout_9.addWidget(self.prefer_horizontal_label)

        self.prefer_horizontal_slider = QSlider(self.frame_5)
        self.prefer_horizontal_slider.setObjectName(u"prefer_horizontal_slider")
        self.prefer_horizontal_slider.setEnabled(True)
        self.prefer_horizontal_slider.setMinimumSize(QSize(30, 0))
        self.prefer_horizontal_slider.setMaximumSize(QSize(30, 16777215))
        self.prefer_horizontal_slider.setSizeIncrement(QSize(10, 0))
        self.prefer_horizontal_slider.setFocusPolicy(Qt.ClickFocus)
        self.prefer_horizontal_slider.setAutoFillBackground(False)
        self.prefer_horizontal_slider.setStyleSheet(u"")
        self.prefer_horizontal_slider.setMaximum(10)
        self.prefer_horizontal_slider.setPageStep(1)
        self.prefer_horizontal_slider.setValue(9)
        self.prefer_horizontal_slider.setOrientation(Qt.Vertical)

        self.horizontalLayout_9.addWidget(self.prefer_horizontal_slider)

        self.label_text_orientation_slider = QLabel(self.frame_5)
        self.label_text_orientation_slider.setObjectName(u"label_text_orientation_slider")
        self.label_text_orientation_slider.setMinimumSize(QSize(50, 0))
        self.label_text_orientation_slider.setMaximumSize(QSize(50, 50))
        self.label_text_orientation_slider.setFont(font11)

        self.horizontalLayout_9.addWidget(self.label_text_orientation_slider)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_10)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_11)


        self.verticalLayout_10.addWidget(self.frame_5)

        self.parameters_window.addTab(self.parameters_windowPage4, "")
        self.parameters_windowPage5 = QWidget()
        self.parameters_windowPage5.setObjectName(u"parameters_windowPage5")
        self.verticalLayout_12 = QVBoxLayout(self.parameters_windowPage5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_6 = QFrame(self.parameters_windowPage5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)

        self.image_scale_label = QLabel(self.frame_6)
        self.image_scale_label.setObjectName(u"image_scale_label")
        self.image_scale_label.setMaximumSize(QSize(16777215, 30))
        self.image_scale_label.setFont(font8)

        self.horizontalLayout_10.addWidget(self.image_scale_label)

        self.scale_slider = QSlider(self.frame_6)
        self.scale_slider.setObjectName(u"scale_slider")
        self.scale_slider.setMinimumSize(QSize(0, 40))
        self.scale_slider.setMaximumSize(QSize(300, 16777215))
        self.scale_slider.setMinimum(1)
        self.scale_slider.setMaximum(10)
        self.scale_slider.setPageStep(1)
        self.scale_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_10.addWidget(self.scale_slider)

        self.label_scale_slider = QLabel(self.frame_6)
        self.label_scale_slider.setObjectName(u"label_scale_slider")
        self.label_scale_slider.setMaximumSize(QSize(50, 50))
        self.label_scale_slider.setFont(font11)
        self.label_scale_slider.setMargin(5)
        self.label_scale_slider.setIndent(-1)
        self.label_scale_slider.setOpenExternalLinks(False)

        self.horizontalLayout_10.addWidget(self.label_scale_slider)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)


        self.gridLayout_4.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 3, 0, 1, 1)

        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font7)

        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_6, 1, 0, 1, 1)


        self.verticalLayout_12.addWidget(self.frame_6)

        self.parameters_window.addTab(self.parameters_windowPage5, "")
        self.parameters_windowPage6 = QWidget()
        self.parameters_windowPage6.setObjectName(u"parameters_windowPage6")
        self.verticalLayout_13 = QVBoxLayout(self.parameters_windowPage6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_7 = QFrame(self.parameters_windowPage6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_7)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font7)

        self.gridLayout_6.addWidget(self.label_7, 0, 0, 1, 1)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.horizontalLayout_13 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_14)

        self.stopwords_label = QLabel(self.frame_8)
        self.stopwords_label.setObjectName(u"stopwords_label")
        self.stopwords_label.setMaximumSize(QSize(150, 30))
        self.stopwords_label.setFont(font8)

        self.horizontalLayout_13.addWidget(self.stopwords_label)

        self.stopwords_checkbox = QRadioButton(self.frame_8)
        self.stopwords_checkbox.setObjectName(u"stopwords_checkbox")
        self.stopwords_checkbox.setMinimumSize(QSize(50, 0))
        self.stopwords_checkbox.setMaximumSize(QSize(50, 20))
        font12 = QFont()
        font12.setPointSize(10)
        font12.setBold(True)
        font12.setKerning(True)
        self.stopwords_checkbox.setFont(font12)
        self.stopwords_checkbox.setIconSize(QSize(24, 24))
        self.stopwords_checkbox.setCheckable(True)
        self.stopwords_checkbox.setChecked(False)

        self.horizontalLayout_13.addWidget(self.stopwords_checkbox)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_15)


        self.gridLayout_6.addWidget(self.frame_8, 2, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_9, 3, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_10, 1, 0, 1, 1)


        self.verticalLayout_13.addWidget(self.frame_7)

        self.parameters_window.addTab(self.parameters_windowPage6, "")
        self.parameters_windowPage7 = QWidget()
        self.parameters_windowPage7.setObjectName(u"parameters_windowPage7")
        self.verticalLayout_15 = QVBoxLayout(self.parameters_windowPage7)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_9 = QFrame(self.parameters_windowPage7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_9)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font7)

        self.verticalLayout_14.addWidget(self.label_8)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_5)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.horizontalLayout_18 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_8)

        self.label_collocations = QLabel(self.frame_10)
        self.label_collocations.setObjectName(u"label_collocations")
        self.label_collocations.setFont(font8)

        self.horizontalLayout_18.addWidget(self.label_collocations)

        self.collocations_checkbox = QCheckBox(self.frame_10)
        self.collocations_checkbox.setObjectName(u"collocations_checkbox")
        self.collocations_checkbox.setFont(font8)
        self.collocations_checkbox.setChecked(True)
        self.collocations_checkbox.setTristate(False)

        self.horizontalLayout_18.addWidget(self.collocations_checkbox)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_7)


        self.verticalLayout_14.addWidget(self.frame_10)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_4)


        self.verticalLayout_15.addWidget(self.frame_9)

        self.parameters_window.addTab(self.parameters_windowPage7, "")
        self.parameters_windowPage8 = QWidget()
        self.parameters_windowPage8.setObjectName(u"parameters_windowPage8")
        self.verticalLayout_17 = QVBoxLayout(self.parameters_windowPage8)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_12 = QFrame(self.parameters_windowPage8)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_12)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_8, 3, 0, 1, 1)

        self.label_9 = QLabel(self.frame_12)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font7)

        self.gridLayout_5.addWidget(self.label_9, 0, 0, 1, 1)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_12)

        self.label_collocations_thresh = QLabel(self.frame_12)
        self.label_collocations_thresh.setObjectName(u"label_collocations_thresh")
        self.label_collocations_thresh.setFont(font8)

        self.horizontalLayout_20.addWidget(self.label_collocations_thresh)

        self.collocations_thresh_slider = QSlider(self.frame_12)
        self.collocations_thresh_slider.setObjectName(u"collocations_thresh_slider")
        self.collocations_thresh_slider.setEnabled(True)
        self.collocations_thresh_slider.setMinimumSize(QSize(30, 0))
        self.collocations_thresh_slider.setMaximumSize(QSize(30, 16777215))
        self.collocations_thresh_slider.setMinimum(0)
        self.collocations_thresh_slider.setMaximum(100)
        self.collocations_thresh_slider.setPageStep(1)
        self.collocations_thresh_slider.setOrientation(Qt.Vertical)

        self.horizontalLayout_20.addWidget(self.collocations_thresh_slider)

        self.collocation_thresh_slider_label = QLabel(self.frame_12)
        self.collocation_thresh_slider_label.setObjectName(u"collocation_thresh_slider_label")
        self.collocation_thresh_slider_label.setMaximumSize(QSize(50, 50))
        self.collocation_thresh_slider_label.setFont(font11)

        self.horizontalLayout_20.addWidget(self.collocation_thresh_slider_label)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_13)


        self.gridLayout_5.addLayout(self.horizontalLayout_20, 2, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_7, 1, 0, 1, 1)


        self.verticalLayout_17.addWidget(self.frame_12)

        self.parameters_window.addTab(self.parameters_windowPage8, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.frame_17 = QFrame(self.tab_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(0, 10, 531, 361))
        self.frame_17.setMinimumSize(QSize(531, 361))
        self.frame_17.setMaximumSize(QSize(531, 361))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_17)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.include_number_checkbox = QCheckBox(self.frame_17)
        self.include_number_checkbox.setObjectName(u"include_number_checkbox")
        self.include_number_checkbox.setFont(font8)
        self.include_number_checkbox.setIconSize(QSize(24, 24))
        self.include_number_checkbox.setChecked(True)

        self.gridLayout_2.addWidget(self.include_number_checkbox, 1, 1, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_19, 1, 0, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_20, 1, 2, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_15, 2, 1, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_16, 0, 1, 1, 1)

        self.parameters_window.addTab(self.tab_2, "")

        self.Parameters_Main.addWidget(self.parameters_window, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_12.addLayout(self.Parameters_Main)


        self.verticalLayout_2.addWidget(self.Parameters_Main_Frame, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.frame_2)


        self.pathsAndparameters.addWidget(self.frame_11)

        self.frame_13 = QFrame(self.frame_main1)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 630))
        self.frame_13.setMaximumSize(QSize(16777215, 630))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_13)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.generated_text_frame = QFrame(self.frame_13)
        self.generated_text_frame.setObjectName(u"generated_text_frame")
        self.generated_text_frame.setMinimumSize(QSize(370, 300))
        self.generated_text_frame.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.generated_text_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.custom_font_directory_selection = QPushButton(self.generated_text_frame)
        self.custom_font_directory_selection.setObjectName(u"custom_font_directory_selection")
        self.custom_font_directory_selection.setMinimumSize(QSize(50, 50))
        self.custom_font_directory_selection.setMaximumSize(QSize(200, 16777215))
        font13 = QFont()
        font13.setFamilies([u"Montserrat"])
        font13.setPointSize(11)
        font13.setBold(True)
        self.custom_font_directory_selection.setFont(font13)
        self.custom_font_directory_selection.setStyleSheet(u"background-color: #7754c8;\n"
"color:#3cf3b6;\n"
"border-radius:10px;")

        self.verticalLayout_3.addWidget(self.custom_font_directory_selection, 0, Qt.AlignHCenter)

        self.font_list = QListWidget(self.generated_text_frame)
        self.font_list.setObjectName(u"font_list")
        self.font_list.setMinimumSize(QSize(0, 200))
        font14 = QFont()
        font14.setPointSize(11)
        font14.setBold(True)
        self.font_list.setFont(font14)
        self.font_list.setStyleSheet(u"border:2px solid gray;")
        self.font_list.setAutoScrollMargin(20)
        self.font_list.setTabKeyNavigation(False)

        self.verticalLayout_3.addWidget(self.font_list)


        self.verticalLayout_21.addWidget(self.generated_text_frame)


        self.pathsAndparameters.addWidget(self.frame_13)


        self.horizontalLayout_23.addLayout(self.pathsAndparameters)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.mask_and_parameters_summary_container = QFrame(self.frame_main1)
        self.mask_and_parameters_summary_container.setObjectName(u"mask_and_parameters_summary_container")
        self.mask_and_parameters_summary_container.setMinimumSize(QSize(300, 5))
        self.mask_and_parameters_summary_container.setMaximumSize(QSize(300, 630))
        self.mask_and_parameters_summary_container.setStyleSheet(u"")
        self.mask_and_parameters_summary_container.setFrameShape(QFrame.StyledPanel)
        self.mask_and_parameters_summary_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.mask_and_parameters_summary_container)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.mask_image_thumbnail = QLabel(self.mask_and_parameters_summary_container)
        self.mask_image_thumbnail.setObjectName(u"mask_image_thumbnail")
        self.mask_image_thumbnail.setMinimumSize(QSize(200, 200))
        self.mask_image_thumbnail.setMaximumSize(QSize(200, 200))
        self.mask_image_thumbnail.setScaledContents(True)

        self.horizontalLayout_19.addWidget(self.mask_image_thumbnail)


        self.verticalLayout_24.addWidget(self.mask_and_parameters_summary_container)

        self.mask_dimensions_label = QLabel(self.frame_main1)
        self.mask_dimensions_label.setObjectName(u"mask_dimensions_label")
        self.mask_dimensions_label.setMaximumSize(QSize(300, 16777215))
        font15 = QFont()
        font15.setFamilies([u"Montserrat"])
        font15.setPointSize(11)
        font15.setBold(True)
        font15.setUnderline(False)
        font15.setStyleStrategy(QFont.PreferDefault)
        self.mask_dimensions_label.setFont(font15)
        self.mask_dimensions_label.setCursor(QCursor(Qt.ArrowCursor))

        self.verticalLayout_24.addWidget(self.mask_dimensions_label, 0, Qt.AlignHCenter)

        self.frame_14 = QFrame(self.frame_main1)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(301, 401))
        self.frame_14.setMaximumSize(QSize(301, 401))
        font16 = QFont()
        font16.setFamilies([u"IBM Plex Sans"])
        font16.setPointSize(10)
        font16.setBold(True)
        self.frame_14.setFont(font16)
        self.frame_14.setStyleSheet(u"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_14)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_2 = QLabel(self.frame_14)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font16)

        self.horizontalLayout_16.addWidget(self.label_2)

        self.repeat_info_label = QLabel(self.frame_14)
        self.repeat_info_label.setObjectName(u"repeat_info_label")
        self.repeat_info_label.setFont(font16)

        self.horizontalLayout_16.addWidget(self.repeat_info_label)


        self.verticalLayout_29.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_18 = QLabel(self.frame_14)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font16)

        self.horizontalLayout_29.addWidget(self.label_18)

        self.margin_info_label = QLabel(self.frame_14)
        self.margin_info_label.setObjectName(u"margin_info_label")
        self.margin_info_label.setFont(font16)

        self.horizontalLayout_29.addWidget(self.margin_info_label)


        self.verticalLayout_29.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_14 = QLabel(self.frame_14)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font16)

        self.horizontalLayout_27.addWidget(self.label_14)

        self.min_font_size_info_label = QLabel(self.frame_14)
        self.min_font_size_info_label.setObjectName(u"min_font_size_info_label")
        self.min_font_size_info_label.setFont(font16)

        self.horizontalLayout_27.addWidget(self.min_font_size_info_label)


        self.verticalLayout_29.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_100 = QLabel(self.frame_14)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setFont(font16)

        self.horizontalLayout_28.addWidget(self.label_100)

        self.max_font_size_info_label = QLabel(self.frame_14)
        self.max_font_size_info_label.setObjectName(u"max_font_size_info_label")
        self.max_font_size_info_label.setFont(font16)

        self.horizontalLayout_28.addWidget(self.max_font_size_info_label)


        self.verticalLayout_29.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_12 = QLabel(self.frame_14)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font16)

        self.horizontalLayout_26.addWidget(self.label_12)

        self.prefer_horizontal_info_label = QLabel(self.frame_14)
        self.prefer_horizontal_info_label.setObjectName(u"prefer_horizontal_info_label")
        self.prefer_horizontal_info_label.setFont(font16)

        self.horizontalLayout_26.addWidget(self.prefer_horizontal_info_label)


        self.verticalLayout_29.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_20 = QLabel(self.frame_14)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font16)

        self.horizontalLayout_30.addWidget(self.label_20)

        self.fontstep_info_label = QLabel(self.frame_14)
        self.fontstep_info_label.setObjectName(u"fontstep_info_label")
        self.fontstep_info_label.setFont(font16)

        self.horizontalLayout_30.addWidget(self.fontstep_info_label)


        self.verticalLayout_29.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_22 = QLabel(self.frame_14)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font16)

        self.horizontalLayout_32.addWidget(self.label_22)

        self.collocations_info_label = QLabel(self.frame_14)
        self.collocations_info_label.setObjectName(u"collocations_info_label")
        self.collocations_info_label.setFont(font16)

        self.horizontalLayout_32.addWidget(self.collocations_info_label)


        self.verticalLayout_29.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_24 = QLabel(self.frame_14)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font16)

        self.horizontalLayout_33.addWidget(self.label_24)

        self.collocations_thresh_info_label = QLabel(self.frame_14)
        self.collocations_thresh_info_label.setObjectName(u"collocations_thresh_info_label")
        self.collocations_thresh_info_label.setFont(font16)

        self.horizontalLayout_33.addWidget(self.collocations_thresh_info_label)


        self.verticalLayout_29.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_26 = QLabel(self.frame_14)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font16)

        self.horizontalLayout_34.addWidget(self.label_26)

        self.include_numbers_info_label = QLabel(self.frame_14)
        self.include_numbers_info_label.setObjectName(u"include_numbers_info_label")
        self.include_numbers_info_label.setFont(font16)

        self.horizontalLayout_34.addWidget(self.include_numbers_info_label)


        self.verticalLayout_29.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_28 = QLabel(self.frame_14)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font16)

        self.horizontalLayout_35.addWidget(self.label_28)

        self.scale_multiplier_info_label = QLabel(self.frame_14)
        self.scale_multiplier_info_label.setObjectName(u"scale_multiplier_info_label")
        self.scale_multiplier_info_label.setFont(font16)

        self.horizontalLayout_35.addWidget(self.scale_multiplier_info_label)


        self.verticalLayout_29.addLayout(self.horizontalLayout_35)


        self.verticalLayout_24.addWidget(self.frame_14)


        self.horizontalLayout_23.addLayout(self.verticalLayout_24)


        self.verticalLayout_25.addWidget(self.frame_main1, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_15 = QFrame(self.FRAME_X)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.color_presets_group = QGroupBox(self.frame_15)
        self.color_presets_group.setObjectName(u"color_presets_group")
        self.color_presets_group.setMinimumSize(QSize(535, 291))
        self.color_presets_group.setMaximumSize(QSize(535, 291))
        font17 = QFont()
        font17.setFamilies([u"IBM Plex Sans"])
        font17.setPointSize(11)
        font17.setBold(False)
        self.color_presets_group.setFont(font17)
        self.verticalLayout_18 = QVBoxLayout(self.color_presets_group)
        self.verticalLayout_18.setSpacing(5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(5, 0, 5, 0)
        self.cp_title_dropdown = QFrame(self.color_presets_group)
        self.cp_title_dropdown.setObjectName(u"cp_title_dropdown")
        self.cp_title_dropdown.setMinimumSize(QSize(200, 62))
        self.cp_title_dropdown.setMaximumSize(QSize(200, 100))
        self.verticalLayout_19 = QVBoxLayout(self.cp_title_dropdown)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_color_presets = QLabel(self.cp_title_dropdown)
        self.label_color_presets.setObjectName(u"label_color_presets")
        self.label_color_presets.setMaximumSize(QSize(150, 30))
        font18 = QFont()
        font18.setFamilies([u"IBM Plex Sans"])
        font18.setPointSize(14)
        font18.setBold(True)
        self.label_color_presets.setFont(font18)

        self.verticalLayout_19.addWidget(self.label_color_presets, 0, Qt.AlignHCenter)

        self.colormaps_dropdown = QComboBox(self.cp_title_dropdown)
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.setObjectName(u"colormaps_dropdown")
        self.colormaps_dropdown.setMinimumSize(QSize(0, 30))
        self.colormaps_dropdown.setMaximumSize(QSize(300, 30))
        self.colormaps_dropdown.setFont(font18)
        self.colormaps_dropdown.setStyleSheet(u"background-color: #7754c8;\n"
"color:#3cf3b6;\n"
"")

        self.verticalLayout_19.addWidget(self.colormaps_dropdown)


        self.verticalLayout_18.addWidget(self.cp_title_dropdown, 0, Qt.AlignHCenter)

        self.RandomColorGroupBox = QGroupBox(self.color_presets_group)
        self.RandomColorGroupBox.setObjectName(u"RandomColorGroupBox")
        self.RandomColorGroupBox.setMinimumSize(QSize(508, 110))
        self.horizontalLayout_22 = QHBoxLayout(self.RandomColorGroupBox)
        self.horizontalLayout_22.setSpacing(5)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.rColorRangeContainer = QFrame(self.RandomColorGroupBox)
        self.rColorRangeContainer.setObjectName(u"rColorRangeContainer")
        self.rColorRangeContainer.setMinimumSize(QSize(256, 150))
        self.rColorRangeContainer.setMaximumSize(QSize(256, 150))
        self.verticalLayout_20 = QVBoxLayout(self.rColorRangeContainer)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.ColorsMinGP = QGroupBox(self.rColorRangeContainer)
        self.ColorsMinGP.setObjectName(u"ColorsMinGP")
        self.ColorsMinGP.setMinimumSize(QSize(254, 71))
        self.ColorsMinGP.setMaximumSize(QSize(254, 71))
        self.horizontalLayout_14 = QHBoxLayout(self.ColorsMinGP)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.red_min = QSpinBox(self.ColorsMinGP)
        self.red_min.setObjectName(u"red_min")
        font19 = QFont()
        font19.setFamilies([u"Play"])
        font19.setPointSize(20)
        font19.setBold(True)
        self.red_min.setFont(font19)
        self.red_min.setStyleSheet(u"background-color: rgb(200, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.red_min.setMinimum(0)
        self.red_min.setMaximum(255)
        self.red_min.setValue(20)

        self.horizontalLayout_14.addWidget(self.red_min)

        self.green_min = QSpinBox(self.ColorsMinGP)
        self.green_min.setObjectName(u"green_min")
        self.green_min.setFont(font19)
        self.green_min.setStyleSheet(u"background-color: rgb(0, 200, 0);\n"
"color: rgb(25, 25, 25);")
        self.green_min.setMaximum(255)
        self.green_min.setValue(20)

        self.horizontalLayout_14.addWidget(self.green_min)

        self.blue_min = QSpinBox(self.ColorsMinGP)
        self.blue_min.setObjectName(u"blue_min")
        self.blue_min.setFont(font19)
        self.blue_min.setStyleSheet(u"background-color: rgb(0, 0, 200);\n"
"color: rgb(255, 255, 255);")
        self.blue_min.setMaximum(255)
        self.blue_min.setValue(20)

        self.horizontalLayout_14.addWidget(self.blue_min)


        self.verticalLayout_20.addWidget(self.ColorsMinGP)

        self.ColorsMaxGP = QGroupBox(self.rColorRangeContainer)
        self.ColorsMaxGP.setObjectName(u"ColorsMaxGP")
        self.ColorsMaxGP.setMinimumSize(QSize(254, 71))
        self.ColorsMaxGP.setMaximumSize(QSize(254, 71))
        self.horizontalLayout_15 = QHBoxLayout(self.ColorsMaxGP)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.red_max = QSpinBox(self.ColorsMaxGP)
        self.red_max.setObjectName(u"red_max")
        self.red_max.setFont(font19)
        self.red_max.setStyleSheet(u"background-color: rgb(200, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.red_max.setMinimum(0)
        self.red_max.setMaximum(255)
        self.red_max.setValue(150)

        self.horizontalLayout_15.addWidget(self.red_max)

        self.green_max = QSpinBox(self.ColorsMaxGP)
        self.green_max.setObjectName(u"green_max")
        self.green_max.setFont(font19)
        self.green_max.setStyleSheet(u"background-color: rgb(0, 200, 0);\n"
"color: rgb(25, 25, 25);")
        self.green_max.setMaximum(255)
        self.green_max.setValue(250)

        self.horizontalLayout_15.addWidget(self.green_max)

        self.blue_max = QSpinBox(self.ColorsMaxGP)
        self.blue_max.setObjectName(u"blue_max")
        self.blue_max.setFont(font19)
        self.blue_max.setStyleSheet(u"background-color: rgb(0, 0, 200);\n"
"color: rgb(255, 255, 255);")
        self.blue_max.setMaximum(255)
        self.blue_max.setValue(150)

        self.horizontalLayout_15.addWidget(self.blue_max)


        self.verticalLayout_20.addWidget(self.ColorsMaxGP)


        self.horizontalLayout_22.addWidget(self.rColorRangeContainer)

        self.frame_18 = QFrame(self.RandomColorGroupBox)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(252, 150))
        self.frame_18.setMaximumSize(QSize(252, 150))
        self.verticalLayout_22 = QVBoxLayout(self.frame_18)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.color_range_preset_buttons_frame = QFrame(self.frame_18)
        self.color_range_preset_buttons_frame.setObjectName(u"color_range_preset_buttons_frame")
        self.color_range_preset_buttons_frame.setMinimumSize(QSize(100, 50))
        self.color_range_preset_buttons_frame.setMaximumSize(QSize(266, 28))
        self.horizontalLayout_25 = QHBoxLayout(self.color_range_preset_buttons_frame)
        self.horizontalLayout_25.setSpacing(1)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.rcp_maximize_blue = QPushButton(self.color_range_preset_buttons_frame)
        self.rcp_maximize_blue.setObjectName(u"rcp_maximize_blue")
        font20 = QFont()
        font20.setFamilies([u"Barlow"])
        font20.setPointSize(10)
        font20.setBold(True)
        self.rcp_maximize_blue.setFont(font20)
        self.rcp_maximize_blue.setStyleSheet(u"color: rgb(0, 0, 250);")

        self.horizontalLayout_17.addWidget(self.rcp_maximize_blue)

        self.rcp_minimize_blue = QPushButton(self.color_range_preset_buttons_frame)
        self.rcp_minimize_blue.setObjectName(u"rcp_minimize_blue")
        self.rcp_minimize_blue.setFont(font20)
        self.rcp_minimize_blue.setStyleSheet(u"color: rgb(0, 0, 250);")

        self.horizontalLayout_17.addWidget(self.rcp_minimize_blue)


        self.horizontalLayout_25.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.rcp_minimize_green = QPushButton(self.color_range_preset_buttons_frame)
        self.rcp_minimize_green.setObjectName(u"rcp_minimize_green")
        self.rcp_minimize_green.setFont(font20)
        self.rcp_minimize_green.setStyleSheet(u"color: rgb(0, 250, 0);")

        self.horizontalLayout_31.addWidget(self.rcp_minimize_green)

        self.rcp_maximize_green = QPushButton(self.color_range_preset_buttons_frame)
        self.rcp_maximize_green.setObjectName(u"rcp_maximize_green")
        self.rcp_maximize_green.setFont(font20)
        self.rcp_maximize_green.setStyleSheet(u"color: rgb(0, 250, 0);")

        self.horizontalLayout_31.addWidget(self.rcp_maximize_green)


        self.horizontalLayout_25.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.rcp_minimize_red = QPushButton(self.color_range_preset_buttons_frame)
        self.rcp_minimize_red.setObjectName(u"rcp_minimize_red")
        self.rcp_minimize_red.setFont(font20)
        self.rcp_minimize_red.setStyleSheet(u"color: rgb(250, 0, 0);")

        self.horizontalLayout_11.addWidget(self.rcp_minimize_red)

        self.rcp_maximize_red = QPushButton(self.color_range_preset_buttons_frame)
        self.rcp_maximize_red.setObjectName(u"rcp_maximize_red")
        self.rcp_maximize_red.setFont(font20)
        self.rcp_maximize_red.setStyleSheet(u"color: rgb(250, 0, 0);")

        self.horizontalLayout_11.addWidget(self.rcp_maximize_red)


        self.horizontalLayout_25.addLayout(self.horizontalLayout_11)


        self.verticalLayout_22.addWidget(self.color_range_preset_buttons_frame)

        self.rcpresets3 = QFrame(self.frame_18)
        self.rcpresets3.setObjectName(u"rcpresets3")
        self.rcpresets3.setMinimumSize(QSize(100, 50))
        self.rcpresets3.setMaximumSize(QSize(164, 26))
        self.gridLayout_3 = QGridLayout(self.rcpresets3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.rcp_bright = QPushButton(self.rcpresets3)
        self.rcp_bright.setObjectName(u"rcp_bright")
        self.rcp_bright.setFont(font20)

        self.gridLayout_3.addWidget(self.rcp_bright, 0, 0, 1, 1)

        self.rcp_reset = QPushButton(self.rcpresets3)
        self.rcp_reset.setObjectName(u"rcp_reset")
        self.rcp_reset.setFont(font20)

        self.gridLayout_3.addWidget(self.rcp_reset, 0, 2, 1, 1)

        self.rcp_dark = QPushButton(self.rcpresets3)
        self.rcp_dark.setObjectName(u"rcp_dark")
        self.rcp_dark.setFont(font20)

        self.gridLayout_3.addWidget(self.rcp_dark, 0, 1, 1, 1)


        self.verticalLayout_22.addWidget(self.rcpresets3)


        self.horizontalLayout_22.addWidget(self.frame_18)


        self.verticalLayout_18.addWidget(self.RandomColorGroupBox)


        self.horizontalLayout_21.addWidget(self.color_presets_group)

        self.generate_Wordcloud_Frame = QFrame(self.frame_15)
        self.generate_Wordcloud_Frame.setObjectName(u"generate_Wordcloud_Frame")
        self.generate_Wordcloud_Frame.setMinimumSize(QSize(831, 350))
        self.generate_Wordcloud_Frame.setMaximumSize(QSize(831, 350))
        self.generate_Wordcloud_Frame.setFrameShape(QFrame.StyledPanel)
        self.generate_Wordcloud_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.generate_Wordcloud_Frame)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.generated_text_label = QLabel(self.generate_Wordcloud_Frame)
        self.generated_text_label.setObjectName(u"generated_text_label")
        font21 = QFont()
        font21.setFamilies([u"Play"])
        font21.setPointSize(14)
        font21.setBold(True)
        self.generated_text_label.setFont(font21)

        self.verticalLayout_23.addWidget(self.generated_text_label, 0, Qt.AlignHCenter)

        self.word_input = QTextEdit(self.generate_Wordcloud_Frame)
        self.word_input.setObjectName(u"word_input")
        font22 = QFont()
        font22.setFamilies([u"Play"])
        font22.setPointSize(14)
        font22.setBold(False)
        font22.setItalic(False)
        self.word_input.setFont(font22)
        self.word_input.setStyleSheet(u"border:2px solid red;")
        self.word_input.setFrameShadow(QFrame.Plain)
        self.word_input.setLineWidth(1)
        self.word_input.setTabChangesFocus(False)
        self.word_input.setUndoRedoEnabled(True)

        self.verticalLayout_23.addWidget(self.word_input)

        self.export_as_frame = QGroupBox(self.generate_Wordcloud_Frame)
        self.export_as_frame.setObjectName(u"export_as_frame")
        self.export_as_frame.setMinimumSize(QSize(90, 61))
        self.export_as_frame.setMaximumSize(QSize(102, 70))
        font23 = QFont()
        font23.setFamilies([u"Sarpanch SemiBold"])
        font23.setBold(False)
        self.export_as_frame.setFont(font23)
        self.verticalLayout_26 = QVBoxLayout(self.export_as_frame)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.exportAs_label = QLabel(self.export_as_frame)
        self.exportAs_label.setObjectName(u"exportAs_label")
        self.exportAs_label.setMinimumSize(QSize(88, 25))
        self.exportAs_label.setFont(font18)

        self.verticalLayout_26.addWidget(self.exportAs_label)

        self.export_format_options = QComboBox(self.export_as_frame)
        self.export_format_options.addItem("")
        self.export_format_options.addItem("")
        self.export_format_options.addItem("")
        self.export_format_options.setObjectName(u"export_format_options")
        self.export_format_options.setFont(font5)

        self.verticalLayout_26.addWidget(self.export_format_options, 0, Qt.AlignHCenter)


        self.verticalLayout_23.addWidget(self.export_as_frame, 0, Qt.AlignHCenter)

        self.generate_wordcloud_button = QPushButton(self.generate_Wordcloud_Frame)
        self.generate_wordcloud_button.setObjectName(u"generate_wordcloud_button")
        self.generate_wordcloud_button.setEnabled(True)
        self.generate_wordcloud_button.setMinimumSize(QSize(700, 150))
        self.generate_wordcloud_button.setFont(font19)
        self.generate_wordcloud_button.setToolTipDuration(-1)
        self.generate_wordcloud_button.setStyleSheet(u"QPushButton{\n"
"color: rgb(200,200,200);\n"
"background-color: rgb(50, 50, 50);\n"
"border: 10px solid green;\n"
"border-radius: 50px;\n"
"padding: 50px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(0,255,0);\n"
"border: 10px solid rgb(50, 50, 50);\n"
"}")
        self.generate_wordcloud_button.setText(u"")
        icon1 = QIcon()
        icon1.addFile(u":/Media/LogoAssetForButton.png", QSize(), QIcon.Normal, QIcon.Off)
        self.generate_wordcloud_button.setIcon(icon1)
        self.generate_wordcloud_button.setIconSize(QSize(100, 100))
        self.generate_wordcloud_button.setCheckable(False)
        self.generate_wordcloud_button.setChecked(False)
        self.generate_wordcloud_button.setAutoRepeat(False)
        self.generate_wordcloud_button.setAutoExclusive(False)
        self.generate_wordcloud_button.setAutoDefault(False)
        self.generate_wordcloud_button.setFlat(False)

        self.verticalLayout_23.addWidget(self.generate_wordcloud_button)


        self.horizontalLayout_21.addWidget(self.generate_Wordcloud_Frame)


        self.verticalLayout_25.addWidget(self.frame_15, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.FRAME_X)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1622, 22))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)

        self.parameters_window.setCurrentIndex(1)
        self.colormaps_dropdown.setCurrentIndex(7)
        self.generate_wordcloud_button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WCGX", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.actionShit.setText(QCoreApplication.translate("MainWindow", u"Shit", None))
        self.app_title.setText(QCoreApplication.translate("MainWindow", u"WordCloud Generator X-Treme", None))
#if QT_CONFIG(tooltip)
        self.mask_select_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Select Mask image </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.mask_select_button.setText(QCoreApplication.translate("MainWindow", u"Select Mask", None))
#if QT_CONFIG(tooltip)
        self.select_destination_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Select destination for generated PNG file</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.select_destination_button.setText(QCoreApplication.translate("MainWindow", u"Select Destination", None))
#if QT_CONFIG(tooltip)
        self.open_destination_folder.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Open destination folder </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.open_destination_folder.setText(QCoreApplication.translate("MainWindow", u"\u25b2", None))
        self.Parameters_Title_label.setText(QCoreApplication.translate("MainWindow", u"WordCloud Parameters", None))

        __sortingEnabled = self.parameters_list.isSortingEnabled()
        self.parameters_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.parameters_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Repeat Words", None));
        ___qlistwidgetitem1 = self.parameters_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Prefer-Horizontal", None));
        ___qlistwidgetitem2 = self.parameters_list.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Margin between words", None));
        ___qlistwidgetitem3 = self.parameters_list.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Min/Max Font-size", None));
        ___qlistwidgetitem4 = self.parameters_list.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Minimum Word Length", None));
        ___qlistwidgetitem5 = self.parameters_list.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Maximum No. of Words", None));
        ___qlistwidgetitem6 = self.parameters_list.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Contour Width", None));
        ___qlistwidgetitem7 = self.parameters_list.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Contour Color", None));
        ___qlistwidgetitem8 = self.parameters_list.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Font Step", None));
        ___qlistwidgetitem9 = self.parameters_list.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Relative Scaling", None));
        ___qlistwidgetitem10 = self.parameters_list.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"StopWords", None));
        ___qlistwidgetitem11 = self.parameters_list.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Collocations", None));
        ___qlistwidgetitem12 = self.parameters_list.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Collocations Threshold", None));
        ___qlistwidgetitem13 = self.parameters_list.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Normalize Plurals", None));
        ___qlistwidgetitem14 = self.parameters_list.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Include Numbers", None));
        ___qlistwidgetitem15 = self.parameters_list.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Scale", None));
        self.parameters_list.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("MainWindow", u"Whether to repeat words and phrases \n"
"until max_words or min_font_size \n"
"is reached.", None))
#if QT_CONFIG(tooltip)
        self.repeat_words_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Enable/Disable word repeat </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.repeat_words_label.setText(QCoreApplication.translate("MainWindow", u"Repeat", None))
#if QT_CONFIG(tooltip)
        self.repeat_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.repeat_checkbox.setText("")
        self.parameters_window.setTabText(self.parameters_window.indexOf(self.parameters_windowPage1), QCoreApplication.translate("MainWindow", u"Repeat", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Set the smallest and largest allowed\n"
" font sizes.", None))
#if QT_CONFIG(tooltip)
        self.min_font_size_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Control the minimum font size of generated word(s) </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.min_font_size_label.setText(QCoreApplication.translate("MainWindow", u"Min Font Size", None))
#if QT_CONFIG(tooltip)
        self.min_font_size_slider.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Set the minimum font size </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_min_font_size_slider.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Minimum Font Size </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_min_font_size_slider.setText(QCoreApplication.translate("MainWindow", u"00", None))
#if QT_CONFIG(tooltip)
        self.max_font_size_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Control the maximum font size of generated word(s) </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.max_font_size_label.setText(QCoreApplication.translate("MainWindow", u"Max Font Size", None))
#if QT_CONFIG(tooltip)
        self.max_font_size_slider.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Set the maximum font size </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_max_font_size_slider.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Maximum Font Size </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_max_font_size_slider.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.parameters_window.setTabText(self.parameters_window.indexOf(self.parameters_windowPage2), QCoreApplication.translate("MainWindow", u"Font Size", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Font Step > 1 might speed up\n"
"computation, but result in a worse fit.", None))
#if QT_CONFIG(tooltip)
        self.fontstep_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Control the minimum font size of generated word(s) </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.fontstep_label.setText(QCoreApplication.translate("MainWindow", u"Font Step", None))
#if QT_CONFIG(tooltip)
        self.font_step_indicator_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Minimum Font Size </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.font_step_indicator_label.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.parameters_window.setTabText(self.parameters_window.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Font Step", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Minimum allowed margin between words.", None))
#if QT_CONFIG(tooltip)
        self.margin_label_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Control the space between the generated words </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.margin_label_2.setText(QCoreApplication.translate("MainWindow", u"Margin", None))
#if QT_CONFIG(tooltip)
        self.margin_slider.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Set the margin between the generated words </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_margin_slider.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Margin between generated words</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_margin_slider.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.parameters_window.setTabText(self.parameters_window.indexOf(self.parameters_windowPage3), QCoreApplication.translate("MainWindow", u"Margin", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"The ratio of times to try horizontal fitting.\n"
"If odds < 1 the algorithm will try\n"
"rotating the word if it doesn\u2019t fit.\n"
"If odds = 1 - horizontal fit is preferred,\n"
"but not guaranteed!", None))
#if QT_CONFIG(tooltip)
        self.prefer_horizontal_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Text orientation control (odds) </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.prefer_horizontal_label.setText(QCoreApplication.translate("MainWindow", u"Horizontal Odds", None))
#if QT_CONFIG(tooltip)
        self.prefer_horizontal_slider.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">1 = Mostly Horizontal Text</span></p><p><span style=\" font-size:10pt;\">0 = No Horizontal Text</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_text_orientation_slider.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Text orientation odds </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_text_orientation_slider.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.parameters_window.setTabText(self.parameters_window.indexOf(self.parameters_windowPage4), QCoreApplication.translate("MainWindow", u"H. Odds", None))
#if QT_CONFIG(tooltip)
        self.image_scale_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Exported image size multiplier !!! </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.image_scale_label.setText(QCoreApplication.translate("MainWindow", u"Image Scale", None))
#if QT_CONFIG(tooltip)
        self.scale_slider.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_scale_slider.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Exported image size will be multiplied by this number !!!</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_scale_slider.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Mask image size * Image Scale = Exported Image size\n"
"Using a smaller mask and increasing the scale\n"
"results in faster rendering.", None))
        self.parameters_window.setTabText(self.parameters_window.indexOf(self.parameters_windowPage5), QCoreApplication.translate("MainWindow", u"Scale", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"The words that will be eliminated.\n"
"If None, the built-in STOPWORDS list will be used.\n"
"Ignored if using generate_from_frequencies.", None))
#if QT_CONFIG(tooltip)
        self.stopwords_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Include/Exclude common words </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.stopwords_label.setText(QCoreApplication.translate("MainWindow", u"StopWords", None))
#if QT_CONFIG(tooltip)
        self.stopwords_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Checked - common words will be excluded <br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.stopwords_checkbox.setText("")
        self.parameters_window.setTabText(self.parameters_window.indexOf(self.parameters_windowPage6), QCoreApplication.translate("MainWindow", u"StopWords", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Whether to include collocations (bigrams) of two words.\n"
"Ignored if using generate_from_frequencies.", None))
        self.label_collocations.setText(QCoreApplication.translate("MainWindow", u"Collocations", None))
        self.collocations_checkbox.setText("")
        self.parameters_window.setTabText(self.parameters_window.indexOf(self.parameters_windowPage7), QCoreApplication.translate("MainWindow", u"CLC", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"The Dunning likelihood collocation score is calculated for each\n"
"bigram based on its frequency and compared to the\n"
"expected co-occurrence by random chance.\n"
"The collocation threshold is used as a filtering parameter\n"
"to include only statistically significant bigrams in the word cloud.\n"
"\n"
"- A lower collocation threshold makes it easier for word pairs(bigrams)\n"
"to pass the significance test and be treated as phrases.\n"
"- A higher threshold means that bigrams must occur together\n"
"much more frequently than expected by random chance\n"
"to be included in the word cloud as 1 phrase.", None))
        self.label_collocations_thresh.setText(QCoreApplication.translate("MainWindow", u"Collocation Threshold", None))
        self.collocation_thresh_slider_label.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.parameters_window.setTabText(self.parameters_window.indexOf(self.parameters_windowPage8), QCoreApplication.translate("MainWindow", u"CLC Thresh", None))
        self.include_number_checkbox.setText(QCoreApplication.translate("MainWindow", u"Include Numbers", None))
        self.parameters_window.setTabText(self.parameters_window.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Numbers", None))
        self.custom_font_directory_selection.setText(QCoreApplication.translate("MainWindow", u"  Change Fonts Folder  ", None))
        self.mask_image_thumbnail.setText(QCoreApplication.translate("MainWindow", u"MASK IMAGE WILL BE PLACED HERE", None))
        self.mask_dimensions_label.setText(QCoreApplication.translate("MainWindow", u"mask_dimensions_label", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Repeat Words:", None))
        self.repeat_info_label.setText(QCoreApplication.translate("MainWindow", u"result here", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Margin:", None))
        self.margin_info_label.setText(QCoreApplication.translate("MainWindow", u"result here", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Min. Font Size:", None))
        self.min_font_size_info_label.setText(QCoreApplication.translate("MainWindow", u"result here", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Max Font Size:", None))
        self.max_font_size_info_label.setText(QCoreApplication.translate("MainWindow", u"result here", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"H. Odds:", None))
        self.prefer_horizontal_info_label.setText(QCoreApplication.translate("MainWindow", u"result here", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Font Step:", None))
        self.fontstep_info_label.setText(QCoreApplication.translate("MainWindow", u"result here", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"CLC:", None))
        self.collocations_info_label.setText(QCoreApplication.translate("MainWindow", u"result here", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"CLC Thresh:", None))
        self.collocations_thresh_info_label.setText(QCoreApplication.translate("MainWindow", u"result here", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Include Numbers:", None))
        self.include_numbers_info_label.setText(QCoreApplication.translate("MainWindow", u"result here", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Scale Multiplier:", None))
        self.scale_multiplier_info_label.setText(QCoreApplication.translate("MainWindow", u"result here", None))
        self.color_presets_group.setTitle("")
        self.label_color_presets.setText(QCoreApplication.translate("MainWindow", u"Color Presets", None))
        self.colormaps_dropdown.setItemText(0, QCoreApplication.translate("MainWindow", u"Default", None))
        self.colormaps_dropdown.setItemText(1, QCoreApplication.translate("MainWindow", u"Reds", None))
        self.colormaps_dropdown.setItemText(2, QCoreApplication.translate("MainWindow", u"Greens", None))
        self.colormaps_dropdown.setItemText(3, QCoreApplication.translate("MainWindow", u"Blues", None))
        self.colormaps_dropdown.setItemText(4, QCoreApplication.translate("MainWindow", u"Greys", None))
        self.colormaps_dropdown.setItemText(5, QCoreApplication.translate("MainWindow", u"Purples", None))
        self.colormaps_dropdown.setItemText(6, QCoreApplication.translate("MainWindow", u"Oranges", None))
        self.colormaps_dropdown.setItemText(7, QCoreApplication.translate("MainWindow", u"plasma", None))
        self.colormaps_dropdown.setItemText(8, QCoreApplication.translate("MainWindow", u"Accent", None))
        self.colormaps_dropdown.setItemText(9, QCoreApplication.translate("MainWindow", u"Random Colors", None))
        self.colormaps_dropdown.setItemText(10, QCoreApplication.translate("MainWindow", u"Paired", None))
        self.colormaps_dropdown.setItemText(11, QCoreApplication.translate("MainWindow", u"Dark2", None))
        self.colormaps_dropdown.setItemText(12, QCoreApplication.translate("MainWindow", u"Spectral", None))
        self.colormaps_dropdown.setItemText(13, QCoreApplication.translate("MainWindow", u"Pastel1", None))
        self.colormaps_dropdown.setItemText(14, QCoreApplication.translate("MainWindow", u"Pastel2", None))
        self.colormaps_dropdown.setItemText(15, QCoreApplication.translate("MainWindow", u"Wistia", None))
        self.colormaps_dropdown.setItemText(16, QCoreApplication.translate("MainWindow", u"Set1", None))
        self.colormaps_dropdown.setItemText(17, QCoreApplication.translate("MainWindow", u"Set2", None))
        self.colormaps_dropdown.setItemText(18, QCoreApplication.translate("MainWindow", u"Set3", None))
        self.colormaps_dropdown.setItemText(19, QCoreApplication.translate("MainWindow", u"winter", None))
        self.colormaps_dropdown.setItemText(20, QCoreApplication.translate("MainWindow", u"spring", None))
        self.colormaps_dropdown.setItemText(21, QCoreApplication.translate("MainWindow", u"summer", None))
        self.colormaps_dropdown.setItemText(22, QCoreApplication.translate("MainWindow", u"autumn", None))
        self.colormaps_dropdown.setItemText(23, QCoreApplication.translate("MainWindow", u"inferno", None))
        self.colormaps_dropdown.setItemText(24, QCoreApplication.translate("MainWindow", u"magma", None))
        self.colormaps_dropdown.setItemText(25, QCoreApplication.translate("MainWindow", u"twilight", None))
        self.colormaps_dropdown.setItemText(26, QCoreApplication.translate("MainWindow", u"twilight_shifted", None))
        self.colormaps_dropdown.setItemText(27, QCoreApplication.translate("MainWindow", u"hot", None))
        self.colormaps_dropdown.setItemText(28, QCoreApplication.translate("MainWindow", u"afmhot", None))
        self.colormaps_dropdown.setItemText(29, QCoreApplication.translate("MainWindow", u"cool", None))
        self.colormaps_dropdown.setItemText(30, QCoreApplication.translate("MainWindow", u"coolwarm", None))
        self.colormaps_dropdown.setItemText(31, QCoreApplication.translate("MainWindow", u"cubehelix", None))
        self.colormaps_dropdown.setItemText(32, QCoreApplication.translate("MainWindow", u"gray", None))
        self.colormaps_dropdown.setItemText(33, QCoreApplication.translate("MainWindow", u"bone", None))
        self.colormaps_dropdown.setItemText(34, QCoreApplication.translate("MainWindow", u"tab10", None))
        self.colormaps_dropdown.setItemText(35, QCoreApplication.translate("MainWindow", u"tab20", None))
        self.colormaps_dropdown.setItemText(36, QCoreApplication.translate("MainWindow", u"seismic", None))
        self.colormaps_dropdown.setItemText(37, QCoreApplication.translate("MainWindow", u"prism", None))
        self.colormaps_dropdown.setItemText(38, QCoreApplication.translate("MainWindow", u"ocean", None))
        self.colormaps_dropdown.setItemText(39, QCoreApplication.translate("MainWindow", u"terrain", None))
        self.colormaps_dropdown.setItemText(40, QCoreApplication.translate("MainWindow", u"rainbow", None))
        self.colormaps_dropdown.setItemText(41, QCoreApplication.translate("MainWindow", u"turbo", None))

        self.ColorsMinGP.setTitle(QCoreApplication.translate("MainWindow", u"Min", None))
        self.ColorsMaxGP.setTitle(QCoreApplication.translate("MainWindow", u"Max", None))
#if QT_CONFIG(tooltip)
        self.rcp_maximize_blue.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Max Blue </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rcp_maximize_blue.setText(QCoreApplication.translate("MainWindow", u"\u25b2", None))
#if QT_CONFIG(tooltip)
        self.rcp_minimize_blue.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Min Blue </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rcp_minimize_blue.setText(QCoreApplication.translate("MainWindow", u"\u25bc", None))
#if QT_CONFIG(tooltip)
        self.rcp_minimize_green.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Min Green </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rcp_minimize_green.setText(QCoreApplication.translate("MainWindow", u"\u25bc", None))
#if QT_CONFIG(tooltip)
        self.rcp_maximize_green.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Max Green </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rcp_maximize_green.setText(QCoreApplication.translate("MainWindow", u"\u25b2", None))
#if QT_CONFIG(tooltip)
        self.rcp_minimize_red.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Min Red </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rcp_minimize_red.setText(QCoreApplication.translate("MainWindow", u"\u25bc", None))
#if QT_CONFIG(tooltip)
        self.rcp_maximize_red.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Max Red </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rcp_maximize_red.setText(QCoreApplication.translate("MainWindow", u"\u25b2", None))
#if QT_CONFIG(tooltip)
        self.rcp_bright.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Bright color range </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rcp_bright.setText(QCoreApplication.translate("MainWindow", u"Bright", None))
#if QT_CONFIG(tooltip)
        self.rcp_reset.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Reset all colors to max range </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rcp_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
#if QT_CONFIG(tooltip)
        self.rcp_dark.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Dark color range </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rcp_dark.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.generated_text_label.setText(QCoreApplication.translate("MainWindow", u"Generated Text:", None))
        self.word_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"WordCloud text goes here. Different words will be identified based on space. Ex: word1 word2", None))
        self.export_as_frame.setTitle("")
        self.exportAs_label.setText(QCoreApplication.translate("MainWindow", u"Export As", None))
        self.export_format_options.setItemText(0, QCoreApplication.translate("MainWindow", u"PNG", None))
        self.export_format_options.setItemText(1, QCoreApplication.translate("MainWindow", u"SVG", None))
        self.export_format_options.setItemText(2, QCoreApplication.translate("MainWindow", u"BOTH", None))

#if QT_CONFIG(tooltip)
        self.export_format_options.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Select output file format </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.generate_wordcloud_button.setToolTip(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Generate WordCloud </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.generate_wordcloud_button.setShortcut("")
#endif // QT_CONFIG(shortcut)
    # retranslateUi

