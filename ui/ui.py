# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QButtonGroup,
    QCheckBox, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QListView,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QTabWidget, QTextEdit, QVBoxLayout,
    QWidget)
import Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1868, 1125)
        icon = QIcon()
        icon.addFile(u":/Icon/WCGXicon2.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget{\n"
"/*font: 700 9pt \"Inter\";*/\n"
"background-color: rgb(20, 20, 20);\n"
"color:#e6e6e6;\n"
"}\n"
"QLabel, QFrame, QToolButton{\n"
"background:none;\n"
"}\n"
"QToolBar{\n"
"background-color:rgba(200,0,200,50);\n"
"}\n"
"QPushButton:pressed{\n"
"	 padding-left: 3px;\n"
"     padding-top: 3px;\n"
"}\n"
"QPushButton{\n"
"background-color: rgba(100,100,100,150);\n"
"color:#E6E6FA;/*#3cf3b6;*/\n"
"border-radius:10px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, -1, 0)
        self.TitleFrame = QFrame(self.centralwidget)
        self.TitleFrame.setObjectName(u"TitleFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.TitleFrame.sizePolicy().hasHeightForWidth())
        self.TitleFrame.setSizePolicy(sizePolicy1)
        self.gridLayout_11 = QGridLayout(self.TitleFrame)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.WordInputAndParametersFrame = QFrame(self.TitleFrame)
        self.WordInputAndParametersFrame.setObjectName(u"WordInputAndParametersFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.WordInputAndParametersFrame.sizePolicy().hasHeightForWidth())
        self.WordInputAndParametersFrame.setSizePolicy(sizePolicy2)
        self.gridLayout_3 = QGridLayout(self.WordInputAndParametersFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(5)
        self.gridLayout_3.setVerticalSpacing(10)
        self.gridLayout_3.setContentsMargins(0, -1, -1, -1)
        self.parameters_window = QTabWidget(self.WordInputAndParametersFrame)
        self.parameters_window.setObjectName(u"parameters_window")
        self.parameters_window.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.parameters_window.sizePolicy().hasHeightForWidth())
        self.parameters_window.setSizePolicy(sizePolicy3)
        self.parameters_window.setMinimumSize(QSize(700, 500))
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setKerning(True)
        self.parameters_window.setFont(font)
        self.parameters_window.setStyleSheet(u"/* Style the QTabWidget */\n"
"QTabWidget {\n"
"    background-color: lightgray; /* Background color of the tab widget */\n"
"    border: 1px solid gray; /* Border around the tab widget */\n"
"}\n"
"\n"
"/* Style the QTabBar (the tab strip) */\n"
"QTabWidget::tab-bar {\n"
"    alignment: center; /* Align tabs to the left (use 'right' or 'center' as needed) */\n"
"}\n"
"\n"
"/* Style individual tabs (QTabBar tabs) */\n"
"QTabBar::tab {\n"
"    background-color: #141414; /* Background color of the tabs */\n"
"    border: 1px solid gray; /* Border around the tabs */\n"
"    padding: 4px 12px; /* Padding inside the tabs (vertical-horizontal) */\n"
"	color:#e6e6e6;\n"
"}\n"
"\n"
"/* Style the selected tab (active tab) */\n"
"QTabBar::tab:selected {\n"
"    background-color: #e6e6e6; /* Background color of the selected tab */\n"
"	color:#141414;\n"
"}\n"
"\n"
"/* Style the tab content area (where the widget content is displayed) */\n"
"QTabWidget::pane {\n"
"    background-color: white; /* Background color of the co"
                        "ntent area */\n"
"    border: 1px solid gray; /* Border around the content area */\n"
"    margin: 2px; /* Margin around the content area */\n"
"}\n"
"")
        self.parameters_window.setTabPosition(QTabWidget.North)
        self.parameters_window.setTabShape(QTabWidget.Rounded)
        self.parameters_window.setIconSize(QSize(24, 24))
        self.parameters_windowPage_2 = QWidget()
        self.parameters_windowPage_2.setObjectName(u"parameters_windowPage_2")
        self.verticalLayout_36 = QVBoxLayout(self.parameters_windowPage_2)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.frame_17 = QFrame(self.parameters_windowPage_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_17)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.frame_17)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout_8.addWidget(self.label, 0, Qt.AlignHCenter)

        self.RepeatFrame = QFrame(self.frame_17)
        self.RepeatFrame.setObjectName(u"RepeatFrame")
        self.horizontalLayout_27 = QHBoxLayout(self.RepeatFrame)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_44)

        self.repeat_words_label = QLabel(self.RepeatFrame)
        self.repeat_words_label.setObjectName(u"repeat_words_label")
        self.repeat_words_label.setMaximumSize(QSize(150, 16777215))
        self.repeat_words_label.setFont(font)

        self.horizontalLayout_27.addWidget(self.repeat_words_label)

        self.repeat_checkbox = QRadioButton(self.RepeatFrame)
        self.repeat_checkbox.setObjectName(u"repeat_checkbox")
        self.repeat_checkbox.setMinimumSize(QSize(50, 0))
        self.repeat_checkbox.setMaximumSize(QSize(50, 20))
        self.repeat_checkbox.setSizeIncrement(QSize(0, 0))
        self.repeat_checkbox.setBaseSize(QSize(0, 0))
        self.repeat_checkbox.setFont(font)
        self.repeat_checkbox.setIconSize(QSize(24, 24))
        self.repeat_checkbox.setCheckable(True)
        self.repeat_checkbox.setChecked(True)
        self.repeat_checkbox.setAutoRepeat(False)

        self.horizontalLayout_27.addWidget(self.repeat_checkbox)

        self.horizontalSpacer_45 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_45)


        self.verticalLayout_8.addWidget(self.RepeatFrame)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_16)


        self.verticalLayout_36.addWidget(self.frame_17, 0, Qt.AlignHCenter)

        self.parameters_window.addTab(self.parameters_windowPage_2, "")
        self.parameters_windowPage = QWidget()
        self.parameters_windowPage.setObjectName(u"parameters_windowPage")
        self.verticalLayout_16 = QVBoxLayout(self.parameters_windowPage)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_29 = QFrame(self.parameters_windowPage)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(0, 0))
        self.frame_29.setStyleSheet(u"")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_29)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_19 = QLabel(self.frame_29)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)

        self.verticalLayout_37.addWidget(self.label_19, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.min_font_size_label = QLabel(self.frame_29)
        self.min_font_size_label.setObjectName(u"min_font_size_label")
        self.min_font_size_label.setMaximumSize(QSize(150, 100))
        self.min_font_size_label.setFont(font)

        self.horizontalLayout_28.addWidget(self.min_font_size_label)

        self.min_font_size_slider = QSlider(self.frame_29)
        self.min_font_size_slider.setObjectName(u"min_font_size_slider")
        self.min_font_size_slider.setEnabled(True)
        self.min_font_size_slider.setMinimumSize(QSize(30, 0))
        self.min_font_size_slider.setMaximumSize(QSize(30, 16777215))
        self.min_font_size_slider.setSizeIncrement(QSize(10, 0))
        self.min_font_size_slider.setFont(font)
        self.min_font_size_slider.setMouseTracking(True)
        self.min_font_size_slider.setFocusPolicy(Qt.ClickFocus)
        self.min_font_size_slider.setStyleSheet(u"")
        self.min_font_size_slider.setMinimum(1)
        self.min_font_size_slider.setMaximum(100)
        self.min_font_size_slider.setPageStep(1)
        self.min_font_size_slider.setValue(1)
        self.min_font_size_slider.setOrientation(Qt.Vertical)

        self.horizontalLayout_28.addWidget(self.min_font_size_slider)

        self.label_min_font_size_slider = QLabel(self.frame_29)
        self.label_min_font_size_slider.setObjectName(u"label_min_font_size_slider")
        self.label_min_font_size_slider.setMinimumSize(QSize(50, 0))
        self.label_min_font_size_slider.setMaximumSize(QSize(50, 50))
        self.label_min_font_size_slider.setFont(font)

        self.horizontalLayout_28.addWidget(self.label_min_font_size_slider)

        self.MinFSp_Frame_3 = QFrame(self.frame_29)
        self.MinFSp_Frame_3.setObjectName(u"MinFSp_Frame_3")
        self.MinFSp_Frame_3.setMinimumSize(QSize(52, 140))
        self.MinFSp_Frame_3.setMaximumSize(QSize(52, 16777215))
        self.MinFSp_Frame_3.setFont(font)
        self.MinFSp_Frame_3.setAutoFillBackground(False)
        self.MinFSp_Frame_3.setStyleSheet(u"QWidget{\n"
"/* background-color:#F1F1F1;*/\n"
"}\n"
"QPushButton{\n"
"background-color:#333333;\n"
"color:#FFFFFF;\n"
"}\n"
"QPushButton:pressed{\n"
"	 padding-left: 3px;\n"
"     padding-top: 3px;\n"
"}")
        self.MinFSp_Frame_3.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_38 = QVBoxLayout(self.MinFSp_Frame_3)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.MinFSp49 = QPushButton(self.MinFSp_Frame_3)
        self.fontSizePresetsGroup = QButtonGroup(MainWindow)
        self.fontSizePresetsGroup.setObjectName(u"fontSizePresetsGroup")
        self.fontSizePresetsGroup.addButton(self.MinFSp49)
        self.MinFSp49.setObjectName(u"MinFSp49")
        self.MinFSp49.setMaximumSize(QSize(30, 30))

        self.verticalLayout_38.addWidget(self.MinFSp49)

        self.MinFSp31 = QPushButton(self.MinFSp_Frame_3)
        self.fontSizePresetsGroup.addButton(self.MinFSp31)
        self.MinFSp31.setObjectName(u"MinFSp31")
        self.MinFSp31.setMaximumSize(QSize(30, 30))

        self.verticalLayout_38.addWidget(self.MinFSp31)

        self.MinFSp21 = QPushButton(self.MinFSp_Frame_3)
        self.fontSizePresetsGroup.addButton(self.MinFSp21)
        self.MinFSp21.setObjectName(u"MinFSp21")
        self.MinFSp21.setMaximumSize(QSize(30, 30))

        self.verticalLayout_38.addWidget(self.MinFSp21)

        self.MinFSp10 = QPushButton(self.MinFSp_Frame_3)
        self.fontSizePresetsGroup.addButton(self.MinFSp10)
        self.MinFSp10.setObjectName(u"MinFSp10")
        self.MinFSp10.setMaximumSize(QSize(30, 30))

        self.verticalLayout_38.addWidget(self.MinFSp10)


        self.horizontalLayout_28.addWidget(self.MinFSp_Frame_3)


        self.verticalLayout_37.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.max_font_size_label = QLabel(self.frame_29)
        self.max_font_size_label.setObjectName(u"max_font_size_label")
        self.max_font_size_label.setMaximumSize(QSize(150, 100))
        self.max_font_size_label.setFont(font)

        self.horizontalLayout_4.addWidget(self.max_font_size_label)

        self.max_font_size_slider = QSlider(self.frame_29)
        self.max_font_size_slider.setObjectName(u"max_font_size_slider")
        self.max_font_size_slider.setEnabled(True)
        self.max_font_size_slider.setMinimumSize(QSize(30, 0))
        self.max_font_size_slider.setMaximumSize(QSize(30, 16777215))
        self.max_font_size_slider.setSizeIncrement(QSize(10, 0))
        self.max_font_size_slider.setFont(font)
        self.max_font_size_slider.setMouseTracking(True)
        self.max_font_size_slider.setFocusPolicy(Qt.ClickFocus)
        self.max_font_size_slider.setStyleSheet(u"")
        self.max_font_size_slider.setMinimum(5)
        self.max_font_size_slider.setMaximum(300)
        self.max_font_size_slider.setPageStep(1)
        self.max_font_size_slider.setValue(82)
        self.max_font_size_slider.setOrientation(Qt.Vertical)

        self.horizontalLayout_4.addWidget(self.max_font_size_slider)

        self.label_max_font_size_slider = QLabel(self.frame_29)
        self.label_max_font_size_slider.setObjectName(u"label_max_font_size_slider")
        self.label_max_font_size_slider.setMinimumSize(QSize(50, 0))
        self.label_max_font_size_slider.setMaximumSize(QSize(50, 50))
        self.label_max_font_size_slider.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_max_font_size_slider)

        self.MaxFSp_Frame = QFrame(self.frame_29)
        self.MaxFSp_Frame.setObjectName(u"MaxFSp_Frame")
        self.MaxFSp_Frame.setMinimumSize(QSize(52, 140))
        self.MaxFSp_Frame.setStyleSheet(u"QWidget{\n"
"/* background-color:#F1F1F1;*/\n"
"}\n"
"QPushButton{\n"
"background-color:#333333;\n"
"color:#FFFFFF;\n"
"}\n"
"QPushButton:pressed{\n"
"	 padding-left: 3px;\n"
"     padding-top: 3px;\n"
"}")
        self.MaxFSp_Frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_39 = QVBoxLayout(self.MaxFSp_Frame)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.MaxFSp250 = QPushButton(self.MaxFSp_Frame)
        self.fontSizePresetsGroup.addButton(self.MaxFSp250)
        self.MaxFSp250.setObjectName(u"MaxFSp250")
        self.MaxFSp250.setMaximumSize(QSize(30, 30))

        self.verticalLayout_39.addWidget(self.MaxFSp250)

        self.MaxFSp150 = QPushButton(self.MaxFSp_Frame)
        self.fontSizePresetsGroup.addButton(self.MaxFSp150)
        self.MaxFSp150.setObjectName(u"MaxFSp150")
        self.MaxFSp150.setMaximumSize(QSize(30, 30))

        self.verticalLayout_39.addWidget(self.MaxFSp150)

        self.MaxFSp73 = QPushButton(self.MaxFSp_Frame)
        self.fontSizePresetsGroup.addButton(self.MaxFSp73)
        self.MaxFSp73.setObjectName(u"MaxFSp73")
        self.MaxFSp73.setMaximumSize(QSize(30, 30))

        self.verticalLayout_39.addWidget(self.MaxFSp73)

        self.MaxFSp50 = QPushButton(self.MaxFSp_Frame)
        self.fontSizePresetsGroup.addButton(self.MaxFSp50)
        self.MaxFSp50.setObjectName(u"MaxFSp50")
        self.MaxFSp50.setMaximumSize(QSize(30, 30))

        self.verticalLayout_39.addWidget(self.MaxFSp50)


        self.horizontalLayout_4.addWidget(self.MaxFSp_Frame)


        self.verticalLayout_37.addLayout(self.horizontalLayout_4)


        self.verticalLayout_16.addWidget(self.frame_29, 0, Qt.AlignHCenter)

        self.parameters_window.addTab(self.parameters_windowPage, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_40 = QVBoxLayout(self.tab_5)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.frame_font_step = QFrame(self.tab_5)
        self.frame_font_step.setObjectName(u"frame_font_step")
        self.gridLayout_9 = QGridLayout(self.frame_font_step)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_2 = QLabel(self.frame_font_step)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_9.addWidget(self.label_2, 0, 1, 1, 1)

        self.frame_30 = QFrame(self.frame_font_step)
        self.frame_30.setObjectName(u"frame_30")
        self.horizontalLayout_30 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_46)

        self.fontstep_label = QLabel(self.frame_30)
        self.fontstep_label.setObjectName(u"fontstep_label")
        self.fontstep_label.setMaximumSize(QSize(16777215, 50))
        self.fontstep_label.setFont(font)

        self.horizontalLayout_30.addWidget(self.fontstep_label)

        self.font_step_slider = QSlider(self.frame_30)
        self.font_step_slider.setObjectName(u"font_step_slider")
        self.font_step_slider.setMinimumSize(QSize(30, 150))
        self.font_step_slider.setMaximumSize(QSize(30, 150))
        self.font_step_slider.setMinimum(1)
        self.font_step_slider.setMaximum(10)
        self.font_step_slider.setSingleStep(1)
        self.font_step_slider.setPageStep(1)
        self.font_step_slider.setValue(1)
        self.font_step_slider.setOrientation(Qt.Vertical)

        self.horizontalLayout_30.addWidget(self.font_step_slider, 0, Qt.AlignHCenter)

        self.font_step_indicator_label = QLabel(self.frame_30)
        self.font_step_indicator_label.setObjectName(u"font_step_indicator_label")
        self.font_step_indicator_label.setMinimumSize(QSize(50, 0))
        self.font_step_indicator_label.setMaximumSize(QSize(50, 50))
        self.font_step_indicator_label.setFont(font)

        self.horizontalLayout_30.addWidget(self.font_step_indicator_label, 0, Qt.AlignHCenter)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_47)


        self.gridLayout_9.addWidget(self.frame_30, 1, 1, 1, 1)

        self.horizontalSpacer_48 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_48, 0, 2, 1, 1)

        self.horizontalSpacer_49 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_49, 0, 0, 1, 1)


        self.verticalLayout_40.addWidget(self.frame_font_step)

        self.parameters_window.addTab(self.tab_5, "")
        self.parameters_windowPage3 = QWidget()
        self.parameters_windowPage3.setObjectName(u"parameters_windowPage3")
        self.verticalLayout_41 = QVBoxLayout(self.parameters_windowPage3)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.label_21 = QLabel(self.parameters_windowPage3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(305, 95))
        self.label_21.setFont(font)

        self.verticalLayout_41.addWidget(self.label_21, 0, Qt.AlignHCenter)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_10)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalSpacer_50 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_50)

        self.margin_label = QLabel(self.parameters_windowPage3)
        self.margin_label.setObjectName(u"margin_label")
        self.margin_label.setMaximumSize(QSize(250, 100))
        self.margin_label.setFont(font)
        self.margin_label.setWordWrap(False)
        self.margin_label.setMargin(0)

        self.horizontalLayout_33.addWidget(self.margin_label)

        self.margin_slider = QSlider(self.parameters_windowPage3)
        self.margin_slider.setObjectName(u"margin_slider")
        self.margin_slider.setEnabled(True)
        self.margin_slider.setMinimumSize(QSize(30, 0))
        self.margin_slider.setMaximumSize(QSize(30, 16777215))
        self.margin_slider.setSizeIncrement(QSize(10, 0))
        self.margin_slider.setFont(font)
        self.margin_slider.setMouseTracking(True)
        self.margin_slider.setFocusPolicy(Qt.ClickFocus)
        self.margin_slider.setMinimum(0)
        self.margin_slider.setMaximum(30)
        self.margin_slider.setPageStep(1)
        self.margin_slider.setValue(3)
        self.margin_slider.setOrientation(Qt.Vertical)

        self.horizontalLayout_33.addWidget(self.margin_slider)

        self.label_margin_slider = QLabel(self.parameters_windowPage3)
        self.label_margin_slider.setObjectName(u"label_margin_slider")
        self.label_margin_slider.setMinimumSize(QSize(50, 0))
        self.label_margin_slider.setMaximumSize(QSize(50, 50))
        self.label_margin_slider.setFont(font)
        self.label_margin_slider.setMargin(0)

        self.horizontalLayout_33.addWidget(self.label_margin_slider)

        self.horizontalSpacer_51 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_51)


        self.verticalLayout_41.addLayout(self.horizontalLayout_33)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_11)

        self.parameters_window.addTab(self.parameters_windowPage3, "")
        self.parameters_windowPage4 = QWidget()
        self.parameters_windowPage4.setObjectName(u"parameters_windowPage4")
        self.verticalLayout_42 = QVBoxLayout(self.parameters_windowPage4)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.frame_31 = QFrame(self.parameters_windowPage4)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_31)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_22 = QLabel(self.frame_31)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)

        self.verticalLayout_43.addWidget(self.label_22, 0, Qt.AlignHCenter)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_43.addItem(self.verticalSpacer_17)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalSpacer_52 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_52)

        self.prefer_horizontal_label = QLabel(self.frame_31)
        self.prefer_horizontal_label.setObjectName(u"prefer_horizontal_label")
        self.prefer_horizontal_label.setMaximumSize(QSize(250, 100))
        self.prefer_horizontal_label.setFont(font)

        self.horizontalLayout_34.addWidget(self.prefer_horizontal_label)

        self.prefer_horizontal_slider = QSlider(self.frame_31)
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
        self.prefer_horizontal_slider.setValue(10)
        self.prefer_horizontal_slider.setOrientation(Qt.Vertical)

        self.horizontalLayout_34.addWidget(self.prefer_horizontal_slider)

        self.label_text_orientation_slider = QLabel(self.frame_31)
        self.label_text_orientation_slider.setObjectName(u"label_text_orientation_slider")
        self.label_text_orientation_slider.setMinimumSize(QSize(50, 0))
        self.label_text_orientation_slider.setMaximumSize(QSize(50, 50))
        self.label_text_orientation_slider.setFont(font)

        self.horizontalLayout_34.addWidget(self.label_text_orientation_slider)

        self.horizontalSpacer_53 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_53)


        self.verticalLayout_43.addLayout(self.horizontalLayout_34)

        self.verticalSpacer_28 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_43.addItem(self.verticalSpacer_28)


        self.verticalLayout_42.addWidget(self.frame_31)

        self.parameters_window.addTab(self.parameters_windowPage4, "")
        self.parameters_windowPage5 = QWidget()
        self.parameters_windowPage5.setObjectName(u"parameters_windowPage5")
        self.verticalLayout_44 = QVBoxLayout(self.parameters_windowPage5)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.frame_32 = QFrame(self.parameters_windowPage5)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_32)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalSpacer_54 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_54)

        self.image_scale_label = QLabel(self.frame_32)
        self.image_scale_label.setObjectName(u"image_scale_label")
        self.image_scale_label.setMaximumSize(QSize(16777215, 30))
        self.image_scale_label.setFont(font)

        self.horizontalLayout_35.addWidget(self.image_scale_label)

        self.scale_slider = QSlider(self.frame_32)
        self.scale_slider.setObjectName(u"scale_slider")
        self.scale_slider.setMinimumSize(QSize(0, 40))
        self.scale_slider.setMaximumSize(QSize(300, 16777215))
        self.scale_slider.setMinimum(1)
        self.scale_slider.setMaximum(10)
        self.scale_slider.setPageStep(1)
        self.scale_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_35.addWidget(self.scale_slider)

        self.label_scale_slider = QLabel(self.frame_32)
        self.label_scale_slider.setObjectName(u"label_scale_slider")
        self.label_scale_slider.setMaximumSize(QSize(50, 50))
        self.label_scale_slider.setFont(font)
        self.label_scale_slider.setMargin(5)
        self.label_scale_slider.setIndent(-1)
        self.label_scale_slider.setOpenExternalLinks(False)

        self.horizontalLayout_35.addWidget(self.label_scale_slider)

        self.horizontalSpacer_55 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_55)


        self.gridLayout_21.addLayout(self.horizontalLayout_35, 2, 0, 1, 1)

        self.verticalSpacer_29 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_21.addItem(self.verticalSpacer_29, 3, 0, 1, 1)

        self.label_23 = QLabel(self.frame_32)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)

        self.gridLayout_21.addWidget(self.label_23, 0, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_30 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_21.addItem(self.verticalSpacer_30, 1, 0, 1, 1)


        self.verticalLayout_44.addWidget(self.frame_32)

        self.parameters_window.addTab(self.parameters_windowPage5, "")
        self.parameters_windowPage6 = QWidget()
        self.parameters_windowPage6.setObjectName(u"parameters_windowPage6")
        self.verticalLayout_45 = QVBoxLayout(self.parameters_windowPage6)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.frame_33 = QFrame(self.parameters_windowPage6)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setEnabled(True)
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_33)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_24 = QLabel(self.frame_33)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)

        self.gridLayout_22.addWidget(self.label_24, 0, 0, 1, 1, Qt.AlignHCenter)

        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        self.horizontalLayout_45 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalSpacer_56 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_56)

        self.stopwords_label = QLabel(self.frame_34)
        self.stopwords_label.setObjectName(u"stopwords_label")
        self.stopwords_label.setMaximumSize(QSize(150, 30))
        self.stopwords_label.setFont(font)

        self.horizontalLayout_45.addWidget(self.stopwords_label)

        self.stopwords_checkbox = QRadioButton(self.frame_34)
        self.stopwords_checkbox.setObjectName(u"stopwords_checkbox")
        self.stopwords_checkbox.setEnabled(False)
        self.stopwords_checkbox.setMinimumSize(QSize(50, 0))
        self.stopwords_checkbox.setMaximumSize(QSize(50, 20))
        self.stopwords_checkbox.setFont(font)
        self.stopwords_checkbox.setIconSize(QSize(24, 24))
        self.stopwords_checkbox.setCheckable(True)
        self.stopwords_checkbox.setChecked(False)

        self.horizontalLayout_45.addWidget(self.stopwords_checkbox)

        self.horizontalSpacer_57 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_57)


        self.gridLayout_22.addWidget(self.frame_34, 2, 0, 1, 1)

        self.verticalSpacer_31 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_22.addItem(self.verticalSpacer_31, 3, 0, 1, 1)

        self.verticalSpacer_32 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_22.addItem(self.verticalSpacer_32, 1, 0, 1, 1)


        self.verticalLayout_45.addWidget(self.frame_33)

        self.parameters_window.addTab(self.parameters_windowPage6, "")
        self.parameters_windowPage8 = QWidget()
        self.parameters_windowPage8.setObjectName(u"parameters_windowPage8")
        self.verticalLayout_46 = QVBoxLayout(self.parameters_windowPage8)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.frame_35 = QFrame(self.parameters_windowPage8)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_35)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.frame_36 = QFrame(self.frame_35)
        self.frame_36.setObjectName(u"frame_36")
        self.horizontalLayout_46 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalSpacer_58 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_58)

        self.label_collocations_thresh = QLabel(self.frame_36)
        self.label_collocations_thresh.setObjectName(u"label_collocations_thresh")
        self.label_collocations_thresh.setFont(font)

        self.horizontalLayout_46.addWidget(self.label_collocations_thresh)

        self.collocations_thresh_slider = QSlider(self.frame_36)
        self.collocations_thresh_slider.setObjectName(u"collocations_thresh_slider")
        self.collocations_thresh_slider.setEnabled(True)
        self.collocations_thresh_slider.setMinimumSize(QSize(30, 0))
        self.collocations_thresh_slider.setMaximumSize(QSize(30, 16777215))
        self.collocations_thresh_slider.setMinimum(0)
        self.collocations_thresh_slider.setMaximum(100)
        self.collocations_thresh_slider.setPageStep(1)
        self.collocations_thresh_slider.setOrientation(Qt.Vertical)

        self.horizontalLayout_46.addWidget(self.collocations_thresh_slider)

        self.collocation_thresh_slider_label = QLabel(self.frame_36)
        self.collocation_thresh_slider_label.setObjectName(u"collocation_thresh_slider_label")
        self.collocation_thresh_slider_label.setMaximumSize(QSize(50, 50))
        self.collocation_thresh_slider_label.setFont(font)

        self.horizontalLayout_46.addWidget(self.collocation_thresh_slider_label)

        self.horizontalSpacer_59 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_59)


        self.gridLayout_23.addWidget(self.frame_36, 2, 0, 1, 1)

        self.label_25 = QLabel(self.frame_35)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font)

        self.gridLayout_23.addWidget(self.label_25, 1, 0, 1, 1, Qt.AlignHCenter)

        self.frame_37 = QFrame(self.frame_35)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_37)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.label_26 = QLabel(self.frame_37)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font)

        self.verticalLayout_47.addWidget(self.label_26, 0, Qt.AlignHCenter)

        self.verticalSpacer_33 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_47.addItem(self.verticalSpacer_33)

        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.horizontalLayout_47 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalSpacer_60 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_60)

        self.label_collocations = QLabel(self.frame_38)
        self.label_collocations.setObjectName(u"label_collocations")
        self.label_collocations.setFont(font)

        self.horizontalLayout_47.addWidget(self.label_collocations)

        self.collocations_checkbox = QCheckBox(self.frame_38)
        self.collocations_checkbox.setObjectName(u"collocations_checkbox")
        self.collocations_checkbox.setFont(font)
        self.collocations_checkbox.setChecked(False)
        self.collocations_checkbox.setTristate(False)

        self.horizontalLayout_47.addWidget(self.collocations_checkbox)

        self.horizontalSpacer_61 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_61)


        self.verticalLayout_47.addWidget(self.frame_38)


        self.gridLayout_23.addWidget(self.frame_37, 0, 0, 1, 1)


        self.verticalLayout_46.addWidget(self.frame_35)

        self.parameters_window.addTab(self.parameters_windowPage8, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.frame_39 = QFrame(self.tab_6)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setGeometry(QRect(0, 10, 531, 361))
        self.frame_39.setMinimumSize(QSize(531, 361))
        self.frame_39.setMaximumSize(QSize(531, 361))
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.gridLayout_24 = QGridLayout(self.frame_39)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.verticalSpacer_34 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_24.addItem(self.verticalSpacer_34, 6, 1, 1, 1)

        self.checkBoxFrame_5 = QFrame(self.frame_39)
        self.checkBoxFrame_5.setObjectName(u"checkBoxFrame_5")
        self.gridLayout_25 = QGridLayout(self.checkBoxFrame_5)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.stopwords_label_2 = QLabel(self.checkBoxFrame_5)
        self.stopwords_label_2.setObjectName(u"stopwords_label_2")
        self.stopwords_label_2.setFont(font)

        self.gridLayout_25.addWidget(self.stopwords_label_2, 0, 0, 1, 1)

        self.include_number_checkbox = QRadioButton(self.checkBoxFrame_5)
        self.include_number_checkbox.setObjectName(u"include_number_checkbox")
        self.include_number_checkbox.setMaximumSize(QSize(50, 20))
        self.include_number_checkbox.setFont(font)
        self.include_number_checkbox.setIconSize(QSize(24, 24))
        self.include_number_checkbox.setCheckable(True)
        self.include_number_checkbox.setChecked(True)

        self.gridLayout_25.addWidget(self.include_number_checkbox, 0, 1, 1, 1)


        self.gridLayout_24.addWidget(self.checkBoxFrame_5, 4, 1, 1, 1, Qt.AlignHCenter)

        self.frame_40 = QFrame(self.frame_39)
        self.frame_40.setObjectName(u"frame_40")
        self.gridLayout_26 = QGridLayout(self.frame_40)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.regxp_any_character_label = QLabel(self.frame_40)
        self.regxp_any_character_label.setObjectName(u"regxp_any_character_label")
        self.regxp_any_character_label.setFont(font)

        self.gridLayout_26.addWidget(self.regxp_any_character_label, 0, 0, 1, 1)

        self.regxp_any_character_checkbox = QRadioButton(self.frame_40)
        self.regxp_any_character_checkbox.setObjectName(u"regxp_any_character_checkbox")
        self.regxp_any_character_checkbox.setMinimumSize(QSize(50, 0))
        self.regxp_any_character_checkbox.setMaximumSize(QSize(50, 20))
        self.regxp_any_character_checkbox.setFont(font)
        self.regxp_any_character_checkbox.setIconSize(QSize(24, 24))
        self.regxp_any_character_checkbox.setCheckable(True)
        self.regxp_any_character_checkbox.setChecked(True)

        self.gridLayout_26.addWidget(self.regxp_any_character_checkbox, 0, 1, 1, 1)


        self.gridLayout_24.addWidget(self.frame_40, 2, 1, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_62 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_62, 4, 2, 1, 1)

        self.label_Character_Filtering_Title = QLabel(self.frame_39)
        self.label_Character_Filtering_Title.setObjectName(u"label_Character_Filtering_Title")
        self.label_Character_Filtering_Title.setFont(font)

        self.gridLayout_24.addWidget(self.label_Character_Filtering_Title, 0, 1, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_63 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_63, 4, 0, 1, 1)

        self.checkBoxFrame_6 = QFrame(self.frame_39)
        self.checkBoxFrame_6.setObjectName(u"checkBoxFrame_6")
        self.gridLayout_27 = QGridLayout(self.checkBoxFrame_6)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.connected_punctuation_label = QLabel(self.checkBoxFrame_6)
        self.connected_punctuation_label.setObjectName(u"connected_punctuation_label")
        self.connected_punctuation_label.setFont(font)

        self.gridLayout_27.addWidget(self.connected_punctuation_label, 0, 0, 1, 1)

        self.connected_punctuation_checkbox = QRadioButton(self.checkBoxFrame_6)
        self.connected_punctuation_checkbox.setObjectName(u"connected_punctuation_checkbox")
        self.connected_punctuation_checkbox.setMinimumSize(QSize(50, 0))
        self.connected_punctuation_checkbox.setMaximumSize(QSize(50, 20))
        self.connected_punctuation_checkbox.setFont(font)
        self.connected_punctuation_checkbox.setIconSize(QSize(24, 24))
        self.connected_punctuation_checkbox.setCheckable(True)
        self.connected_punctuation_checkbox.setChecked(False)

        self.gridLayout_27.addWidget(self.connected_punctuation_checkbox, 0, 1, 1, 1)


        self.gridLayout_24.addWidget(self.checkBoxFrame_6, 3, 1, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_35 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_24.addItem(self.verticalSpacer_35, 1, 1, 1, 1)

        self.parameters_window.addTab(self.tab_6, "")

        self.gridLayout_3.addWidget(self.parameters_window, 0, 0, 1, 1)

        self.generated_text_label = QLabel(self.WordInputAndParametersFrame)
        self.generated_text_label.setObjectName(u"generated_text_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.generated_text_label.sizePolicy().hasHeightForWidth())
        self.generated_text_label.setSizePolicy(sizePolicy4)
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setItalic(False)
        self.generated_text_label.setFont(font1)

        self.gridLayout_3.addWidget(self.generated_text_label, 1, 0, 1, 1)

        self.fonts_Frame = QFrame(self.WordInputAndParametersFrame)
        self.fonts_Frame.setObjectName(u"fonts_Frame")
        sizePolicy4.setHeightForWidth(self.fonts_Frame.sizePolicy().hasHeightForWidth())
        self.fonts_Frame.setSizePolicy(sizePolicy4)
        self.verticalLayout_3 = QVBoxLayout(self.fonts_Frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.font_selection_buttonsFrame = QFrame(self.fonts_Frame)
        self.font_selection_buttonsFrame.setObjectName(u"font_selection_buttonsFrame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.font_selection_buttonsFrame.sizePolicy().hasHeightForWidth())
        self.font_selection_buttonsFrame.setSizePolicy(sizePolicy5)
        self.horizontalLayout_7 = QHBoxLayout(self.font_selection_buttonsFrame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.load_system_fonts_btn = QPushButton(self.font_selection_buttonsFrame)
        self.load_system_fonts_btn.setObjectName(u"load_system_fonts_btn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.load_system_fonts_btn.sizePolicy().hasHeightForWidth())
        self.load_system_fonts_btn.setSizePolicy(sizePolicy6)
        self.load_system_fonts_btn.setMinimumSize(QSize(121, 30))
        self.load_system_fonts_btn.setFont(font1)
        self.load_system_fonts_btn.setStyleSheet(u"QPushButton{\n"
"background-color:#212121;\n"
"color:#e6e6e6;\n"
"}")

        self.horizontalLayout_7.addWidget(self.load_system_fonts_btn)

        self.custom_font_directory_selection = QPushButton(self.font_selection_buttonsFrame)
        self.custom_font_directory_selection.setObjectName(u"custom_font_directory_selection")
        sizePolicy6.setHeightForWidth(self.custom_font_directory_selection.sizePolicy().hasHeightForWidth())
        self.custom_font_directory_selection.setSizePolicy(sizePolicy6)
        self.custom_font_directory_selection.setMinimumSize(QSize(134, 30))
        self.custom_font_directory_selection.setFont(font1)
        self.custom_font_directory_selection.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.custom_font_directory_selection)

        self.load_emoji_fonts_btn = QPushButton(self.font_selection_buttonsFrame)
        self.load_emoji_fonts_btn.setObjectName(u"load_emoji_fonts_btn")
        sizePolicy6.setHeightForWidth(self.load_emoji_fonts_btn.sizePolicy().hasHeightForWidth())
        self.load_emoji_fonts_btn.setSizePolicy(sizePolicy6)
        self.load_emoji_fonts_btn.setMinimumSize(QSize(107, 30))
        self.load_emoji_fonts_btn.setFont(font1)
        self.load_emoji_fonts_btn.setStyleSheet(u"QPushButton{\n"
"background-color:#212121;\n"
"color:#e6e6e6;\n"
"}")

        self.horizontalLayout_7.addWidget(self.load_emoji_fonts_btn)


        self.verticalLayout_3.addWidget(self.font_selection_buttonsFrame)

        self.font_list = QListWidget(self.fonts_Frame)
        self.font_list.setObjectName(u"font_list")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.font_list.sizePolicy().hasHeightForWidth())
        self.font_list.setSizePolicy(sizePolicy7)
        self.font_list.setMinimumSize(QSize(0, 500))
        font2 = QFont()
        font2.setFamilies([u"Inter"])
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setItalic(False)
        self.font_list.setFont(font2)
        self.font_list.setStyleSheet(u"QListWidget{\n"
"border:2px solid gray;\n"
"color: #141414;\n"
"}")
        self.font_list.setAutoScrollMargin(20)
        self.font_list.setTabKeyNavigation(False)

        self.verticalLayout_3.addWidget(self.font_list)


        self.gridLayout_3.addWidget(self.fonts_Frame, 0, 1, 1, 1)

        self.word_input = QTextEdit(self.WordInputAndParametersFrame)
        self.word_input.setObjectName(u"word_input")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.word_input.sizePolicy().hasHeightForWidth())
        self.word_input.setSizePolicy(sizePolicy8)
        font3 = QFont()
        font3.setFamilies([u"Inter"])
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setItalic(False)
        self.word_input.setFont(font3)
        self.word_input.setStyleSheet(u"QTextEdit{\n"
"/*border:2px solid red;*/\n"
"color:#141414;\n"
"}")
        self.word_input.setFrameShadow(QFrame.Plain)
        self.word_input.setLineWidth(1)
        self.word_input.setTabChangesFocus(False)
        self.word_input.setUndoRedoEnabled(True)

        self.gridLayout_3.addWidget(self.word_input, 2, 0, 1, 2)


        self.gridLayout_11.addWidget(self.WordInputAndParametersFrame, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.TitleFrame, 0, 1, 1, 1)

        self.WC_GeneratorFrame = QFrame(self.centralwidget)
        self.WC_GeneratorFrame.setObjectName(u"WC_GeneratorFrame")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.WC_GeneratorFrame.sizePolicy().hasHeightForWidth())
        self.WC_GeneratorFrame.setSizePolicy(sizePolicy9)
        self.WC_GeneratorFrame.setMinimumSize(QSize(0, 300))
        self.horizontalLayout = QHBoxLayout(self.WC_GeneratorFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.file_handling_frame = QFrame(self.WC_GeneratorFrame)
        self.file_handling_frame.setObjectName(u"file_handling_frame")
        sizePolicy10 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.file_handling_frame.sizePolicy().hasHeightForWidth())
        self.file_handling_frame.setSizePolicy(sizePolicy10)
        self.gridLayout_12 = QGridLayout(self.file_handling_frame)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_18, 0, 0, 1, 1)

        self.stash_last_generated_button = QPushButton(self.file_handling_frame)
        self.stash_last_generated_button.setObjectName(u"stash_last_generated_button")
        self.stash_last_generated_button.setMinimumSize(QSize(40, 40))
        self.stash_last_generated_button.setMaximumSize(QSize(40, 40))
        self.stash_last_generated_button.setFont(font1)
        self.stash_last_generated_button.setStyleSheet(u"QPushButton {\n"
"    background-color: green; /* or any other color you want */\n"
"}\n"
"QPushButton:pressed{\n"
"	 padding-left: 3px;\n"
"     padding-top: 3px;\n"
"}")

        self.gridLayout_12.addWidget(self.stash_last_generated_button, 2, 0, 1, 1)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_19, 3, 0, 1, 1)

        self.delete_last_generated_button = QPushButton(self.file_handling_frame)
        self.delete_last_generated_button.setObjectName(u"delete_last_generated_button")
        self.delete_last_generated_button.setMinimumSize(QSize(40, 40))
        self.delete_last_generated_button.setMaximumSize(QSize(40, 40))
        self.delete_last_generated_button.setFont(font1)
        self.delete_last_generated_button.setStyleSheet(u"QPushButton {\n"
"    background-color: red; /* or any other color you want */\n"
"}\n"
"QPushButton:pressed{\n"
"	 padding-left: 3px;\n"
"     padding-top: 3px;\n"
"}")

        self.gridLayout_12.addWidget(self.delete_last_generated_button, 1, 0, 1, 1)


        self.horizontalLayout.addWidget(self.file_handling_frame)

        self.btnContainerFrame = QFrame(self.WC_GeneratorFrame)
        self.btnContainerFrame.setObjectName(u"btnContainerFrame")
        sizePolicy2.setHeightForWidth(self.btnContainerFrame.sizePolicy().hasHeightForWidth())
        self.btnContainerFrame.setSizePolicy(sizePolicy2)
        self.verticalLayout_2 = QVBoxLayout(self.btnContainerFrame)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 0, 10)
        self.export_as_frame = QGroupBox(self.btnContainerFrame)
        self.export_as_frame.setObjectName(u"export_as_frame")
        sizePolicy2.setHeightForWidth(self.export_as_frame.sizePolicy().hasHeightForWidth())
        self.export_as_frame.setSizePolicy(sizePolicy2)
        self.export_as_frame.setMinimumSize(QSize(100, 75))
        self.export_as_frame.setFont(font1)
        self.export_as_frame.setFlat(True)
        self.verticalLayout_26 = QVBoxLayout(self.export_as_frame)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(-1, 0, 0, 10)
        self.exportAs_label = QLabel(self.export_as_frame)
        self.exportAs_label.setObjectName(u"exportAs_label")
        sizePolicy5.setHeightForWidth(self.exportAs_label.sizePolicy().hasHeightForWidth())
        self.exportAs_label.setSizePolicy(sizePolicy5)
        self.exportAs_label.setFont(font1)

        self.verticalLayout_26.addWidget(self.exportAs_label, 0, Qt.AlignHCenter)

        self.export_format_options = QComboBox(self.export_as_frame)
        self.export_format_options.addItem("")
        self.export_format_options.addItem("")
        self.export_format_options.addItem("")
        self.export_format_options.setObjectName(u"export_format_options")
        sizePolicy11 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.export_format_options.sizePolicy().hasHeightForWidth())
        self.export_format_options.setSizePolicy(sizePolicy11)
        self.export_format_options.setFont(font1)
        self.export_format_options.setStyleSheet(u"/* Style the QComboBox */\n"
"QComboBox {\n"
"    background-color: #141414; /* Background color of the entire combo box */\n"
"    border: 1px solid #e6e6e6; /* Border around the combo box */\n"
"    padding: 10px; /* Padding inside the combo box */\n"
"    color:#e6e6e6; /* Current text color*/\n"
"}\n"
"/* Style the QComboBox's drop-down list */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #141414; /* Background color of the drop-down list */\n"
"    border: 1px solid #e6e6e6; /* Border around the drop-down list */\n"
"    padding: 10px; /* Padding inside the drop-down list */\n"
"	color:#e6e6e6;\n"
"}\n"
"/* Style individual items within the QComboBox's drop-down list */\n"
"QComboBox QAbstractItemView::item {\n"
"    background-color: #141414; /* Background color of each item in the list */\n"
"    padding: 1px; /* Padding inside each item */\n"
"	color: #e6e6e6;\n"
"}\n"
"/* Style the selected item within the drop-down list */\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    backgr"
                        "ound-color: rgba(0,200,0,200); /* Background color of the selected item */\n"
"    color: #e6e6e6; /* Text color of the selected item */\n"
"}\n"
"/* Style the drop-down list scroll bar (if it appears) */\n"
"QComboBox QScrollBar:vertical {\n"
"    width: 0px; /* Width of the vertical scrollbar */\n"
"    background: #e6e6e6; /* Background color of the scrollbar */\n"
"}\n"
"/* Style the drop-down list scroll bar handle (thumb) */\n"
"QComboBox QScrollBar::handle:vertical {\n"
"    background: #141414; /* Background color of the scrollbar handle */\n"
"}")
        self.export_format_options.setDuplicatesEnabled(False)
        self.export_format_options.setFrame(True)

        self.verticalLayout_26.addWidget(self.export_format_options, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.export_as_frame, 0, Qt.AlignHCenter)

        self.generate_wordcloud_button = QPushButton(self.btnContainerFrame)
        self.generate_wordcloud_button.setObjectName(u"generate_wordcloud_button")
        self.generate_wordcloud_button.setEnabled(True)
        sizePolicy12 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.generate_wordcloud_button.sizePolicy().hasHeightForWidth())
        self.generate_wordcloud_button.setSizePolicy(sizePolicy12)
        self.generate_wordcloud_button.setMinimumSize(QSize(300, 150))
        self.generate_wordcloud_button.setFont(font1)
        self.generate_wordcloud_button.setToolTipDuration(-1)
        self.generate_wordcloud_button.setStyleSheet(u"QPushButton{\n"
"color: rgb(200,200,200);\n"
"background-color: rgb(50, 50, 50);\n"
"border: 10px solid green;\n"
"border-radius: 50px;\n"
"padding: 50px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:green;\n"
"border: 10px solid rgb(50, 50, 50);\n"
"padding-left: 50px;\n"
"padding-bottom:20px\n"
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

        self.verticalLayout_2.addWidget(self.generate_wordcloud_button)


        self.horizontalLayout.addWidget(self.btnContainerFrame)


        self.gridLayout.addWidget(self.WC_GeneratorFrame, 1, 1, 1, 1)

        self.SummaryFrame = QFrame(self.centralwidget)
        self.SummaryFrame.setObjectName(u"SummaryFrame")
        self.SummaryFrame.setMinimumSize(QSize(301, 401))
        self.SummaryFrame.setFont(font1)
        self.SummaryFrame.setStyleSheet(u"QFrame{\n"
"background-color:rgba(200,0,200,50);\n"
"}\n"
"QFrame QLabel{\n"
"font: 700 10pt \"Inter\";\n"
"background:none;\n"
"color:white;\n"
"}")
        self.SummaryFrame.setFrameShape(QFrame.StyledPanel)
        self.SummaryFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.SummaryFrame)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.parameters_summary_label_2 = QLabel(self.SummaryFrame)
        self.parameters_summary_label_2.setObjectName(u"parameters_summary_label_2")
        self.parameters_summary_label_2.setStyleSheet(u"font: 700 14pt \"Inter\";")
        self.parameters_summary_label_2.setWordWrap(False)
        self.parameters_summary_label_2.setMargin(0)
        self.parameters_summary_label_2.setIndent(-1)
        self.parameters_summary_label_2.setOpenExternalLinks(False)

        self.verticalLayout_32.addWidget(self.parameters_summary_label_2, 0, Qt.AlignHCenter)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.repeatWords_btn = QPushButton(self.SummaryFrame)
        self.parametersButtonGroup = QButtonGroup(MainWindow)
        self.parametersButtonGroup.setObjectName(u"parametersButtonGroup")
        self.parametersButtonGroup.addButton(self.repeatWords_btn)
        self.repeatWords_btn.setObjectName(u"repeatWords_btn")
        font4 = QFont()
        font4.setFamilies([u"Inter"])
        font4.setBold(True)
        self.repeatWords_btn.setFont(font4)
        self.repeatWords_btn.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:#e6e6e6;")

        self.horizontalLayout_19.addWidget(self.repeatWords_btn)

        self.repeat_info_label = QLabel(self.SummaryFrame)
        self.repeat_info_label.setObjectName(u"repeat_info_label")
        font5 = QFont()
        font5.setFamilies([u"Inter"])
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setItalic(False)
        self.repeat_info_label.setFont(font5)

        self.horizontalLayout_19.addWidget(self.repeat_info_label)


        self.verticalLayout_32.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.marginSettings_btn = QPushButton(self.SummaryFrame)
        self.parametersButtonGroup.addButton(self.marginSettings_btn)
        self.marginSettings_btn.setObjectName(u"marginSettings_btn")
        self.marginSettings_btn.setFont(font4)
        self.marginSettings_btn.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:#e6e6e6;")

        self.horizontalLayout_36.addWidget(self.marginSettings_btn)

        self.margin_info_label = QLabel(self.SummaryFrame)
        self.margin_info_label.setObjectName(u"margin_info_label")
        self.margin_info_label.setFont(font5)

        self.horizontalLayout_36.addWidget(self.margin_info_label)


        self.verticalLayout_32.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.fontSizeSettings_btn = QPushButton(self.SummaryFrame)
        self.parametersButtonGroup.addButton(self.fontSizeSettings_btn)
        self.fontSizeSettings_btn.setObjectName(u"fontSizeSettings_btn")
        self.fontSizeSettings_btn.setFont(font4)
        self.fontSizeSettings_btn.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:#e6e6e6;")

        self.horizontalLayout_37.addWidget(self.fontSizeSettings_btn)

        self.min_font_size_info_label = QLabel(self.SummaryFrame)
        self.min_font_size_info_label.setObjectName(u"min_font_size_info_label")
        self.min_font_size_info_label.setFont(font5)

        self.horizontalLayout_37.addWidget(self.min_font_size_info_label)


        self.verticalLayout_32.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.fontSizeSettings_btn2 = QPushButton(self.SummaryFrame)
        self.parametersButtonGroup.addButton(self.fontSizeSettings_btn2)
        self.fontSizeSettings_btn2.setObjectName(u"fontSizeSettings_btn2")
        self.fontSizeSettings_btn2.setFont(font4)
        self.fontSizeSettings_btn2.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:#e6e6e6;")

        self.horizontalLayout_38.addWidget(self.fontSizeSettings_btn2)

        self.max_font_size_info_label = QLabel(self.SummaryFrame)
        self.max_font_size_info_label.setObjectName(u"max_font_size_info_label")
        self.max_font_size_info_label.setFont(font5)

        self.horizontalLayout_38.addWidget(self.max_font_size_info_label)


        self.verticalLayout_32.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.textOrientationSettings_btn = QPushButton(self.SummaryFrame)
        self.parametersButtonGroup.addButton(self.textOrientationSettings_btn)
        self.textOrientationSettings_btn.setObjectName(u"textOrientationSettings_btn")
        self.textOrientationSettings_btn.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:#e6e6e6;")

        self.horizontalLayout_39.addWidget(self.textOrientationSettings_btn)

        self.prefer_horizontal_info_label = QLabel(self.SummaryFrame)
        self.prefer_horizontal_info_label.setObjectName(u"prefer_horizontal_info_label")
        self.prefer_horizontal_info_label.setFont(font5)

        self.horizontalLayout_39.addWidget(self.prefer_horizontal_info_label)


        self.verticalLayout_32.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.fontStepSettings_btn = QPushButton(self.SummaryFrame)
        self.parametersButtonGroup.addButton(self.fontStepSettings_btn)
        self.fontStepSettings_btn.setObjectName(u"fontStepSettings_btn")
        self.fontStepSettings_btn.setFont(font4)
        self.fontStepSettings_btn.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:#e6e6e6;")

        self.horizontalLayout_40.addWidget(self.fontStepSettings_btn)

        self.fontstep_info_label = QLabel(self.SummaryFrame)
        self.fontstep_info_label.setObjectName(u"fontstep_info_label")
        self.fontstep_info_label.setFont(font5)

        self.horizontalLayout_40.addWidget(self.fontstep_info_label)


        self.verticalLayout_32.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.collocationSettings_btn = QPushButton(self.SummaryFrame)
        self.parametersButtonGroup.addButton(self.collocationSettings_btn)
        self.collocationSettings_btn.setObjectName(u"collocationSettings_btn")
        self.collocationSettings_btn.setFont(font4)
        self.collocationSettings_btn.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:#e6e6e6;")

        self.horizontalLayout_41.addWidget(self.collocationSettings_btn)

        self.collocations_info_label = QLabel(self.SummaryFrame)
        self.collocations_info_label.setObjectName(u"collocations_info_label")
        self.collocations_info_label.setFont(font5)

        self.horizontalLayout_41.addWidget(self.collocations_info_label)


        self.verticalLayout_32.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.collocationSettings_btn2 = QPushButton(self.SummaryFrame)
        self.parametersButtonGroup.addButton(self.collocationSettings_btn2)
        self.collocationSettings_btn2.setObjectName(u"collocationSettings_btn2")
        self.collocationSettings_btn2.setFont(font4)
        self.collocationSettings_btn2.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:#e6e6e6;")

        self.horizontalLayout_42.addWidget(self.collocationSettings_btn2)

        self.collocations_thresh_info_label = QLabel(self.SummaryFrame)
        self.collocations_thresh_info_label.setObjectName(u"collocations_thresh_info_label")
        self.collocations_thresh_info_label.setFont(font5)

        self.horizontalLayout_42.addWidget(self.collocations_thresh_info_label)


        self.verticalLayout_32.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.charInclusion_btn = QPushButton(self.SummaryFrame)
        self.parametersButtonGroup.addButton(self.charInclusion_btn)
        self.charInclusion_btn.setObjectName(u"charInclusion_btn")
        self.charInclusion_btn.setFont(font4)
        self.charInclusion_btn.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:#e6e6e6;")

        self.horizontalLayout_43.addWidget(self.charInclusion_btn)

        self.include_numbers_info_label = QLabel(self.SummaryFrame)
        self.include_numbers_info_label.setObjectName(u"include_numbers_info_label")
        self.include_numbers_info_label.setFont(font5)

        self.horizontalLayout_43.addWidget(self.include_numbers_info_label)


        self.verticalLayout_32.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.scaleSettings_btn = QPushButton(self.SummaryFrame)
        self.parametersButtonGroup.addButton(self.scaleSettings_btn)
        self.scaleSettings_btn.setObjectName(u"scaleSettings_btn")
        self.scaleSettings_btn.setFont(font4)
        self.scaleSettings_btn.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:#e6e6e6;")

        self.horizontalLayout_44.addWidget(self.scaleSettings_btn)

        self.scale_multiplier_info_label = QLabel(self.SummaryFrame)
        self.scale_multiplier_info_label.setObjectName(u"scale_multiplier_info_label")
        self.scale_multiplier_info_label.setFont(font5)

        self.horizontalLayout_44.addWidget(self.scale_multiplier_info_label)


        self.verticalLayout_32.addLayout(self.horizontalLayout_44)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_32.addItem(self.horizontalSpacer_23)

        self.color_presets_group = QFrame(self.SummaryFrame)
        self.color_presets_group.setObjectName(u"color_presets_group")
        sizePolicy4.setHeightForWidth(self.color_presets_group.sizePolicy().hasHeightForWidth())
        self.color_presets_group.setSizePolicy(sizePolicy4)
        self.color_presets_group.setFont(font1)
        self.color_presets_group.setStyleSheet(u"background:none;")
        self.color_presets_group.setFrameShape(QFrame.NoFrame)
        self.color_presets_group.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.color_presets_group)
        self.verticalLayout_18.setSpacing(5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(5, 0, 5, 0)
        self.cp_title_dropdown = QFrame(self.color_presets_group)
        self.cp_title_dropdown.setObjectName(u"cp_title_dropdown")
        sizePolicy12.setHeightForWidth(self.cp_title_dropdown.sizePolicy().hasHeightForWidth())
        self.cp_title_dropdown.setSizePolicy(sizePolicy12)
        self.cp_title_dropdown.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_19 = QVBoxLayout(self.cp_title_dropdown)
        self.verticalLayout_19.setSpacing(15)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 10, 0, 0)
        self.label_color_presets = QLabel(self.cp_title_dropdown)
        self.label_color_presets.setObjectName(u"label_color_presets")
        self.label_color_presets.setMaximumSize(QSize(150, 30))
        self.label_color_presets.setFont(font5)

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
        sizePolicy12.setHeightForWidth(self.colormaps_dropdown.sizePolicy().hasHeightForWidth())
        self.colormaps_dropdown.setSizePolicy(sizePolicy12)
        self.colormaps_dropdown.setMinimumSize(QSize(200, 30))
        self.colormaps_dropdown.setMaximumSize(QSize(250, 40))
        self.colormaps_dropdown.setFont(font1)
        self.colormaps_dropdown.setStyleSheet(u"/* Style the QComboBox */\n"
"QComboBox {\n"
"    background-color: #141414; /* Background color of the entire combo box */\n"
"    border: 1px solid #e6e6e6; /* Border around the combo box */\n"
"    padding: 4px; /* Padding inside the combo box */\n"
"    color:#e6e6e6; /* Current text color*/\n"
"}\n"
"/* Style the QComboBox's drop-down list */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #141414; /* Background color of the drop-down list */\n"
"    border: 1px solid #e6e6e6; /* Border around the drop-down list */\n"
"    padding: 10px; /* Padding inside the drop-down list */\n"
"	color:#e6e6e6;\n"
"}\n"
"\n"
"/* Style individual items within the QComboBox's drop-down list */\n"
"QComboBox QAbstractItemView::item {\n"
"    background-color: #141414; /* Background color of each item in the list */\n"
"    padding: 4px; /* Padding inside each item */\n"
"	color: #e6e6e6;\n"
"}\n"
"\n"
"/* Style the selected item within the drop-down list */\n"
"QComboBox QAbstractItemView::item:selected {\n"
" "
                        "   background-color: rgba(0,200,0,150); /* Background color of the selected item */\n"
"    color: #e6e6e6; /* Text color of the selected item */\n"
"}\n"
"\n"
"/* Style the drop-down list scroll bar (if it appears) */\n"
"QComboBox QScrollBar:vertical {\n"
"    width: 20px; /* Width of the vertical scrollbar */\n"
"    background: #e6e6e6; /* Background color of the scrollbar */\n"
"}\n"
"/* Style the drop-down list scroll bar handle (thumb) */\n"
"QComboBox QScrollBar::handle:vertical {\n"
"    background: #141414; /* Background color of the scrollbar handle */\n"
"    border-radius:5px;\n"
"}")

        self.verticalLayout_19.addWidget(self.colormaps_dropdown)


        self.verticalLayout_18.addWidget(self.cp_title_dropdown, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.RandomColorFrame = QFrame(self.color_presets_group)
        self.RandomColorFrame.setObjectName(u"RandomColorFrame")
        sizePolicy4.setHeightForWidth(self.RandomColorFrame.sizePolicy().hasHeightForWidth())
        self.RandomColorFrame.setSizePolicy(sizePolicy4)
        self.gridLayout_13 = QGridLayout(self.RandomColorFrame)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.rColorRangeContainer = QFrame(self.RandomColorFrame)
        self.rColorRangeContainer.setObjectName(u"rColorRangeContainer")
        sizePolicy11.setHeightForWidth(self.rColorRangeContainer.sizePolicy().hasHeightForWidth())
        self.rColorRangeContainer.setSizePolicy(sizePolicy11)
        self.rColorRangeContainer.setMaximumSize(QSize(256, 16777215))
        self.rColorRangeContainer.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_20 = QVBoxLayout(self.rColorRangeContainer)
        self.verticalLayout_20.setSpacing(1)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.color_range_preset_buttons_frame = QFrame(self.rColorRangeContainer)
        self.color_range_preset_buttons_frame.setObjectName(u"color_range_preset_buttons_frame")
        sizePolicy12.setHeightForWidth(self.color_range_preset_buttons_frame.sizePolicy().hasHeightForWidth())
        self.color_range_preset_buttons_frame.setSizePolicy(sizePolicy12)
        self.color_range_preset_buttons_frame.setMinimumSize(QSize(100, 50))
        self.color_range_preset_buttons_frame.setMaximumSize(QSize(266, 28))
        self.color_range_preset_buttons_frame.setStyleSheet(u"font: 700 14pt \"Inter\";")
        self.horizontalLayout_25 = QHBoxLayout(self.color_range_preset_buttons_frame)
        self.horizontalLayout_25.setSpacing(20)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.rcp_minimize_red = QPushButton(self.color_range_preset_buttons_frame)
        self.randomColorsPresetsGroup = QButtonGroup(MainWindow)
        self.randomColorsPresetsGroup.setObjectName(u"randomColorsPresetsGroup")
        self.randomColorsPresetsGroup.addButton(self.rcp_minimize_red)
        self.rcp_minimize_red.setObjectName(u"rcp_minimize_red")
        self.rcp_minimize_red.setFont(font3)
        self.rcp_minimize_red.setStyleSheet(u"color: rgb(250, 0, 0);\n"
"")

        self.horizontalLayout_11.addWidget(self.rcp_minimize_red)

        self.rcp_maximize_red = QPushButton(self.color_range_preset_buttons_frame)
        self.randomColorsPresetsGroup.addButton(self.rcp_maximize_red)
        self.rcp_maximize_red.setObjectName(u"rcp_maximize_red")
        self.rcp_maximize_red.setFont(font3)
        self.rcp_maximize_red.setStyleSheet(u"color: rgb(250, 0, 0);")

        self.horizontalLayout_11.addWidget(self.rcp_maximize_red)


        self.horizontalLayout_25.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.rcp_minimize_green = QPushButton(self.color_range_preset_buttons_frame)
        self.randomColorsPresetsGroup.addButton(self.rcp_minimize_green)
        self.rcp_minimize_green.setObjectName(u"rcp_minimize_green")
        self.rcp_minimize_green.setFont(font3)
        self.rcp_minimize_green.setStyleSheet(u"color: rgb(0, 250, 0);")

        self.horizontalLayout_31.addWidget(self.rcp_minimize_green)

        self.rcp_maximize_green = QPushButton(self.color_range_preset_buttons_frame)
        self.randomColorsPresetsGroup.addButton(self.rcp_maximize_green)
        self.rcp_maximize_green.setObjectName(u"rcp_maximize_green")
        self.rcp_maximize_green.setFont(font3)
        self.rcp_maximize_green.setStyleSheet(u"color: rgb(0, 250, 0);")

        self.horizontalLayout_31.addWidget(self.rcp_maximize_green)


        self.horizontalLayout_25.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.rcp_maximize_blue = QPushButton(self.color_range_preset_buttons_frame)
        self.randomColorsPresetsGroup.addButton(self.rcp_maximize_blue)
        self.rcp_maximize_blue.setObjectName(u"rcp_maximize_blue")
        self.rcp_maximize_blue.setFont(font3)
        self.rcp_maximize_blue.setStyleSheet(u"color: rgb(0, 0, 250);")

        self.horizontalLayout_32.addWidget(self.rcp_maximize_blue)

        self.rcp_minimize_blue = QPushButton(self.color_range_preset_buttons_frame)
        self.randomColorsPresetsGroup.addButton(self.rcp_minimize_blue)
        self.rcp_minimize_blue.setObjectName(u"rcp_minimize_blue")
        self.rcp_minimize_blue.setFont(font3)
        self.rcp_minimize_blue.setStyleSheet(u"color: rgb(0, 0, 250);")

        self.horizontalLayout_32.addWidget(self.rcp_minimize_blue)


        self.horizontalLayout_25.addLayout(self.horizontalLayout_32)


        self.verticalLayout_20.addWidget(self.color_range_preset_buttons_frame, 0, Qt.AlignHCenter)

        self.ColorsMinGP = QGroupBox(self.rColorRangeContainer)
        self.ColorsMinGP.setObjectName(u"ColorsMinGP")
        sizePolicy4.setHeightForWidth(self.ColorsMinGP.sizePolicy().hasHeightForWidth())
        self.ColorsMinGP.setSizePolicy(sizePolicy4)
        self.ColorsMinGP.setMaximumSize(QSize(16777215, 71))
        self.horizontalLayout_14 = QHBoxLayout(self.ColorsMinGP)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.red_min = QSpinBox(self.ColorsMinGP)
        self.red_min.setObjectName(u"red_min")
        self.red_min.setMinimumSize(QSize(60, 30))
        self.red_min.setMaximumSize(QSize(60, 30))
        self.red_min.setFont(font1)
        self.red_min.setStyleSheet(u"background-color: rgb(200, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.red_min.setAccelerated(True)
        self.red_min.setMinimum(0)
        self.red_min.setMaximum(255)
        self.red_min.setValue(20)

        self.horizontalLayout_14.addWidget(self.red_min, 0, Qt.AlignHCenter)

        self.green_min = QSpinBox(self.ColorsMinGP)
        self.green_min.setObjectName(u"green_min")
        self.green_min.setMinimumSize(QSize(60, 30))
        self.green_min.setMaximumSize(QSize(60, 30))
        self.green_min.setFont(font1)
        self.green_min.setStyleSheet(u"background-color: rgb(0, 200, 0);\n"
"color: rgb(25, 25, 25);")
        self.green_min.setAccelerated(True)
        self.green_min.setMaximum(255)
        self.green_min.setValue(20)

        self.horizontalLayout_14.addWidget(self.green_min)

        self.blue_min = QSpinBox(self.ColorsMinGP)
        self.blue_min.setObjectName(u"blue_min")
        self.blue_min.setMinimumSize(QSize(60, 30))
        self.blue_min.setMaximumSize(QSize(60, 30))
        self.blue_min.setFont(font1)
        self.blue_min.setStyleSheet(u"background-color: rgb(0, 0, 200);\n"
"color: rgb(255, 255, 255);")
        self.blue_min.setAccelerated(True)
        self.blue_min.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.blue_min.setMaximum(255)
        self.blue_min.setStepType(QAbstractSpinBox.DefaultStepType)
        self.blue_min.setValue(20)

        self.horizontalLayout_14.addWidget(self.blue_min)


        self.verticalLayout_20.addWidget(self.ColorsMinGP, 0, Qt.AlignHCenter)

        self.rcpresets3 = QFrame(self.rColorRangeContainer)
        self.rcpresets3.setObjectName(u"rcpresets3")
        sizePolicy5.setHeightForWidth(self.rcpresets3.sizePolicy().hasHeightForWidth())
        self.rcpresets3.setSizePolicy(sizePolicy5)
        self.gridLayout_7 = QGridLayout(self.rcpresets3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.rcp_dark = QPushButton(self.rcpresets3)
        self.randomColorsPresetsGroup.addButton(self.rcp_dark)
        self.rcp_dark.setObjectName(u"rcp_dark")
        self.rcp_dark.setFont(font1)

        self.gridLayout_7.addWidget(self.rcp_dark, 0, 2, 1, 1)

        self.rcp_reset = QPushButton(self.rcpresets3)
        self.randomColorsPresetsGroup.addButton(self.rcp_reset)
        self.rcp_reset.setObjectName(u"rcp_reset")
        self.rcp_reset.setFont(font1)

        self.gridLayout_7.addWidget(self.rcp_reset, 0, 4, 1, 1)

        self.rcp_bright = QPushButton(self.rcpresets3)
        self.randomColorsPresetsGroup.addButton(self.rcp_bright)
        self.rcp_bright.setObjectName(u"rcp_bright")
        self.rcp_bright.setFont(font1)

        self.gridLayout_7.addWidget(self.rcp_bright, 0, 0, 1, 1)

        self.rcp_gray = QPushButton(self.rcpresets3)
        self.randomColorsPresetsGroup.addButton(self.rcp_gray)
        self.rcp_gray.setObjectName(u"rcp_gray")
        self.rcp_gray.setFont(font1)

        self.gridLayout_7.addWidget(self.rcp_gray, 0, 1, 1, 1)


        self.verticalLayout_20.addWidget(self.rcpresets3, 0, Qt.AlignHCenter)

        self.ColorsMaxGP = QGroupBox(self.rColorRangeContainer)
        self.ColorsMaxGP.setObjectName(u"ColorsMaxGP")
        sizePolicy10.setHeightForWidth(self.ColorsMaxGP.sizePolicy().hasHeightForWidth())
        self.ColorsMaxGP.setSizePolicy(sizePolicy10)
        self.ColorsMaxGP.setMaximumSize(QSize(16777215, 71))
        self.horizontalLayout_15 = QHBoxLayout(self.ColorsMaxGP)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.red_max = QSpinBox(self.ColorsMaxGP)
        self.red_max.setObjectName(u"red_max")
        self.red_max.setMinimumSize(QSize(60, 30))
        self.red_max.setMaximumSize(QSize(60, 30))
        self.red_max.setFont(font1)
        self.red_max.setStyleSheet(u"background-color: rgb(200, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.red_max.setAccelerated(True)
        self.red_max.setMinimum(0)
        self.red_max.setMaximum(255)
        self.red_max.setValue(150)

        self.horizontalLayout_15.addWidget(self.red_max, 0, Qt.AlignHCenter)

        self.green_max = QSpinBox(self.ColorsMaxGP)
        self.green_max.setObjectName(u"green_max")
        self.green_max.setMinimumSize(QSize(60, 30))
        self.green_max.setMaximumSize(QSize(60, 30))
        self.green_max.setFont(font1)
        self.green_max.setStyleSheet(u"background-color: rgb(0, 200, 0);\n"
"color: rgb(25, 25, 25);")
        self.green_max.setAccelerated(True)
        self.green_max.setMaximum(255)
        self.green_max.setValue(250)

        self.horizontalLayout_15.addWidget(self.green_max, 0, Qt.AlignHCenter)

        self.blue_max = QSpinBox(self.ColorsMaxGP)
        self.blue_max.setObjectName(u"blue_max")
        self.blue_max.setMinimumSize(QSize(60, 30))
        self.blue_max.setMaximumSize(QSize(60, 30))
        self.blue_max.setFont(font1)
        self.blue_max.setStyleSheet(u"background-color: rgb(0, 0, 200);\n"
"color: rgb(255, 255, 255);")
        self.blue_max.setAccelerated(True)
        self.blue_max.setMaximum(255)
        self.blue_max.setValue(150)

        self.horizontalLayout_15.addWidget(self.blue_max, 0, Qt.AlignHCenter)


        self.verticalLayout_20.addWidget(self.ColorsMaxGP, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_13.addWidget(self.rColorRangeContainer, 0, 0, 1, 1, Qt.AlignHCenter)

        self.frame_18 = QFrame(self.RandomColorFrame)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy12.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy12)
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Plain)
        self.frame_18.setLineWidth(1)
        self.verticalLayout_22 = QVBoxLayout(self.frame_18)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")

        self.gridLayout_13.addWidget(self.frame_18, 0, 1, 1, 1)


        self.verticalLayout_18.addWidget(self.RandomColorFrame, 0, Qt.AlignHCenter)


        self.verticalLayout_32.addWidget(self.color_presets_group, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.SummaryFrame, 0, 0, 2, 1, Qt.AlignHCenter)

        self.MaskandEmojisFrame = QFrame(self.centralwidget)
        self.MaskandEmojisFrame.setObjectName(u"MaskandEmojisFrame")
        sizePolicy13 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.MaskandEmojisFrame.sizePolicy().hasHeightForWidth())
        self.MaskandEmojisFrame.setSizePolicy(sizePolicy13)
        self.kaka = QGridLayout(self.MaskandEmojisFrame)
        self.kaka.setObjectName(u"kaka")
        self.EmojiFull_Frame = QFrame(self.MaskandEmojisFrame)
        self.EmojiFull_Frame.setObjectName(u"EmojiFull_Frame")
        sizePolicy8.setHeightForWidth(self.EmojiFull_Frame.sizePolicy().hasHeightForWidth())
        self.EmojiFull_Frame.setSizePolicy(sizePolicy8)
        self.EmojiFull_Frame.setFont(font4)
        self.verticalLayout_9 = QVBoxLayout(self.EmojiFull_Frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(20, -1, -1, -1)
        self.load_emojis_Frame = QFrame(self.EmojiFull_Frame)
        self.load_emojis_Frame.setObjectName(u"load_emojis_Frame")
        sizePolicy10.setHeightForWidth(self.load_emojis_Frame.sizePolicy().hasHeightForWidth())
        self.load_emojis_Frame.setSizePolicy(sizePolicy10)
        self.horizontalLayout_6 = QHBoxLayout(self.load_emojis_Frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.unicode_Emojis_btn = QPushButton(self.load_emojis_Frame)
        self.unicode_Emojis_btn.setObjectName(u"unicode_Emojis_btn")
        self.unicode_Emojis_btn.setEnabled(True)
        self.unicode_Emojis_btn.setMinimumSize(QSize(150, 40))
        self.unicode_Emojis_btn.setMaximumSize(QSize(150, 16777215))
        self.unicode_Emojis_btn.setFont(font1)
        self.unicode_Emojis_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.unicode_Emojis_btn)

        self.font_Awesome_Icons_btn = QPushButton(self.load_emojis_Frame)
        self.font_Awesome_Icons_btn.setObjectName(u"font_Awesome_Icons_btn")
        self.font_Awesome_Icons_btn.setEnabled(True)
        self.font_Awesome_Icons_btn.setMinimumSize(QSize(150, 40))
        self.font_Awesome_Icons_btn.setMaximumSize(QSize(150, 16777215))
        self.font_Awesome_Icons_btn.setFont(font1)
        self.font_Awesome_Icons_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.font_Awesome_Icons_btn)


        self.verticalLayout_9.addWidget(self.load_emojis_Frame, 0, Qt.AlignHCenter)

        self.FilterListFrame = QFrame(self.EmojiFull_Frame)
        self.FilterListFrame.setObjectName(u"FilterListFrame")
        sizePolicy4.setHeightForWidth(self.FilterListFrame.sizePolicy().hasHeightForWidth())
        self.FilterListFrame.setSizePolicy(sizePolicy4)
        self.horizontalLayout_5 = QHBoxLayout(self.FilterListFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.emojiFilter_label = QLabel(self.FilterListFrame)
        self.emojiFilter_label.setObjectName(u"emojiFilter_label")
        sizePolicy4.setHeightForWidth(self.emojiFilter_label.sizePolicy().hasHeightForWidth())
        self.emojiFilter_label.setSizePolicy(sizePolicy4)
        font6 = QFont()
        font6.setFamilies([u"Inter"])
        font6.setPointSize(11)
        font6.setBold(True)
        self.emojiFilter_label.setFont(font6)

        self.horizontalLayout_5.addWidget(self.emojiFilter_label)

        self.emoji_filter_list = QComboBox(self.FilterListFrame)
        self.emoji_filter_list.addItem("")
        self.emoji_filter_list.addItem("")
        self.emoji_filter_list.addItem("")
        self.emoji_filter_list.addItem("")
        self.emoji_filter_list.addItem("")
        self.emoji_filter_list.addItem("")
        self.emoji_filter_list.addItem("")
        self.emoji_filter_list.addItem("")
        self.emoji_filter_list.addItem("")
        self.emoji_filter_list.addItem("")
        self.emoji_filter_list.setObjectName(u"emoji_filter_list")
        sizePolicy4.setHeightForWidth(self.emoji_filter_list.sizePolicy().hasHeightForWidth())
        self.emoji_filter_list.setSizePolicy(sizePolicy4)
        self.emoji_filter_list.setMinimumSize(QSize(211, 41))
        self.emoji_filter_list.setFont(font6)
        self.emoji_filter_list.setStyleSheet(u"/* Style the QComboBox */\n"
"QComboBox {\n"
"    background-color: #141414; /* Background color of the entire combo box */\n"
"    border: 1px solid #e6e6e6; /* Border around the combo box */\n"
"    padding: 10px; /* Padding inside the combo box */\n"
"    color:#e6e6e6; /* Current text color*/\n"
"}\n"
"/* Style the QComboBox's drop-down list */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #141414; /* Background color of the drop-down list */\n"
"    border: 1px solid #e6e6e6; /* Border around the drop-down list */\n"
"    padding: 10px; /* Padding inside the drop-down list */\n"
"	color:#e6e6e6;\n"
"}\n"
"/* Style individual items within the QComboBox's drop-down list */\n"
"QComboBox QAbstractItemView::item {\n"
"    background-color: #141414; /* Background color of each item in the list */\n"
"    padding: 1px; /* Padding inside each item */\n"
"	color: #e6e6e6;\n"
"}\n"
"/* Style the selected item within the drop-down list */\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    backgr"
                        "ound-color: rgba(0,200,0,150); /* Background color of the selected item */\n"
"    color: #e6e6e6; /* Text color of the selected item */\n"
"}\n"
"/* Style the drop-down list scroll bar (if it appears) */\n"
"QComboBox QScrollBar:vertical {\n"
"    width: 0px; /* Width of the vertical scrollbar */\n"
"    background: #e6e6e6; /* Background color of the scrollbar */\n"
"}\n"
"/* Style the drop-down list scroll bar handle (thumb) */\n"
"QComboBox QScrollBar::handle:vertical {\n"
"    background: #141414; /* Background color of the scrollbar handle */\n"
"}")

        self.horizontalLayout_5.addWidget(self.emoji_filter_list)


        self.verticalLayout_9.addWidget(self.FilterListFrame, 0, Qt.AlignHCenter)

        self.emoji_list = QListWidget(self.EmojiFull_Frame)
        self.emoji_list.setObjectName(u"emoji_list")
        sizePolicy2.setHeightForWidth(self.emoji_list.sizePolicy().hasHeightForWidth())
        self.emoji_list.setSizePolicy(sizePolicy2)
        font7 = QFont()
        font7.setFamilies([u"Segoe UI Emoji"])
        font7.setPointSize(28)
        font7.setBold(False)
        self.emoji_list.setFont(font7)
        self.emoji_list.setStyleSheet(u"QListWidget::item:selected {\n"
"    background: rgba(0,200,0,200);\n"
"}\n"
"QListWidget::item:hover {\n"
"    background: rgba(0,200,0,200);\n"
"}\n"
"QListWidget{\n"
"background:rgba(20,20,20,200);\n"
"border-radius:0px;\n"
"border:1px solid #e6e6e6;\n"
"}")
        self.emoji_list.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.emoji_list.setAutoScroll(False)
        self.emoji_list.setAutoScrollMargin(20)
        self.emoji_list.setTextElideMode(Qt.ElideNone)
        self.emoji_list.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.emoji_list.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.emoji_list.setMovement(QListView.Snap)
        self.emoji_list.setProperty("isWrapping", True)
        self.emoji_list.setResizeMode(QListView.Adjust)
        self.emoji_list.setLayoutMode(QListView.SinglePass)
        self.emoji_list.setSpacing(1)
        self.emoji_list.setViewMode(QListView.IconMode)
        self.emoji_list.setUniformItemSizes(True)

        self.verticalLayout_9.addWidget(self.emoji_list)


        self.kaka.addWidget(self.EmojiFull_Frame, 1, 1, 1, 1)

        self.mask_container = QFrame(self.MaskandEmojisFrame)
        self.mask_container.setObjectName(u"mask_container")
        sizePolicy4.setHeightForWidth(self.mask_container.sizePolicy().hasHeightForWidth())
        self.mask_container.setSizePolicy(sizePolicy4)
        self.mask_container.setStyleSheet(u"")
        self.mask_container.setFrameShape(QFrame.StyledPanel)
        self.mask_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.mask_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mask_image_thumbnail = QLabel(self.mask_container)
        self.mask_image_thumbnail.setObjectName(u"mask_image_thumbnail")
        self.mask_image_thumbnail.setMinimumSize(QSize(200, 200))
        self.mask_image_thumbnail.setFrameShape(QFrame.NoFrame)
        self.mask_image_thumbnail.setLineWidth(1)
        self.mask_image_thumbnail.setScaledContents(False)

        self.verticalLayout.addWidget(self.mask_image_thumbnail, 0, Qt.AlignHCenter)

        self.mask_dimensions_label = QLabel(self.mask_container)
        self.mask_dimensions_label.setObjectName(u"mask_dimensions_label")
        sizePolicy4.setHeightForWidth(self.mask_dimensions_label.sizePolicy().hasHeightForWidth())
        self.mask_dimensions_label.setSizePolicy(sizePolicy4)
        self.mask_dimensions_label.setMaximumSize(QSize(300, 16777215))
        font8 = QFont()
        font8.setFamilies([u"Inter"])
        font8.setPointSize(9)
        font8.setBold(True)
        font8.setItalic(False)
        font8.setUnderline(False)
        font8.setStyleStrategy(QFont.PreferDefault)
        self.mask_dimensions_label.setFont(font8)
        self.mask_dimensions_label.setCursor(QCursor(Qt.ArrowCursor))

        self.verticalLayout.addWidget(self.mask_dimensions_label, 0, Qt.AlignHCenter)

        self.SelectButtonsFrame = QFrame(self.mask_container)
        self.SelectButtonsFrame.setObjectName(u"SelectButtonsFrame")
        sizePolicy4.setHeightForWidth(self.SelectButtonsFrame.sizePolicy().hasHeightForWidth())
        self.SelectButtonsFrame.setSizePolicy(sizePolicy4)
        self.horizontalLayout_3 = QHBoxLayout(self.SelectButtonsFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.mask_select_button = QPushButton(self.SelectButtonsFrame)
        self.mask_select_button.setObjectName(u"mask_select_button")
        self.mask_select_button.setMinimumSize(QSize(150, 50))
        self.mask_select_button.setMaximumSize(QSize(150, 16777215))
        self.mask_select_button.setFont(font1)
        self.mask_select_button.setStyleSheet(u"QPushButton{\n"
"border:2px solid red; \n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.mask_select_button)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.select_destination_button = QPushButton(self.SelectButtonsFrame)
        self.select_destination_button.setObjectName(u"select_destination_button")
        self.select_destination_button.setEnabled(True)
        self.select_destination_button.setMinimumSize(QSize(150, 50))
        self.select_destination_button.setMaximumSize(QSize(150, 16777215))
        self.select_destination_button.setFont(font1)
        self.select_destination_button.setStyleSheet(u"QPushButton{\n"
"border:2px solid red; \n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.select_destination_button)

        self.open_destination_folder = QPushButton(self.SelectButtonsFrame)
        self.open_destination_folder.setObjectName(u"open_destination_folder")
        self.open_destination_folder.setMinimumSize(QSize(50, 50))
        self.open_destination_folder.setMaximumSize(QSize(40, 50))
        self.open_destination_folder.setFont(font1)
        self.open_destination_folder.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 170, 0);\n"
"border-radius:5px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.open_destination_folder)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.SelectButtonsFrame, 0, Qt.AlignHCenter)


        self.kaka.addWidget(self.mask_container, 0, 1, 1, 1, Qt.AlignRight)


        self.gridLayout.addWidget(self.MaskandEmojisFrame, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.parameters_window.setCurrentIndex(1)
        self.generate_wordcloud_button.setDefault(False)
        self.colormaps_dropdown.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WCGX - WordCloud Generator X-Treme", None))
        self.WordInputAndParametersFrame.setStyleSheet(QCoreApplication.translate("MainWindow", u"QListWidget{\n"
"border:2px solid gray;\n"
"color: #141414;\n"
"font: 700 11pt \"Inter\";\n"
"}", None))
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
        self.parameters_window.setTabText(self.parameters_window.indexOf(self.parameters_windowPage_2), QCoreApplication.translate("MainWindow", u"Repeat", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Set the smallest and largest allowed\n"
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
        self.MinFSp49.setText(QCoreApplication.translate("MainWindow", u"49", None))
        self.MinFSp31.setText(QCoreApplication.translate("MainWindow", u"31", None))
        self.MinFSp21.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.MinFSp10.setText(QCoreApplication.translate("MainWindow", u"10", None))
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
        self.MaxFSp250.setText(QCoreApplication.translate("MainWindow", u"250", None))
        self.MaxFSp150.setText(QCoreApplication.translate("MainWindow", u"150", None))
        self.MaxFSp73.setText(QCoreApplication.translate("MainWindow", u"73", None))
        self.MaxFSp50.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.parameters_window.setTabText(self.parameters_window.indexOf(self.parameters_windowPage), QCoreApplication.translate("MainWindow", u"Font Size", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Font Step > 1 might speed up\n"
"computation, but result in a worse fit.", None))
#if QT_CONFIG(tooltip)
        self.fontstep_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Control the minimum font size of generated word(s) </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.fontstep_label.setText(QCoreApplication.translate("MainWindow", u"Font Step", None))
#if QT_CONFIG(tooltip)
        self.font_step_indicator_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Minimum Font Size </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.font_step_indicator_label.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.parameters_window.setTabText(self.parameters_window.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Font Step", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Minimum allowed margin between words.", None))
#if QT_CONFIG(tooltip)
        self.margin_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Control the space between the generated words </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.margin_label.setText(QCoreApplication.translate("MainWindow", u"Margin", None))
#if QT_CONFIG(tooltip)
        self.margin_slider.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Set the margin between the generated words </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_margin_slider.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Margin between generated words</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_margin_slider.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.parameters_window.setTabText(self.parameters_window.indexOf(self.parameters_windowPage3), QCoreApplication.translate("MainWindow", u"Margin", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"The ratio of times to try horizontal fitting.\n"
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
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Mask image size * Image Scale = Exported Image size\n"
"Using a smaller mask and increasing the scale\n"
"results in faster rendering.", None))
        self.parameters_window.setTabText(self.parameters_window.indexOf(self.parameters_windowPage5), QCoreApplication.translate("MainWindow", u"Scale", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"The words that will be ignored. (NYI)", None))
#if QT_CONFIG(tooltip)
        self.stopwords_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Include/Exclude common words </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.stopwords_label.setText(QCoreApplication.translate("MainWindow", u"StopWords", None))
#if QT_CONFIG(tooltip)
        self.stopwords_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Checked - common words will be excluded <br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.stopwords_checkbox.setText("")
        self.parameters_window.setTabText(self.parameters_window.indexOf(self.parameters_windowPage6), QCoreApplication.translate("MainWindow", u"StopWords", None))
        self.label_collocations_thresh.setText(QCoreApplication.translate("MainWindow", u"Collocation Threshold", None))
        self.collocation_thresh_slider_label.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"The Dunning likelihood collocation score is calculated for each\n"
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
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Whether to include collocations (bigrams) of two words.\n"
"Ignored if using generate_from_frequencies.", None))
        self.label_collocations.setText(QCoreApplication.translate("MainWindow", u"Collocations", None))
        self.collocations_checkbox.setText("")
        self.parameters_window.setTabText(self.parameters_window.indexOf(self.parameters_windowPage8), QCoreApplication.translate("MainWindow", u"Collocations", None))
#if QT_CONFIG(tooltip)
        self.stopwords_label_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Include/Exclude numbers</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.stopwords_label_2.setText(QCoreApplication.translate("MainWindow", u"Include Numbers", None))
#if QT_CONFIG(tooltip)
        self.include_number_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Checked - common words will be excluded <br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.include_number_checkbox.setText("")
#if QT_CONFIG(tooltip)
        self.regxp_any_character_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Any special characters will be trated as words</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.regxp_any_character_label.setText(QCoreApplication.translate("MainWindow", u"Include ALL special characters", None))
#if QT_CONFIG(tooltip)
        self.regxp_any_character_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Checked - common words will be excluded <br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.regxp_any_character_checkbox.setText("")
        self.label_Character_Filtering_Title.setText(QCoreApplication.translate("MainWindow", u"Character Filtering", None))
#if QT_CONFIG(tooltip)
        self.connected_punctuation_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Punctuation included if connected to a word<br/>Example: </span></p><p><span style=\" font-size:10pt; font-weight:400;\">word?com (? included)</span></p><p><span style=\" font-size:10pt; font-weight:400;\">word ? com (? excluded)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.connected_punctuation_label.setText(QCoreApplication.translate("MainWindow", u"Connected Punctuation", None))
#if QT_CONFIG(tooltip)
        self.connected_punctuation_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Checked - common words will be excluded <br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.connected_punctuation_checkbox.setText("")
        self.parameters_window.setTabText(self.parameters_window.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Char. Inc.", None))
        self.generated_text_label.setText(QCoreApplication.translate("MainWindow", u"Generated Text:", None))
        self.load_system_fonts_btn.setText(QCoreApplication.translate("MainWindow", u"Load System Fonts", None))
        self.custom_font_directory_selection.setText(QCoreApplication.translate("MainWindow", u"Select Custom Folder", None))
        self.load_emoji_fonts_btn.setText(QCoreApplication.translate("MainWindow", u"Load Emoji Fonts", None))
        self.word_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"WordCloud text goes here. Different words will be identified based on space. Ex: word1 word2", None))
#if QT_CONFIG(tooltip)
        self.stash_last_generated_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Stash the last generated image(s)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.stash_last_generated_button.setText(QCoreApplication.translate("MainWindow", u"Stash", None))
#if QT_CONFIG(tooltip)
        self.delete_last_generated_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Delete the last generated image(s)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.delete_last_generated_button.setText(QCoreApplication.translate("MainWindow", u"Del", None))
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
        self.parameters_summary_label_2.setText(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.repeatWords_btn.setText(QCoreApplication.translate("MainWindow", u"Repeat Words:", None))
        self.repeat_info_label.setText(QCoreApplication.translate("MainWindow", u"result here", None))
        self.marginSettings_btn.setText(QCoreApplication.translate("MainWindow", u"Margin:", None))
        self.margin_info_label.setText(QCoreApplication.translate("MainWindow", u"result here", None))
        self.fontSizeSettings_btn.setText(QCoreApplication.translate("MainWindow", u"Min. Font Size:", None))
        self.min_font_size_info_label.setText(QCoreApplication.translate("MainWindow", u"result here", None))
        self.fontSizeSettings_btn2.setText(QCoreApplication.translate("MainWindow", u"Max. Font Size:", None))
        self.max_font_size_info_label.setText(QCoreApplication.translate("MainWindow", u"result here", None))
        self.textOrientationSettings_btn.setText(QCoreApplication.translate("MainWindow", u"Orientation:", None))
        self.prefer_horizontal_info_label.setText(QCoreApplication.translate("MainWindow", u"result here", None))
        self.fontStepSettings_btn.setText(QCoreApplication.translate("MainWindow", u"Font Step:", None))
        self.fontstep_info_label.setText(QCoreApplication.translate("MainWindow", u"result here", None))
        self.collocationSettings_btn.setText(QCoreApplication.translate("MainWindow", u"CLC:", None))
        self.collocations_info_label.setText(QCoreApplication.translate("MainWindow", u"result here", None))
        self.collocationSettings_btn2.setText(QCoreApplication.translate("MainWindow", u"CLC Thresh:", None))
        self.collocations_thresh_info_label.setText(QCoreApplication.translate("MainWindow", u"result here", None))
        self.charInclusion_btn.setText(QCoreApplication.translate("MainWindow", u"Include Numbers:", None))
        self.include_numbers_info_label.setText(QCoreApplication.translate("MainWindow", u"result here", None))
        self.scaleSettings_btn.setText(QCoreApplication.translate("MainWindow", u"Scale:", None))
        self.scale_multiplier_info_label.setText(QCoreApplication.translate("MainWindow", u"result here", None))
        self.label_color_presets.setText(QCoreApplication.translate("MainWindow", u"Color Presets", None))
        self.colormaps_dropdown.setItemText(0, QCoreApplication.translate("MainWindow", u"Default", None))
        self.colormaps_dropdown.setItemText(1, QCoreApplication.translate("MainWindow", u"Accent", None))
        self.colormaps_dropdown.setItemText(2, QCoreApplication.translate("MainWindow", u"Reds", None))
        self.colormaps_dropdown.setItemText(3, QCoreApplication.translate("MainWindow", u"Dark2", None))
        self.colormaps_dropdown.setItemText(4, QCoreApplication.translate("MainWindow", u"Paired", None))
        self.colormaps_dropdown.setItemText(5, QCoreApplication.translate("MainWindow", u"Set1", None))
        self.colormaps_dropdown.setItemText(6, QCoreApplication.translate("MainWindow", u"Set2", None))
        self.colormaps_dropdown.setItemText(7, QCoreApplication.translate("MainWindow", u"Set3", None))
        self.colormaps_dropdown.setItemText(8, QCoreApplication.translate("MainWindow", u"Random Colors", None))
        self.colormaps_dropdown.setItemText(9, QCoreApplication.translate("MainWindow", u"Greens", None))
        self.colormaps_dropdown.setItemText(10, QCoreApplication.translate("MainWindow", u"Blues", None))
        self.colormaps_dropdown.setItemText(11, QCoreApplication.translate("MainWindow", u"Greys", None))
        self.colormaps_dropdown.setItemText(12, QCoreApplication.translate("MainWindow", u"Purples", None))
        self.colormaps_dropdown.setItemText(13, QCoreApplication.translate("MainWindow", u"Oranges", None))
        self.colormaps_dropdown.setItemText(14, QCoreApplication.translate("MainWindow", u"plasma", None))
        self.colormaps_dropdown.setItemText(15, QCoreApplication.translate("MainWindow", u"Spectral", None))
        self.colormaps_dropdown.setItemText(16, QCoreApplication.translate("MainWindow", u"Pastel1", None))
        self.colormaps_dropdown.setItemText(17, QCoreApplication.translate("MainWindow", u"Pastel2", None))
        self.colormaps_dropdown.setItemText(18, QCoreApplication.translate("MainWindow", u"Wistia", None))
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
        self.colormaps_dropdown.setItemText(36, QCoreApplication.translate("MainWindow", u"prism", None))
        self.colormaps_dropdown.setItemText(37, QCoreApplication.translate("MainWindow", u"ocean", None))
        self.colormaps_dropdown.setItemText(38, QCoreApplication.translate("MainWindow", u"terrain", None))
        self.colormaps_dropdown.setItemText(39, QCoreApplication.translate("MainWindow", u"rainbow", None))
        self.colormaps_dropdown.setItemText(40, QCoreApplication.translate("MainWindow", u"turbo", None))
        self.colormaps_dropdown.setItemText(41, QCoreApplication.translate("MainWindow", u"gist_ncar_r", None))

#if QT_CONFIG(tooltip)
        self.rcp_minimize_red.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Min Red </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rcp_minimize_red.setText(QCoreApplication.translate("MainWindow", u"\u25bc", None))
#if QT_CONFIG(tooltip)
        self.rcp_maximize_red.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Max Red </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rcp_maximize_red.setText(QCoreApplication.translate("MainWindow", u"\u25b2", None))
#if QT_CONFIG(tooltip)
        self.rcp_minimize_green.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Min Green </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rcp_minimize_green.setText(QCoreApplication.translate("MainWindow", u"\u25bc", None))
#if QT_CONFIG(tooltip)
        self.rcp_maximize_green.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Max Green </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rcp_maximize_green.setText(QCoreApplication.translate("MainWindow", u"\u25b2", None))
#if QT_CONFIG(tooltip)
        self.rcp_maximize_blue.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Max Blue </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rcp_maximize_blue.setText(QCoreApplication.translate("MainWindow", u"\u25b2", None))
#if QT_CONFIG(tooltip)
        self.rcp_minimize_blue.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Min Blue </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rcp_minimize_blue.setText(QCoreApplication.translate("MainWindow", u"\u25bc", None))
        self.ColorsMinGP.setTitle(QCoreApplication.translate("MainWindow", u"Min", None))
#if QT_CONFIG(tooltip)
        self.rcp_dark.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Dark color range </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rcp_dark.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
#if QT_CONFIG(tooltip)
        self.rcp_reset.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Reset all colors to max range </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rcp_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
#if QT_CONFIG(tooltip)
        self.rcp_bright.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Bright color range </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rcp_bright.setText(QCoreApplication.translate("MainWindow", u"Bright", None))
#if QT_CONFIG(tooltip)
        self.rcp_gray.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Reset all colors to max range </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rcp_gray.setText(QCoreApplication.translate("MainWindow", u"Gray", None))
        self.ColorsMaxGP.setTitle(QCoreApplication.translate("MainWindow", u"Max", None))
#if QT_CONFIG(tooltip)
        self.unicode_Emojis_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Select destination for generated PNG file</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.unicode_Emojis_btn.setText(QCoreApplication.translate("MainWindow", u"Unicode Emojis", None))
#if QT_CONFIG(tooltip)
        self.font_Awesome_Icons_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Select destination for generated PNG file</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.font_Awesome_Icons_btn.setText(QCoreApplication.translate("MainWindow", u"Font Awesome Icons", None))
        self.emojiFilter_label.setText(QCoreApplication.translate("MainWindow", u"Filter:", None))
        self.emoji_filter_list.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.emoji_filter_list.setItemText(1, QCoreApplication.translate("MainWindow", u"Objects", None))
        self.emoji_filter_list.setItemText(2, QCoreApplication.translate("MainWindow", u"Smileys & Emotion", None))
        self.emoji_filter_list.setItemText(3, QCoreApplication.translate("MainWindow", u"Travel & Places", None))
        self.emoji_filter_list.setItemText(4, QCoreApplication.translate("MainWindow", u"Animals & Nature", None))
        self.emoji_filter_list.setItemText(5, QCoreApplication.translate("MainWindow", u"Activities", None))
        self.emoji_filter_list.setItemText(6, QCoreApplication.translate("MainWindow", u"Food & Drink", None))
        self.emoji_filter_list.setItemText(7, QCoreApplication.translate("MainWindow", u"Flags", None))
        self.emoji_filter_list.setItemText(8, QCoreApplication.translate("MainWindow", u"People & Body", None))
        self.emoji_filter_list.setItemText(9, QCoreApplication.translate("MainWindow", u"Symbols", None))

        self.mask_image_thumbnail.setText(QCoreApplication.translate("MainWindow", u"MASK IMAGE WILL BE PLACED HERE", None))
        self.mask_dimensions_label.setText(QCoreApplication.translate("MainWindow", u"mask_dimensions_label", None))
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
    # retranslateUi

