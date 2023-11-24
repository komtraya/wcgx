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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QAbstractSpinBox, QApplication,
    QButtonGroup, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QStackedWidget, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)
import Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1869, 1371)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/Icon/WCGXicon2.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget{\n"
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
"QPlainTextEdit:focus{\n"
"border: 1px solid #e6e6e6;\n"
"}\n"
"QPlainTextEdit{\n"
"color: #141414;\n"
"}\n"
"QTextEdit{\n"
"color:#e6e6e6;\n"
"background:#151515;\n"
"}\n"
"QTextEdit:focus {\n"
"border:1px solid #e6e6e6;\n"
"}\n"
"QListWidget::item:selected {\n"
"    background: rgba(0,200,0,200);\n"
"}\n"
"QListWidget::item:hover {\n"
"    background: rgba(0,200,0,200);\n"
"}\n"
"QListWidget{\n"
"background:rgba(20,20,20,200);\n"
"border-radius:0px;\n"
"border:1px solid #e6e6e6;\n"
"}\n"
"QListWidget::item{\n"
"color:white;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    background: grey;\n"
"    margin: 0 3px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: red;\n"
"    border: none;\n"
"    height: 15px;\n"
"    margin: 0 -10px;\n"
"	/*	width:20px;*/\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    width: 10px;\n"
"    background: green;\n"
"    border: none;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    width: 15px;\n"
"    background: #e9e9e9;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, -1, 0)
        self.SummaryFrame = QFrame(self.centralwidget)
        self.SummaryFrame.setObjectName(u"SummaryFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.SummaryFrame.sizePolicy().hasHeightForWidth())
        self.SummaryFrame.setSizePolicy(sizePolicy1)
        self.SummaryFrame.setMinimumSize(QSize(301, 200))
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.SummaryFrame.setFont(font)
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
        self.update_settingsProfile_btn = QPushButton(self.SummaryFrame)
        self.update_settingsProfile_btn.setObjectName(u"update_settingsProfile_btn")
        self.update_settingsProfile_btn.setMinimumSize(QSize(32, 37))
        self.update_settingsProfile_btn.setMaximumSize(QSize(32, 37))
        self.update_settingsProfile_btn.setStyleSheet(u"QPushButton:pressed{\n"
"	 padding-left: 3px;\n"
"     padding-top: 3px;\n"
"}\n"
"QPushButton{\n"
"background-color: rgba(100,100,100,0);\n"
"border-radius:10px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Media/update_repair_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.update_settingsProfile_btn.setIcon(icon1)
        self.update_settingsProfile_btn.setIconSize(QSize(32, 37))

        self.verticalLayout_32.addWidget(self.update_settingsProfile_btn, 0, Qt.AlignHCenter)

        self.delete_btnFrame1 = QFrame(self.SummaryFrame)
        self.delete_btnFrame1.setObjectName(u"delete_btnFrame1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.delete_btnFrame1.sizePolicy().hasHeightForWidth())
        self.delete_btnFrame1.setSizePolicy(sizePolicy2)
        self.delete_btnFrame1.setMinimumSize(QSize(267, 30))
        self.delete_btnFrame1.setMaximumSize(QSize(267, 50))
        self.delete_btnFrame1.setStyleSheet(u"QWidget{\n"
"background-color: rgba(20, 20, 20,0);\n"
"}")
        self.horizontalLayout_10 = QHBoxLayout(self.delete_btnFrame1)
        self.horizontalLayout_10.setSpacing(40)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 15, 0, 0)
        self.storeSettingsProfile_btn = QPushButton(self.delete_btnFrame1)
        self.storeSettingsProfile_btn.setObjectName(u"storeSettingsProfile_btn")
        self.storeSettingsProfile_btn.setMinimumSize(QSize(32, 32))
        self.storeSettingsProfile_btn.setMaximumSize(QSize(32, 32))
        self.storeSettingsProfile_btn.setStyleSheet(u"QPushButton:pressed{\n"
"	 padding-left: 3px;\n"
"     padding-top: 3px;\n"
"}\n"
"QPushButton{\n"
"background-color: rgba(100,100,100,0);\n"
"border-radius:10px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Media/Settings_CogWheel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.storeSettingsProfile_btn.setIcon(icon2)
        self.storeSettingsProfile_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.storeSettingsProfile_btn)

        self.settingsProfiles_lbl = QLabel(self.delete_btnFrame1)
        self.settingsProfiles_lbl.setObjectName(u"settingsProfiles_lbl")
        sizePolicy2.setHeightForWidth(self.settingsProfiles_lbl.sizePolicy().hasHeightForWidth())
        self.settingsProfiles_lbl.setSizePolicy(sizePolicy2)
        self.settingsProfiles_lbl.setMinimumSize(QSize(0, 20))
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(False)
        self.settingsProfiles_lbl.setFont(font1)

        self.horizontalLayout_10.addWidget(self.settingsProfiles_lbl)

        self.deleteSettingsProfile_btn = QPushButton(self.delete_btnFrame1)
        self.deleteSettingsProfile_btn.setObjectName(u"deleteSettingsProfile_btn")
        self.deleteSettingsProfile_btn.setMinimumSize(QSize(14, 15))
        self.deleteSettingsProfile_btn.setMaximumSize(QSize(14, 15))
        self.deleteSettingsProfile_btn.setStyleSheet(u"QPushButton:pressed{\n"
"	 padding-left: 3px;\n"
"     padding-top: 3px;\n"
"}\n"
"QPushButton{\n"
"background-color: rgba(100,100,100,0);\n"
"border-radius:10px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/Media/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteSettingsProfile_btn.setIcon(icon3)
        self.deleteSettingsProfile_btn.setIconSize(QSize(14, 15))

        self.horizontalLayout_10.addWidget(self.deleteSettingsProfile_btn, 0, Qt.AlignRight)


        self.verticalLayout_32.addWidget(self.delete_btnFrame1, 0, Qt.AlignHCenter)

        self.settingsAreaFrame = QFrame(self.SummaryFrame)
        self.settingsAreaFrame.setObjectName(u"settingsAreaFrame")
        sizePolicy2.setHeightForWidth(self.settingsAreaFrame.sizePolicy().hasHeightForWidth())
        self.settingsAreaFrame.setSizePolicy(sizePolicy2)
        self.horizontalLayout_7 = QHBoxLayout(self.settingsAreaFrame)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.settingsProfiles_list = QComboBox(self.settingsAreaFrame)
        self.settingsProfiles_list.setObjectName(u"settingsProfiles_list")
        sizePolicy2.setHeightForWidth(self.settingsProfiles_list.sizePolicy().hasHeightForWidth())
        self.settingsProfiles_list.setSizePolicy(sizePolicy2)
        self.settingsProfiles_list.setMinimumSize(QSize(211, 41))
        font2 = QFont()
        font2.setFamilies([u"Inter"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.settingsProfiles_list.setFont(font2)
        self.settingsProfiles_list.setStyleSheet(u"/* Style the QComboBox */\n"
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
        self.settingsProfiles_list.setMaxVisibleItems(15)

        self.horizontalLayout_7.addWidget(self.settingsProfiles_list)

        self.applySettingsProfile_btn = QPushButton(self.settingsAreaFrame)
        self.applySettingsProfile_btn.setObjectName(u"applySettingsProfile_btn")
        self.applySettingsProfile_btn.setMinimumSize(QSize(32, 32))
        self.applySettingsProfile_btn.setMaximumSize(QSize(32, 32))
        self.applySettingsProfile_btn.setStyleSheet(u"QPushButton:pressed{\n"
"	 padding-left: 3px;\n"
"     padding-top: 3px;\n"
"}\n"
"QPushButton{\n"
"background-color: rgba(100,100,100,0);\n"
"border-radius:10px;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/Media/apply_agree2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.applySettingsProfile_btn.setIcon(icon4)
        self.applySettingsProfile_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_7.addWidget(self.applySettingsProfile_btn)


        self.verticalLayout_32.addWidget(self.settingsAreaFrame, 0, Qt.AlignHCenter)

        self.delete_btnFrame2 = QFrame(self.SummaryFrame)
        self.delete_btnFrame2.setObjectName(u"delete_btnFrame2")
        sizePolicy2.setHeightForWidth(self.delete_btnFrame2.sizePolicy().hasHeightForWidth())
        self.delete_btnFrame2.setSizePolicy(sizePolicy2)
        self.delete_btnFrame2.setMinimumSize(QSize(267, 30))
        self.delete_btnFrame2.setMaximumSize(QSize(267, 50))
        self.delete_btnFrame2.setStyleSheet(u"QWidget{\n"
"background-color: rgba(20, 20, 20,0);\n"
"}")
        self.horizontalLayout_12 = QHBoxLayout(self.delete_btnFrame2)
        self.horizontalLayout_12.setSpacing(50)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 15, 0, 0)
        self.storeTextProfile_btn2 = QPushButton(self.delete_btnFrame2)
        self.storeTextProfile_btn2.setObjectName(u"storeTextProfile_btn2")
        self.storeTextProfile_btn2.setMinimumSize(QSize(32, 32))
        self.storeTextProfile_btn2.setMaximumSize(QSize(32, 32))
        self.storeTextProfile_btn2.setStyleSheet(u"QPushButton:pressed{\n"
"/*	 padding-left: 3px;\n"
"     padding-top: 3px;*/\n"
"    border-style: inset;\n"
"}\n"
"QPushButton{\n"
"background-color: rgba(100,100,100,0);\n"
"border-radius:10px;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/Media/text_article.png", QSize(), QIcon.Normal, QIcon.Off)
        self.storeTextProfile_btn2.setIcon(icon5)
        self.storeTextProfile_btn2.setIconSize(QSize(32, 32))

        self.horizontalLayout_12.addWidget(self.storeTextProfile_btn2, 0, Qt.AlignHCenter)

        self.textProfiles_lbl = QLabel(self.delete_btnFrame2)
        self.textProfiles_lbl.setObjectName(u"textProfiles_lbl")
        sizePolicy2.setHeightForWidth(self.textProfiles_lbl.sizePolicy().hasHeightForWidth())
        self.textProfiles_lbl.setSizePolicy(sizePolicy2)
        self.textProfiles_lbl.setMinimumSize(QSize(106, 20))
        self.textProfiles_lbl.setFont(font1)

        self.horizontalLayout_12.addWidget(self.textProfiles_lbl)

        self.deleteTextProfile_btn = QPushButton(self.delete_btnFrame2)
        self.deleteTextProfile_btn.setObjectName(u"deleteTextProfile_btn")
        self.deleteTextProfile_btn.setMinimumSize(QSize(14, 15))
        self.deleteTextProfile_btn.setMaximumSize(QSize(14, 15))
        self.deleteTextProfile_btn.setStyleSheet(u"QPushButton:pressed{\n"
"	 padding-left: 3px;\n"
"     padding-top: 3px;\n"
"}\n"
"QPushButton{\n"
"background-color: rgba(100,100,100,0);\n"
"border-radius:10px;\n"
"}")
        self.deleteTextProfile_btn.setIcon(icon3)
        self.deleteTextProfile_btn.setIconSize(QSize(14, 15))

        self.horizontalLayout_12.addWidget(self.deleteTextProfile_btn, 0, Qt.AlignRight)


        self.verticalLayout_32.addWidget(self.delete_btnFrame2, 0, Qt.AlignHCenter)

        self.textAreaFrame = QFrame(self.SummaryFrame)
        self.textAreaFrame.setObjectName(u"textAreaFrame")
        sizePolicy2.setHeightForWidth(self.textAreaFrame.sizePolicy().hasHeightForWidth())
        self.textAreaFrame.setSizePolicy(sizePolicy2)
        self.horizontalLayout_9 = QHBoxLayout(self.textAreaFrame)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(10, 10, 10, 10)
        self.textProfiles_list = QComboBox(self.textAreaFrame)
        self.textProfiles_list.setObjectName(u"textProfiles_list")
        sizePolicy2.setHeightForWidth(self.textProfiles_list.sizePolicy().hasHeightForWidth())
        self.textProfiles_list.setSizePolicy(sizePolicy2)
        self.textProfiles_list.setMinimumSize(QSize(211, 41))
        self.textProfiles_list.setFont(font2)
        self.textProfiles_list.setStyleSheet(u"/* Style the QComboBox */\n"
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
        self.textProfiles_list.setMaxVisibleItems(15)

        self.horizontalLayout_9.addWidget(self.textProfiles_list)

        self.applyTextProfile_btn = QPushButton(self.textAreaFrame)
        self.applyTextProfile_btn.setObjectName(u"applyTextProfile_btn")
        self.applyTextProfile_btn.setMinimumSize(QSize(32, 32))
        self.applyTextProfile_btn.setMaximumSize(QSize(32, 32))
        self.applyTextProfile_btn.setStyleSheet(u"QPushButton:pressed{\n"
"	 padding-left: 3px;\n"
"     padding-top: 3px;\n"
"}\n"
"QPushButton{\n"
"background-color: rgba(100,100,100,0);\n"
"border-radius:10px;\n"
"}")
        self.applyTextProfile_btn.setIcon(icon4)
        self.applyTextProfile_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.applyTextProfile_btn)


        self.verticalLayout_32.addWidget(self.textAreaFrame, 0, Qt.AlignHCenter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_32.addItem(self.horizontalSpacer)

        self.parameters_summary_label = QLabel(self.SummaryFrame)
        self.parameters_summary_label.setObjectName(u"parameters_summary_label")
        self.parameters_summary_label.setStyleSheet(u"font: 700 14pt \"Inter\";")
        self.parameters_summary_label.setWordWrap(False)
        self.parameters_summary_label.setMargin(10)
        self.parameters_summary_label.setIndent(-1)
        self.parameters_summary_label.setOpenExternalLinks(False)

        self.verticalLayout_32.addWidget(self.parameters_summary_label, 0, Qt.AlignHCenter)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.repeatWords_btn = QPushButton(self.SummaryFrame)
        self.parametersButtonGroup = QButtonGroup(MainWindow)
        self.parametersButtonGroup.setObjectName(u"parametersButtonGroup")
        self.parametersButtonGroup.addButton(self.repeatWords_btn)
        self.repeatWords_btn.setObjectName(u"repeatWords_btn")
        self.repeatWords_btn.setFont(font2)
        self.repeatWords_btn.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:#e6e6e6;")

        self.horizontalLayout_19.addWidget(self.repeatWords_btn)

        self.repeat_info_label = QLabel(self.SummaryFrame)
        self.repeat_info_label.setObjectName(u"repeat_info_label")
        self.repeat_info_label.setFont(font1)

        self.horizontalLayout_19.addWidget(self.repeat_info_label)


        self.verticalLayout_32.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.marginSettings_btn = QPushButton(self.SummaryFrame)
        self.parametersButtonGroup.addButton(self.marginSettings_btn)
        self.marginSettings_btn.setObjectName(u"marginSettings_btn")
        self.marginSettings_btn.setFont(font2)
        self.marginSettings_btn.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:#e6e6e6;")

        self.horizontalLayout_36.addWidget(self.marginSettings_btn)

        self.margin_info_label = QLabel(self.SummaryFrame)
        self.margin_info_label.setObjectName(u"margin_info_label")
        self.margin_info_label.setFont(font1)

        self.horizontalLayout_36.addWidget(self.margin_info_label)


        self.verticalLayout_32.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.fontSizeSettings_btn = QPushButton(self.SummaryFrame)
        self.parametersButtonGroup.addButton(self.fontSizeSettings_btn)
        self.fontSizeSettings_btn.setObjectName(u"fontSizeSettings_btn")
        self.fontSizeSettings_btn.setFont(font2)
        self.fontSizeSettings_btn.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:#e6e6e6;")

        self.horizontalLayout_37.addWidget(self.fontSizeSettings_btn)

        self.min_font_size_info_label = QLabel(self.SummaryFrame)
        self.min_font_size_info_label.setObjectName(u"min_font_size_info_label")
        self.min_font_size_info_label.setFont(font1)

        self.horizontalLayout_37.addWidget(self.min_font_size_info_label)


        self.verticalLayout_32.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.fontSizeSettings_btn2 = QPushButton(self.SummaryFrame)
        self.parametersButtonGroup.addButton(self.fontSizeSettings_btn2)
        self.fontSizeSettings_btn2.setObjectName(u"fontSizeSettings_btn2")
        self.fontSizeSettings_btn2.setFont(font2)
        self.fontSizeSettings_btn2.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:#e6e6e6;")

        self.horizontalLayout_38.addWidget(self.fontSizeSettings_btn2)

        self.max_font_size_info_label = QLabel(self.SummaryFrame)
        self.max_font_size_info_label.setObjectName(u"max_font_size_info_label")
        self.max_font_size_info_label.setFont(font1)

        self.horizontalLayout_38.addWidget(self.max_font_size_info_label)


        self.verticalLayout_32.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.textOrientationSettings_btn = QPushButton(self.SummaryFrame)
        self.parametersButtonGroup.addButton(self.textOrientationSettings_btn)
        self.textOrientationSettings_btn.setObjectName(u"textOrientationSettings_btn")
        self.textOrientationSettings_btn.setFont(font2)
        self.textOrientationSettings_btn.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:#e6e6e6;")

        self.horizontalLayout_39.addWidget(self.textOrientationSettings_btn)

        self.prefer_horizontal_info_label = QLabel(self.SummaryFrame)
        self.prefer_horizontal_info_label.setObjectName(u"prefer_horizontal_info_label")
        self.prefer_horizontal_info_label.setFont(font1)

        self.horizontalLayout_39.addWidget(self.prefer_horizontal_info_label)


        self.verticalLayout_32.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.fontStepSettings_btn = QPushButton(self.SummaryFrame)
        self.parametersButtonGroup.addButton(self.fontStepSettings_btn)
        self.fontStepSettings_btn.setObjectName(u"fontStepSettings_btn")
        self.fontStepSettings_btn.setFont(font2)
        self.fontStepSettings_btn.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:#e6e6e6;")

        self.horizontalLayout_40.addWidget(self.fontStepSettings_btn)

        self.fontstep_info_label = QLabel(self.SummaryFrame)
        self.fontstep_info_label.setObjectName(u"fontstep_info_label")
        self.fontstep_info_label.setFont(font1)

        self.horizontalLayout_40.addWidget(self.fontstep_info_label)


        self.verticalLayout_32.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.collocationSettings_btn = QPushButton(self.SummaryFrame)
        self.parametersButtonGroup.addButton(self.collocationSettings_btn)
        self.collocationSettings_btn.setObjectName(u"collocationSettings_btn")
        self.collocationSettings_btn.setFont(font2)
        self.collocationSettings_btn.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:#e6e6e6;")

        self.horizontalLayout_41.addWidget(self.collocationSettings_btn)

        self.collocations_info_label = QLabel(self.SummaryFrame)
        self.collocations_info_label.setObjectName(u"collocations_info_label")
        self.collocations_info_label.setFont(font1)

        self.horizontalLayout_41.addWidget(self.collocations_info_label)


        self.verticalLayout_32.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.collocationSettings_btn2 = QPushButton(self.SummaryFrame)
        self.parametersButtonGroup.addButton(self.collocationSettings_btn2)
        self.collocationSettings_btn2.setObjectName(u"collocationSettings_btn2")
        self.collocationSettings_btn2.setFont(font2)
        self.collocationSettings_btn2.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:#e6e6e6;")

        self.horizontalLayout_42.addWidget(self.collocationSettings_btn2)

        self.collocations_thresh_info_label = QLabel(self.SummaryFrame)
        self.collocations_thresh_info_label.setObjectName(u"collocations_thresh_info_label")
        self.collocations_thresh_info_label.setFont(font1)

        self.horizontalLayout_42.addWidget(self.collocations_thresh_info_label)


        self.verticalLayout_32.addLayout(self.horizontalLayout_42)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_32.addItem(self.horizontalSpacer_23)

        self.color_presets_group = QFrame(self.SummaryFrame)
        self.color_presets_group.setObjectName(u"color_presets_group")
        sizePolicy2.setHeightForWidth(self.color_presets_group.sizePolicy().hasHeightForWidth())
        self.color_presets_group.setSizePolicy(sizePolicy2)
        self.color_presets_group.setFont(font)
        self.color_presets_group.setStyleSheet(u"background:none;")
        self.color_presets_group.setFrameShape(QFrame.NoFrame)
        self.color_presets_group.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.color_presets_group)
        self.verticalLayout_18.setSpacing(5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(5, 0, 5, 0)
        self.cp_title_dropdown = QFrame(self.color_presets_group)
        self.cp_title_dropdown.setObjectName(u"cp_title_dropdown")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cp_title_dropdown.sizePolicy().hasHeightForWidth())
        self.cp_title_dropdown.setSizePolicy(sizePolicy3)
        self.cp_title_dropdown.setMaximumSize(QSize(16777215, 100))
        font3 = QFont()
        font3.setFamilies([u"Inter"])
        font3.setPointSize(11)
        self.cp_title_dropdown.setFont(font3)
        self.verticalLayout_19 = QVBoxLayout(self.cp_title_dropdown)
        self.verticalLayout_19.setSpacing(15)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 10, 0, 10)
        self.label_color_presets = QLabel(self.cp_title_dropdown)
        self.label_color_presets.setObjectName(u"label_color_presets")
        self.label_color_presets.setMinimumSize(QSize(0, 0))
        self.label_color_presets.setMaximumSize(QSize(200, 40))
        font4 = QFont()
        font4.setFamilies([u"Inter"])
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setItalic(False)
        self.label_color_presets.setFont(font4)
        self.label_color_presets.setStyleSheet(u"QLabel{\n"
"font: 700 12pt \"Inter\";\n"
"}")
        self.label_color_presets.setTextFormat(Qt.RichText)
        self.label_color_presets.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_color_presets)

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
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.addItem("")
        self.colormaps_dropdown.setObjectName(u"colormaps_dropdown")
        sizePolicy3.setHeightForWidth(self.colormaps_dropdown.sizePolicy().hasHeightForWidth())
        self.colormaps_dropdown.setSizePolicy(sizePolicy3)
        self.colormaps_dropdown.setMinimumSize(QSize(200, 30))
        self.colormaps_dropdown.setMaximumSize(QSize(250, 40))
        self.colormaps_dropdown.setFont(font)
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
"    border-radius:0px;\n"
"}")
        self.colormaps_dropdown.setMaxVisibleItems(15)

        self.verticalLayout_19.addWidget(self.colormaps_dropdown)


        self.verticalLayout_18.addWidget(self.cp_title_dropdown, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.colorEdgeSliderFrame = QFrame(self.color_presets_group)
        self.colorEdgeSliderFrame.setObjectName(u"colorEdgeSliderFrame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.colorEdgeSliderFrame.sizePolicy().hasHeightForWidth())
        self.colorEdgeSliderFrame.setSizePolicy(sizePolicy4)
        self.gridLayout_6 = QGridLayout(self.colorEdgeSliderFrame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.color_detection_thresh_info_lbl = QLabel(self.colorEdgeSliderFrame)
        self.color_detection_thresh_info_lbl.setObjectName(u"color_detection_thresh_info_lbl")
        font5 = QFont()
        font5.setFamilies([u"Inter"])
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setKerning(True)
        self.color_detection_thresh_info_lbl.setFont(font5)
        self.color_detection_thresh_info_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.color_detection_thresh_info_lbl, 2, 0, 1, 1, Qt.AlignHCenter)

        self.color_detection_thresh_lbl = QLabel(self.colorEdgeSliderFrame)
        self.color_detection_thresh_lbl.setObjectName(u"color_detection_thresh_lbl")
        self.color_detection_thresh_lbl.setMaximumSize(QSize(16777215, 30))
        self.color_detection_thresh_lbl.setFont(font5)
        self.color_detection_thresh_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.color_detection_thresh_lbl, 0, 0, 1, 2)

        self.Color_detectionSliderFrame = QFrame(self.colorEdgeSliderFrame)
        self.Color_detectionSliderFrame.setObjectName(u"Color_detectionSliderFrame")
        self.horizontalLayout_11 = QHBoxLayout(self.Color_detectionSliderFrame)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(18, 0, 0, 0)
        self.color_thresh_slider = QSlider(self.Color_detectionSliderFrame)
        self.color_thresh_slider.setObjectName(u"color_thresh_slider")
        self.color_thresh_slider.setMinimumSize(QSize(0, 40))
        self.color_thresh_slider.setMaximumSize(QSize(140, 40))
        self.color_thresh_slider.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_thresh_slider.setMouseTracking(False)
        self.color_thresh_slider.setFocusPolicy(Qt.StrongFocus)
        self.color_thresh_slider.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.color_thresh_slider.setLayoutDirection(Qt.LeftToRight)
        self.color_thresh_slider.setStyleSheet(u"QSlider::groove {\n"
"height: 5px;\n"
"/*width: 350px;*/\n"
"background: grey;\n"
"margin: 3px 0;\n"
"/*border: 2px solid #c17d08;\n"
"border-radius: 2px;*/\n"
"}\n"
"QSlider::handle{\n"
"    background: red;\n"
"    border: none;\n"
"    width: 15px;\n"
"    margin: -10px 0;\n"
"    border-radius: 5px;\n"
"}\n"
"QSlider::add-page {\n"
"height: 10px;\n"
"background: #e9e9e9;\n"
"border: none;\n"
"border-radius: 4px;\n"
"}\n"
"/*QSlider::sub-page {\n"
"background: #c17d08;\n"
"height: 6px;\n"
"border: 1px solid #c17d08;\n"
"border-radius: 12px;\n"
"}*/\n"
"QSlider::sub-page{\n"
"height: 15px;\n"
"background: green;\n"
"border: none;\n"
"border-radius: 5px;\n"
"}")
        self.color_thresh_slider.setMinimum(0)
        self.color_thresh_slider.setMaximum(100)
        self.color_thresh_slider.setPageStep(1)
        self.color_thresh_slider.setValue(10)
        self.color_thresh_slider.setSliderPosition(10)
        self.color_thresh_slider.setOrientation(Qt.Horizontal)
        self.color_thresh_slider.setInvertedControls(False)
        self.color_thresh_slider.setTickPosition(QSlider.NoTicks)
        self.color_thresh_slider.setTickInterval(0)

        self.horizontalLayout_11.addWidget(self.color_thresh_slider)

        self.color_thresh_slider_lbl = QLabel(self.Color_detectionSliderFrame)
        self.color_thresh_slider_lbl.setObjectName(u"color_thresh_slider_lbl")
        self.color_thresh_slider_lbl.setMinimumSize(QSize(34, 40))
        self.color_thresh_slider_lbl.setMaximumSize(QSize(50, 50))
        self.color_thresh_slider_lbl.setFont(font5)
        self.color_thresh_slider_lbl.setMargin(5)
        self.color_thresh_slider_lbl.setIndent(-1)
        self.color_thresh_slider_lbl.setOpenExternalLinks(False)

        self.horizontalLayout_11.addWidget(self.color_thresh_slider_lbl)


        self.gridLayout_6.addWidget(self.Color_detectionSliderFrame, 1, 0, 1, 1)


        self.verticalLayout_18.addWidget(self.colorEdgeSliderFrame, 0, Qt.AlignHCenter)

        self.gradient_settings_btn = QPushButton(self.color_presets_group)
        self.gradient_settings_btn.setObjectName(u"gradient_settings_btn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.gradient_settings_btn.sizePolicy().hasHeightForWidth())
        self.gradient_settings_btn.setSizePolicy(sizePolicy5)
        self.gradient_settings_btn.setMinimumSize(QSize(107, 30))
        font6 = QFont()
        font6.setFamilies([u"Inter"])
        font6.setPointSize(11)
        font6.setBold(True)
        font6.setItalic(False)
        self.gradient_settings_btn.setFont(font6)
        self.gradient_settings_btn.setStyleSheet(u"QPushButton{\n"
"background-color:#212121;\n"
"color:#e6e6e6;\n"
"}")
        self.gradient_settings_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_18.addWidget(self.gradient_settings_btn)

        self.RandomColorFrame = QFrame(self.color_presets_group)
        self.RandomColorFrame.setObjectName(u"RandomColorFrame")
        sizePolicy2.setHeightForWidth(self.RandomColorFrame.sizePolicy().hasHeightForWidth())
        self.RandomColorFrame.setSizePolicy(sizePolicy2)
        self.gridLayout_13 = QGridLayout(self.RandomColorFrame)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setHorizontalSpacing(0)
        self.gridLayout_13.setVerticalSpacing(20)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 20)
        self.rColorRangeContainer_2 = QFrame(self.RandomColorFrame)
        self.rColorRangeContainer_2.setObjectName(u"rColorRangeContainer_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.rColorRangeContainer_2.sizePolicy().hasHeightForWidth())
        self.rColorRangeContainer_2.setSizePolicy(sizePolicy6)
        self.rColorRangeContainer_2.setMaximumSize(QSize(256, 16777215))
        self.rColorRangeContainer_2.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_22 = QVBoxLayout(self.rColorRangeContainer_2)
        self.verticalLayout_22.setSpacing(1)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.color_range_preset_buttons_frame = QFrame(self.rColorRangeContainer_2)
        self.color_range_preset_buttons_frame.setObjectName(u"color_range_preset_buttons_frame")
        sizePolicy3.setHeightForWidth(self.color_range_preset_buttons_frame.sizePolicy().hasHeightForWidth())
        self.color_range_preset_buttons_frame.setSizePolicy(sizePolicy3)
        self.color_range_preset_buttons_frame.setMinimumSize(QSize(100, 50))
        self.color_range_preset_buttons_frame.setMaximumSize(QSize(266, 28))
        self.color_range_preset_buttons_frame.setStyleSheet(u"font: 700 14pt \"Inter\";")
        self.horizontalLayout_52 = QHBoxLayout(self.color_range_preset_buttons_frame)
        self.horizontalLayout_52.setSpacing(20)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.rcp_minimize_red = QPushButton(self.color_range_preset_buttons_frame)
        self.randomColorsPresetsGroup = QButtonGroup(MainWindow)
        self.randomColorsPresetsGroup.setObjectName(u"randomColorsPresetsGroup")
        self.randomColorsPresetsGroup.addButton(self.rcp_minimize_red)
        self.rcp_minimize_red.setObjectName(u"rcp_minimize_red")
        font7 = QFont()
        font7.setFamilies([u"Inter"])
        font7.setPointSize(14)
        font7.setBold(True)
        font7.setItalic(False)
        self.rcp_minimize_red.setFont(font7)
        self.rcp_minimize_red.setStyleSheet(u"color: rgb(250, 0, 0);\n"
"")

        self.horizontalLayout_53.addWidget(self.rcp_minimize_red)

        self.rcp_maximize_red = QPushButton(self.color_range_preset_buttons_frame)
        self.randomColorsPresetsGroup.addButton(self.rcp_maximize_red)
        self.rcp_maximize_red.setObjectName(u"rcp_maximize_red")
        self.rcp_maximize_red.setFont(font7)
        self.rcp_maximize_red.setStyleSheet(u"color: rgb(250, 0, 0);")

        self.horizontalLayout_53.addWidget(self.rcp_maximize_red)


        self.horizontalLayout_52.addLayout(self.horizontalLayout_53)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.rcp_minimize_green = QPushButton(self.color_range_preset_buttons_frame)
        self.randomColorsPresetsGroup.addButton(self.rcp_minimize_green)
        self.rcp_minimize_green.setObjectName(u"rcp_minimize_green")
        self.rcp_minimize_green.setFont(font7)
        self.rcp_minimize_green.setStyleSheet(u"color: rgb(0, 250, 0);")

        self.horizontalLayout_54.addWidget(self.rcp_minimize_green)

        self.rcp_maximize_green = QPushButton(self.color_range_preset_buttons_frame)
        self.randomColorsPresetsGroup.addButton(self.rcp_maximize_green)
        self.rcp_maximize_green.setObjectName(u"rcp_maximize_green")
        self.rcp_maximize_green.setFont(font7)
        self.rcp_maximize_green.setStyleSheet(u"color: rgb(0, 250, 0);")

        self.horizontalLayout_54.addWidget(self.rcp_maximize_green)


        self.horizontalLayout_52.addLayout(self.horizontalLayout_54)

        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.rcp_maximize_blue = QPushButton(self.color_range_preset_buttons_frame)
        self.randomColorsPresetsGroup.addButton(self.rcp_maximize_blue)
        self.rcp_maximize_blue.setObjectName(u"rcp_maximize_blue")
        self.rcp_maximize_blue.setFont(font7)
        self.rcp_maximize_blue.setStyleSheet(u"color: rgb(0, 0, 250);")

        self.horizontalLayout_55.addWidget(self.rcp_maximize_blue)

        self.rcp_minimize_blue = QPushButton(self.color_range_preset_buttons_frame)
        self.randomColorsPresetsGroup.addButton(self.rcp_minimize_blue)
        self.rcp_minimize_blue.setObjectName(u"rcp_minimize_blue")
        self.rcp_minimize_blue.setFont(font7)
        self.rcp_minimize_blue.setStyleSheet(u"color: rgb(0, 0, 250);")

        self.horizontalLayout_55.addWidget(self.rcp_minimize_blue)


        self.horizontalLayout_52.addLayout(self.horizontalLayout_55)


        self.verticalLayout_22.addWidget(self.color_range_preset_buttons_frame, 0, Qt.AlignHCenter)

        self.ColorsMinGP = QGroupBox(self.rColorRangeContainer_2)
        self.ColorsMinGP.setObjectName(u"ColorsMinGP")
        sizePolicy2.setHeightForWidth(self.ColorsMinGP.sizePolicy().hasHeightForWidth())
        self.ColorsMinGP.setSizePolicy(sizePolicy2)
        self.ColorsMinGP.setMaximumSize(QSize(16777215, 71))
        self.horizontalLayout_56 = QHBoxLayout(self.ColorsMinGP)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.red_min = QSpinBox(self.ColorsMinGP)
        self.red_min.setObjectName(u"red_min")
        self.red_min.setMinimumSize(QSize(60, 30))
        self.red_min.setMaximumSize(QSize(60, 30))
        self.red_min.setFont(font)
        self.red_min.setStyleSheet(u"background-color: rgb(200, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.red_min.setAccelerated(True)
        self.red_min.setMinimum(0)
        self.red_min.setMaximum(255)
        self.red_min.setValue(20)

        self.horizontalLayout_56.addWidget(self.red_min, 0, Qt.AlignHCenter)

        self.green_min = QSpinBox(self.ColorsMinGP)
        self.green_min.setObjectName(u"green_min")
        self.green_min.setMinimumSize(QSize(60, 30))
        self.green_min.setMaximumSize(QSize(60, 30))
        self.green_min.setFont(font)
        self.green_min.setStyleSheet(u"background-color: rgb(0, 200, 0);\n"
"color: rgb(25, 25, 25);")
        self.green_min.setAccelerated(True)
        self.green_min.setMaximum(255)
        self.green_min.setValue(20)

        self.horizontalLayout_56.addWidget(self.green_min)

        self.blue_min = QSpinBox(self.ColorsMinGP)
        self.blue_min.setObjectName(u"blue_min")
        self.blue_min.setMinimumSize(QSize(60, 30))
        self.blue_min.setMaximumSize(QSize(60, 30))
        self.blue_min.setFont(font)
        self.blue_min.setStyleSheet(u"background-color: rgb(0, 0, 200);\n"
"color: rgb(255, 255, 255);")
        self.blue_min.setAccelerated(True)
        self.blue_min.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.blue_min.setMaximum(255)
        self.blue_min.setStepType(QAbstractSpinBox.DefaultStepType)
        self.blue_min.setValue(20)

        self.horizontalLayout_56.addWidget(self.blue_min)


        self.verticalLayout_22.addWidget(self.ColorsMinGP, 0, Qt.AlignHCenter)

        self.rcpresets3 = QFrame(self.rColorRangeContainer_2)
        self.rcpresets3.setObjectName(u"rcpresets3")
        sizePolicy2.setHeightForWidth(self.rcpresets3.sizePolicy().hasHeightForWidth())
        self.rcpresets3.setSizePolicy(sizePolicy2)
        self.gridLayout_10 = QGridLayout(self.rcpresets3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")

        self.verticalLayout_22.addWidget(self.rcpresets3, 0, Qt.AlignHCenter)

        self.ColorsMaxGP = QGroupBox(self.rColorRangeContainer_2)
        self.ColorsMaxGP.setObjectName(u"ColorsMaxGP")
        sizePolicy4.setHeightForWidth(self.ColorsMaxGP.sizePolicy().hasHeightForWidth())
        self.ColorsMaxGP.setSizePolicy(sizePolicy4)
        self.ColorsMaxGP.setMaximumSize(QSize(16777215, 71))
        self.horizontalLayout_57 = QHBoxLayout(self.ColorsMaxGP)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.red_max = QSpinBox(self.ColorsMaxGP)
        self.red_max.setObjectName(u"red_max")
        self.red_max.setMinimumSize(QSize(60, 30))
        self.red_max.setMaximumSize(QSize(60, 30))
        self.red_max.setFont(font)
        self.red_max.setStyleSheet(u"background-color: rgb(200, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.red_max.setAccelerated(True)
        self.red_max.setMinimum(0)
        self.red_max.setMaximum(255)
        self.red_max.setValue(150)

        self.horizontalLayout_57.addWidget(self.red_max, 0, Qt.AlignHCenter)

        self.green_max = QSpinBox(self.ColorsMaxGP)
        self.green_max.setObjectName(u"green_max")
        self.green_max.setMinimumSize(QSize(60, 30))
        self.green_max.setMaximumSize(QSize(60, 30))
        self.green_max.setFont(font)
        self.green_max.setStyleSheet(u"background-color: rgb(0, 200, 0);\n"
"color: rgb(25, 25, 25);")
        self.green_max.setAccelerated(True)
        self.green_max.setMaximum(255)
        self.green_max.setValue(250)

        self.horizontalLayout_57.addWidget(self.green_max, 0, Qt.AlignHCenter)

        self.blue_max = QSpinBox(self.ColorsMaxGP)
        self.blue_max.setObjectName(u"blue_max")
        self.blue_max.setMinimumSize(QSize(60, 30))
        self.blue_max.setMaximumSize(QSize(60, 30))
        self.blue_max.setFont(font)
        self.blue_max.setStyleSheet(u"background-color: rgb(0, 0, 200);\n"
"color: rgb(255, 255, 255);")
        self.blue_max.setAccelerated(True)
        self.blue_max.setMaximum(255)
        self.blue_max.setValue(150)

        self.horizontalLayout_57.addWidget(self.blue_max, 0, Qt.AlignHCenter)


        self.verticalLayout_22.addWidget(self.ColorsMaxGP, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_13.addWidget(self.rColorRangeContainer_2, 1, 0, 1, 1)

        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.rcp_bright = QPushButton(self.RandomColorFrame)
        self.randomColorsPresetsGroup.addButton(self.rcp_bright)
        self.rcp_bright.setObjectName(u"rcp_bright")
        sizePolicy2.setHeightForWidth(self.rcp_bright.sizePolicy().hasHeightForWidth())
        self.rcp_bright.setSizePolicy(sizePolicy2)
        self.rcp_bright.setFont(font1)

        self.horizontalLayout_58.addWidget(self.rcp_bright)

        self.rcp_gray = QPushButton(self.RandomColorFrame)
        self.randomColorsPresetsGroup.addButton(self.rcp_gray)
        self.rcp_gray.setObjectName(u"rcp_gray")
        sizePolicy2.setHeightForWidth(self.rcp_gray.sizePolicy().hasHeightForWidth())
        self.rcp_gray.setSizePolicy(sizePolicy2)
        self.rcp_gray.setFont(font1)

        self.horizontalLayout_58.addWidget(self.rcp_gray)

        self.rcp_dark = QPushButton(self.RandomColorFrame)
        self.randomColorsPresetsGroup.addButton(self.rcp_dark)
        self.rcp_dark.setObjectName(u"rcp_dark")
        sizePolicy2.setHeightForWidth(self.rcp_dark.sizePolicy().hasHeightForWidth())
        self.rcp_dark.setSizePolicy(sizePolicy2)
        self.rcp_dark.setFont(font1)

        self.horizontalLayout_58.addWidget(self.rcp_dark)

        self.rcp_reset = QPushButton(self.RandomColorFrame)
        self.randomColorsPresetsGroup.addButton(self.rcp_reset)
        self.rcp_reset.setObjectName(u"rcp_reset")
        sizePolicy2.setHeightForWidth(self.rcp_reset.sizePolicy().hasHeightForWidth())
        self.rcp_reset.setSizePolicy(sizePolicy2)
        self.rcp_reset.setFont(font1)

        self.horizontalLayout_58.addWidget(self.rcp_reset)


        self.gridLayout_13.addLayout(self.horizontalLayout_58, 2, 0, 1, 1)

        self.rColorRangeContainer = QFrame(self.RandomColorFrame)
        self.rColorRangeContainer.setObjectName(u"rColorRangeContainer")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.rColorRangeContainer.sizePolicy().hasHeightForWidth())
        self.rColorRangeContainer.setSizePolicy(sizePolicy7)
        self.rColorRangeContainer.setMaximumSize(QSize(256, 16777215))
        self.rColorRangeContainer.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_20 = QVBoxLayout(self.rColorRangeContainer)
        self.verticalLayout_20.setSpacing(1)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_13.addWidget(self.rColorRangeContainer, 0, 0, 1, 1)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.colp_pink_btn = QPushButton(self.RandomColorFrame)
        self.randomColorsPresetsGroup.addButton(self.colp_pink_btn)
        self.colp_pink_btn.setObjectName(u"colp_pink_btn")
        self.colp_pink_btn.setEnabled(True)
        self.colp_pink_btn.setMinimumSize(QSize(32, 32))
        self.colp_pink_btn.setMaximumSize(QSize(32, 32))
        self.colp_pink_btn.setFont(font)
        self.colp_pink_btn.setStyleSheet(u"QPushButton{\n"
"background: #ff00ff;\n"
"border-radius: 4px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:rgba(100,100,100,100)\n"
"}")

        self.horizontalLayout_60.addWidget(self.colp_pink_btn)

        self.colp_wpp_btn = QPushButton(self.RandomColorFrame)
        self.randomColorsPresetsGroup.addButton(self.colp_wpp_btn)
        self.colp_wpp_btn.setObjectName(u"colp_wpp_btn")
        self.colp_wpp_btn.setEnabled(True)
        self.colp_wpp_btn.setMinimumSize(QSize(32, 32))
        self.colp_wpp_btn.setMaximumSize(QSize(32, 32))
        self.colp_wpp_btn.setFont(font)
        self.colp_wpp_btn.setStyleSheet(u"QPushButton{\n"
"background:#590d3b;\n"
"border-radius:3px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:rgba(100,100,100,100)\n"
"}")

        self.horizontalLayout_60.addWidget(self.colp_wpp_btn)

        self.colp_14_btn = QPushButton(self.RandomColorFrame)
        self.randomColorsPresetsGroup.addButton(self.colp_14_btn)
        self.colp_14_btn.setObjectName(u"colp_14_btn")
        self.colp_14_btn.setEnabled(True)
        self.colp_14_btn.setMinimumSize(QSize(32, 32))
        self.colp_14_btn.setMaximumSize(QSize(32, 32))
        self.colp_14_btn.setFont(font)
        self.colp_14_btn.setStyleSheet(u"QPushButton{\n"
"background:#141414;\n"
"border-radius:3px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:rgba(100,100,100,100)\n"
"}")

        self.horizontalLayout_60.addWidget(self.colp_14_btn)

        self.colp_e6_btn = QPushButton(self.RandomColorFrame)
        self.randomColorsPresetsGroup.addButton(self.colp_e6_btn)
        self.colp_e6_btn.setObjectName(u"colp_e6_btn")
        self.colp_e6_btn.setEnabled(True)
        self.colp_e6_btn.setMinimumSize(QSize(32, 32))
        self.colp_e6_btn.setMaximumSize(QSize(32, 32))
        self.colp_e6_btn.setFont(font)
        self.colp_e6_btn.setStyleSheet(u"QPushButton{\n"
"background:#e6e6e6;\n"
"border-radius:3px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:rgba(100,100,100,100)\n"
"}")

        self.horizontalLayout_60.addWidget(self.colp_e6_btn)


        self.gridLayout_13.addLayout(self.horizontalLayout_60, 3, 0, 1, 1)


        self.verticalLayout_18.addWidget(self.RandomColorFrame, 0, Qt.AlignHCenter)


        self.verticalLayout_32.addWidget(self.color_presets_group, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_32.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.SummaryFrame, 0, 0, 3, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy8)
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        sizePolicy7.setHeightForWidth(self.page1.sizePolicy().hasHeightForWidth())
        self.page1.setSizePolicy(sizePolicy7)
        self.gridLayout_2 = QGridLayout(self.page1)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(0, 10, 0, 0)
        self.WordInputAndParametersFrame = QFrame(self.page1)
        self.WordInputAndParametersFrame.setObjectName(u"WordInputAndParametersFrame")
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.WordInputAndParametersFrame.sizePolicy().hasHeightForWidth())
        self.WordInputAndParametersFrame.setSizePolicy(sizePolicy9)
        self.WordInputAndParametersFrame.setMaximumSize(QSize(16777215, 1400))
        self.gridLayout_3 = QGridLayout(self.WordInputAndParametersFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(10)
        self.gridLayout_3.setContentsMargins(0, 10, 0, 10)
        self.parameters_window = QTabWidget(self.WordInputAndParametersFrame)
        self.parameters_window.setObjectName(u"parameters_window")
        self.parameters_window.setEnabled(True)
        sizePolicy10 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.parameters_window.sizePolicy().hasHeightForWidth())
        self.parameters_window.setSizePolicy(sizePolicy10)
        self.parameters_window.setMaximumSize(QSize(16777215, 16777215))
        font8 = QFont()
        font8.setFamilies([u"Inter"])
        font8.setPointSize(9)
        font8.setBold(True)
        font8.setItalic(False)
        font8.setKerning(True)
        self.parameters_window.setFont(font8)
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
        self.label.setFont(font8)
        self.label.setTextFormat(Qt.MarkdownText)

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
        self.repeat_words_label.setFont(font8)
        self.repeat_words_label.setTextFormat(Qt.MarkdownText)

        self.horizontalLayout_27.addWidget(self.repeat_words_label)

        self.repeat_checkbox = QPushButton(self.RepeatFrame)
        self.repeat_checkbox.setObjectName(u"repeat_checkbox")
        self.repeat_checkbox.setMinimumSize(QSize(41, 41))
        self.repeat_checkbox.setMaximumSize(QSize(41, 41))
        font9 = QFont()
        font9.setFamilies([u"Segoe UI"])
        font9.setPointSize(9)
        font9.setBold(True)
        font9.setItalic(False)
        font9.setKerning(True)
        self.repeat_checkbox.setFont(font9)
        self.repeat_checkbox.setStyleSheet(u"QPushButton {\n"
"    background-color: #e0e0e0;\n"
"    border: 2px solid #141414;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* Style for the checked state */\n"
"QPushButton:checked {\n"
"    background-color: #4CAF50;  /* Change the background color when checked*/\n"
"    color: white; /* Change the text color when checked */\n"
"	border:2px solid #141414;\n"
"}")
        self.repeat_checkbox.setIconSize(QSize(70, 70))
        self.repeat_checkbox.setCheckable(True)
        self.repeat_checkbox.setChecked(True)
        self.repeat_checkbox.setAutoRepeat(False)
        self.repeat_checkbox.setAutoExclusive(False)

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
        self.min_max_fontSize_lbl = QLabel(self.parameters_windowPage)
        self.min_max_fontSize_lbl.setObjectName(u"min_max_fontSize_lbl")
        sizePolicy2.setHeightForWidth(self.min_max_fontSize_lbl.sizePolicy().hasHeightForWidth())
        self.min_max_fontSize_lbl.setSizePolicy(sizePolicy2)
        self.min_max_fontSize_lbl.setMinimumSize(QSize(231, 50))
        self.min_max_fontSize_lbl.setMaximumSize(QSize(231, 50))
        self.min_max_fontSize_lbl.setFont(font8)
        self.min_max_fontSize_lbl.setTextFormat(Qt.MarkdownText)

        self.verticalLayout_16.addWidget(self.min_max_fontSize_lbl, 0, Qt.AlignHCenter)

        self.frame_29 = QFrame(self.parameters_windowPage)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(0, 0))
        self.frame_29.setStyleSheet(u"")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_29)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.minFontSizeFrame = QFrame(self.frame_29)
        self.minFontSizeFrame.setObjectName(u"minFontSizeFrame")
        sizePolicy2.setHeightForWidth(self.minFontSizeFrame.sizePolicy().hasHeightForWidth())
        self.minFontSizeFrame.setSizePolicy(sizePolicy2)
        self.horizontalLayout_28 = QHBoxLayout(self.minFontSizeFrame)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.min_font_size_label = QLabel(self.minFontSizeFrame)
        self.min_font_size_label.setObjectName(u"min_font_size_label")
        self.min_font_size_label.setMaximumSize(QSize(150, 100))
        self.min_font_size_label.setFont(font8)
        self.min_font_size_label.setTextFormat(Qt.MarkdownText)

        self.horizontalLayout_28.addWidget(self.min_font_size_label)

        self.min_font_size_slider = QSlider(self.minFontSizeFrame)
        self.min_font_size_slider.setObjectName(u"min_font_size_slider")
        self.min_font_size_slider.setEnabled(True)
        self.min_font_size_slider.setMinimumSize(QSize(30, 200))
        self.min_font_size_slider.setMaximumSize(QSize(30, 16777215))
        self.min_font_size_slider.setSizeIncrement(QSize(10, 0))
        self.min_font_size_slider.setFont(font8)
        self.min_font_size_slider.setCursor(QCursor(Qt.PointingHandCursor))
        self.min_font_size_slider.setMouseTracking(True)
        self.min_font_size_slider.setFocusPolicy(Qt.ClickFocus)
        self.min_font_size_slider.setStyleSheet(u"")
        self.min_font_size_slider.setMinimum(1)
        self.min_font_size_slider.setMaximum(100)
        self.min_font_size_slider.setPageStep(1)
        self.min_font_size_slider.setValue(2)
        self.min_font_size_slider.setOrientation(Qt.Vertical)

        self.horizontalLayout_28.addWidget(self.min_font_size_slider)

        self.label_min_font_size_slider = QLabel(self.minFontSizeFrame)
        self.label_min_font_size_slider.setObjectName(u"label_min_font_size_slider")
        sizePolicy2.setHeightForWidth(self.label_min_font_size_slider.sizePolicy().hasHeightForWidth())
        self.label_min_font_size_slider.setSizePolicy(sizePolicy2)
        self.label_min_font_size_slider.setMinimumSize(QSize(50, 0))
        self.label_min_font_size_slider.setMaximumSize(QSize(50, 50))
        font10 = QFont()
        font10.setFamilies([u"Inter"])
        font10.setPointSize(14)
        font10.setBold(True)
        font10.setItalic(False)
        font10.setKerning(True)
        self.label_min_font_size_slider.setFont(font10)

        self.horizontalLayout_28.addWidget(self.label_min_font_size_slider)

        self.MinFSp_Frame_3 = QFrame(self.minFontSizeFrame)
        self.MinFSp_Frame_3.setObjectName(u"MinFSp_Frame_3")
        self.MinFSp_Frame_3.setMinimumSize(QSize(52, 140))
        self.MinFSp_Frame_3.setMaximumSize(QSize(52, 16777215))
        self.MinFSp_Frame_3.setFont(font8)
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


        self.verticalLayout_37.addWidget(self.minFontSizeFrame)

        self.MaxFontSizeFrame = QFrame(self.frame_29)
        self.MaxFontSizeFrame.setObjectName(u"MaxFontSizeFrame")
        sizePolicy6.setHeightForWidth(self.MaxFontSizeFrame.sizePolicy().hasHeightForWidth())
        self.MaxFontSizeFrame.setSizePolicy(sizePolicy6)
        self.horizontalLayout_4 = QHBoxLayout(self.MaxFontSizeFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.max_font_size_label = QLabel(self.MaxFontSizeFrame)
        self.max_font_size_label.setObjectName(u"max_font_size_label")
        self.max_font_size_label.setMaximumSize(QSize(150, 100))
        self.max_font_size_label.setFont(font8)
        self.max_font_size_label.setTextFormat(Qt.MarkdownText)

        self.horizontalLayout_4.addWidget(self.max_font_size_label)

        self.max_font_size_slider = QSlider(self.MaxFontSizeFrame)
        self.max_font_size_slider.setObjectName(u"max_font_size_slider")
        self.max_font_size_slider.setEnabled(True)
        self.max_font_size_slider.setMinimumSize(QSize(30, 200))
        self.max_font_size_slider.setMaximumSize(QSize(30, 16777215))
        self.max_font_size_slider.setSizeIncrement(QSize(10, 0))
        self.max_font_size_slider.setFont(font8)
        self.max_font_size_slider.setCursor(QCursor(Qt.PointingHandCursor))
        self.max_font_size_slider.setMouseTracking(True)
        self.max_font_size_slider.setFocusPolicy(Qt.ClickFocus)
        self.max_font_size_slider.setStyleSheet(u"")
        self.max_font_size_slider.setMinimum(10)
        self.max_font_size_slider.setMaximum(300)
        self.max_font_size_slider.setPageStep(1)
        self.max_font_size_slider.setValue(28)
        self.max_font_size_slider.setOrientation(Qt.Vertical)

        self.horizontalLayout_4.addWidget(self.max_font_size_slider)

        self.label_max_font_size_slider = QLabel(self.MaxFontSizeFrame)
        self.label_max_font_size_slider.setObjectName(u"label_max_font_size_slider")
        sizePolicy2.setHeightForWidth(self.label_max_font_size_slider.sizePolicy().hasHeightForWidth())
        self.label_max_font_size_slider.setSizePolicy(sizePolicy2)
        self.label_max_font_size_slider.setMinimumSize(QSize(50, 0))
        self.label_max_font_size_slider.setMaximumSize(QSize(50, 50))
        self.label_max_font_size_slider.setFont(font10)

        self.horizontalLayout_4.addWidget(self.label_max_font_size_slider)

        self.MaxFSp_Frame = QFrame(self.MaxFontSizeFrame)
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


        self.verticalLayout_37.addWidget(self.MaxFontSizeFrame)


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
        self.frame_30 = QFrame(self.frame_font_step)
        self.frame_30.setObjectName(u"frame_30")
        self.horizontalLayout_30 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_46)

        self.fontstep_label = QLabel(self.frame_30)
        self.fontstep_label.setObjectName(u"fontstep_label")
        self.fontstep_label.setMaximumSize(QSize(16777215, 50))
        self.fontstep_label.setFont(font8)
        self.fontstep_label.setTextFormat(Qt.MarkdownText)

        self.horizontalLayout_30.addWidget(self.fontstep_label)

        self.font_step_slider = QSlider(self.frame_30)
        self.font_step_slider.setObjectName(u"font_step_slider")
        self.font_step_slider.setMinimumSize(QSize(30, 150))
        self.font_step_slider.setMaximumSize(QSize(30, 150))
        self.font_step_slider.setCursor(QCursor(Qt.PointingHandCursor))
        self.font_step_slider.setStyleSheet(u"")
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
        self.font_step_indicator_label.setFont(font10)

        self.horizontalLayout_30.addWidget(self.font_step_indicator_label, 0, Qt.AlignHCenter)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_47)


        self.gridLayout_9.addWidget(self.frame_30, 1, 1, 1, 1)

        self.horizontalSpacer_48 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_48, 0, 2, 1, 1)

        self.horizontalSpacer_49 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_49, 0, 0, 1, 1)

        self.label_2 = QLabel(self.frame_font_step)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setFont(font8)
        self.label_2.setTextFormat(Qt.MarkdownText)

        self.gridLayout_9.addWidget(self.label_2, 0, 1, 1, 1)


        self.verticalLayout_40.addWidget(self.frame_font_step)

        self.parameters_window.addTab(self.tab_5, "")
        self.parameters_windowPage3 = QWidget()
        self.parameters_windowPage3.setObjectName(u"parameters_windowPage3")
        self.verticalLayout_41 = QVBoxLayout(self.parameters_windowPage3)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.label_21 = QLabel(self.parameters_windowPage3)
        self.label_21.setObjectName(u"label_21")
        sizePolicy3.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy3)
        self.label_21.setFont(font8)
        self.label_21.setTextFormat(Qt.MarkdownText)

        self.verticalLayout_41.addWidget(self.label_21, 0, Qt.AlignHCenter)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_10)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalSpacer_50 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_50)

        self.margin_label = QLabel(self.parameters_windowPage3)
        self.margin_label.setObjectName(u"margin_label")
        sizePolicy2.setHeightForWidth(self.margin_label.sizePolicy().hasHeightForWidth())
        self.margin_label.setSizePolicy(sizePolicy2)
        self.margin_label.setMaximumSize(QSize(250, 100))
        self.margin_label.setFont(font8)
        self.margin_label.setTextFormat(Qt.MarkdownText)
        self.margin_label.setWordWrap(False)
        self.margin_label.setMargin(0)

        self.horizontalLayout_33.addWidget(self.margin_label)

        self.margin_slider = QSlider(self.parameters_windowPage3)
        self.margin_slider.setObjectName(u"margin_slider")
        self.margin_slider.setEnabled(True)
        self.margin_slider.setMinimumSize(QSize(30, 0))
        self.margin_slider.setMaximumSize(QSize(30, 16777215))
        self.margin_slider.setSizeIncrement(QSize(10, 0))
        self.margin_slider.setFont(font8)
        self.margin_slider.setCursor(QCursor(Qt.PointingHandCursor))
        self.margin_slider.setMouseTracking(True)
        self.margin_slider.setFocusPolicy(Qt.StrongFocus)
        self.margin_slider.setStyleSheet(u"")
        self.margin_slider.setMinimum(0)
        self.margin_slider.setMaximum(30)
        self.margin_slider.setPageStep(1)
        self.margin_slider.setValue(4)
        self.margin_slider.setOrientation(Qt.Vertical)

        self.horizontalLayout_33.addWidget(self.margin_slider)

        self.label_margin_slider = QLabel(self.parameters_windowPage3)
        self.label_margin_slider.setObjectName(u"label_margin_slider")
        self.label_margin_slider.setMinimumSize(QSize(50, 0))
        self.label_margin_slider.setMaximumSize(QSize(50, 50))
        self.label_margin_slider.setFont(font10)
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
        self.label_22.setFont(font8)
        self.label_22.setTextFormat(Qt.MarkdownText)

        self.verticalLayout_43.addWidget(self.label_22, 0, Qt.AlignHCenter)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalSpacer_52 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_52)

        self.prefer_horizontal_label = QLabel(self.frame_31)
        self.prefer_horizontal_label.setObjectName(u"prefer_horizontal_label")
        self.prefer_horizontal_label.setMaximumSize(QSize(250, 100))
        self.prefer_horizontal_label.setFont(font8)
        self.prefer_horizontal_label.setTextFormat(Qt.MarkdownText)

        self.horizontalLayout_34.addWidget(self.prefer_horizontal_label)

        self.prefer_horizontal_slider = QSlider(self.frame_31)
        self.prefer_horizontal_slider.setObjectName(u"prefer_horizontal_slider")
        self.prefer_horizontal_slider.setEnabled(True)
        self.prefer_horizontal_slider.setMinimumSize(QSize(30, 0))
        self.prefer_horizontal_slider.setMaximumSize(QSize(30, 16777215))
        self.prefer_horizontal_slider.setSizeIncrement(QSize(10, 0))
        self.prefer_horizontal_slider.setCursor(QCursor(Qt.PointingHandCursor))
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
        self.label_text_orientation_slider.setFont(font10)

        self.horizontalLayout_34.addWidget(self.label_text_orientation_slider)

        self.horizontalSpacer_53 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_53)


        self.verticalLayout_43.addLayout(self.horizontalLayout_34)

        self.verticalSpacer_28 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_43.addItem(self.verticalSpacer_28)


        self.verticalLayout_42.addWidget(self.frame_31)

        self.parameters_window.addTab(self.parameters_windowPage4, "")
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
        self.stopwords = QTextEdit(self.frame_33)
        self.stopwords.setObjectName(u"stopwords")
        sizePolicy11 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.stopwords.sizePolicy().hasHeightForWidth())
        self.stopwords.setSizePolicy(sizePolicy11)
        self.stopwords.setFont(font6)
        self.stopwords.setStyleSheet(u"")
        self.stopwords.setFrameShadow(QFrame.Plain)
        self.stopwords.setLineWidth(1)
        self.stopwords.setTabChangesFocus(False)
        self.stopwords.setUndoRedoEnabled(True)

        self.gridLayout_22.addWidget(self.stopwords, 1, 0, 1, 1)

        self.verticalSpacer_31 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_22.addItem(self.verticalSpacer_31, 2, 0, 1, 1)

        self.lbl_stopwords = QLabel(self.frame_33)
        self.lbl_stopwords.setObjectName(u"lbl_stopwords")
        self.lbl_stopwords.setFont(font8)
        self.lbl_stopwords.setTextFormat(Qt.MarkdownText)
        self.lbl_stopwords.setMargin(20)

        self.gridLayout_22.addWidget(self.lbl_stopwords, 0, 0, 1, 1, Qt.AlignHCenter)


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
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(10, 0, 10, 20)
        self.label_25 = QLabel(self.frame_35)
        self.label_25.setObjectName(u"label_25")
        font11 = QFont()
        font11.setFamilies([u"Inter"])
        font11.setPointSize(11)
        font11.setBold(True)
        font11.setItalic(False)
        font11.setKerning(True)
        self.label_25.setFont(font11)

        self.gridLayout_23.addWidget(self.label_25, 1, 0, 1, 1, Qt.AlignHCenter)

        self.frame_37 = QFrame(self.frame_35)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_37)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.label_26 = QLabel(self.frame_37)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font8)
        self.label_26.setTextFormat(Qt.MarkdownText)

        self.verticalLayout_47.addWidget(self.label_26, 0, Qt.AlignHCenter)

        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.horizontalLayout_47 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_47.setSpacing(10)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(10, 0, 10, 0)
        self.horizontalSpacer_60 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_60)

        self.label_collocations = QLabel(self.frame_38)
        self.label_collocations.setObjectName(u"label_collocations")
        self.label_collocations.setFont(font8)
        self.label_collocations.setTextFormat(Qt.MarkdownText)

        self.horizontalLayout_47.addWidget(self.label_collocations)

        self.collocations_checkbox = QPushButton(self.frame_38)
        self.collocations_checkbox.setObjectName(u"collocations_checkbox")
        self.collocations_checkbox.setMinimumSize(QSize(41, 41))
        self.collocations_checkbox.setMaximumSize(QSize(41, 41))
        self.collocations_checkbox.setFont(font9)
        self.collocations_checkbox.setStyleSheet(u"QPushButton {\n"
"    background-color: #e0e0e0;\n"
"    border: 2px solid #141414;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* Style for the checked state */\n"
"QPushButton:checked {\n"
"    background-color: #4CAF50; /* Change the background color when checked */\n"
"    color: white; /* Change the text color when checked */\n"
"	border:2px solid #141414;\n"
"}")
        self.collocations_checkbox.setIconSize(QSize(70, 70))
        self.collocations_checkbox.setCheckable(True)
        self.collocations_checkbox.setChecked(False)
        self.collocations_checkbox.setAutoRepeat(False)
        self.collocations_checkbox.setAutoExclusive(False)

        self.horizontalLayout_47.addWidget(self.collocations_checkbox)

        self.frame_36 = QFrame(self.frame_38)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(289, 150))
        self.frame_36.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout_46 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_collocations_thresh = QLabel(self.frame_36)
        self.label_collocations_thresh.setObjectName(u"label_collocations_thresh")
        sizePolicy6.setHeightForWidth(self.label_collocations_thresh.sizePolicy().hasHeightForWidth())
        self.label_collocations_thresh.setSizePolicy(sizePolicy6)
        self.label_collocations_thresh.setFont(font8)
        self.label_collocations_thresh.setTextFormat(Qt.MarkdownText)

        self.horizontalLayout_46.addWidget(self.label_collocations_thresh)

        self.collocations_thresh_slider = QSlider(self.frame_36)
        self.collocations_thresh_slider.setObjectName(u"collocations_thresh_slider")
        self.collocations_thresh_slider.setEnabled(True)
        self.collocations_thresh_slider.setMinimumSize(QSize(30, 0))
        self.collocations_thresh_slider.setMaximumSize(QSize(30, 16777215))
        self.collocations_thresh_slider.setCursor(QCursor(Qt.PointingHandCursor))
        self.collocations_thresh_slider.setMinimum(0)
        self.collocations_thresh_slider.setMaximum(100)
        self.collocations_thresh_slider.setPageStep(1)
        self.collocations_thresh_slider.setOrientation(Qt.Vertical)

        self.horizontalLayout_46.addWidget(self.collocations_thresh_slider)

        self.collocation_thresh_slider_label = QLabel(self.frame_36)
        self.collocation_thresh_slider_label.setObjectName(u"collocation_thresh_slider_label")
        self.collocation_thresh_slider_label.setMaximumSize(QSize(50, 50))
        self.collocation_thresh_slider_label.setFont(font10)

        self.horizontalLayout_46.addWidget(self.collocation_thresh_slider_label)


        self.horizontalLayout_47.addWidget(self.frame_36)

        self.horizontalSpacer_61 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_61)


        self.verticalLayout_47.addWidget(self.frame_38)


        self.gridLayout_23.addWidget(self.frame_37, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_23.addItem(self.verticalSpacer_2, 2, 0, 1, 1)


        self.verticalLayout_46.addWidget(self.frame_35)

        self.parameters_window.addTab(self.parameters_windowPage8, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_5 = QGridLayout(self.tab_6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.CharacterInclusionOptionsFrame = QFrame(self.tab_6)
        self.CharacterInclusionOptionsFrame.setObjectName(u"CharacterInclusionOptionsFrame")
        sizePolicy7.setHeightForWidth(self.CharacterInclusionOptionsFrame.sizePolicy().hasHeightForWidth())
        self.CharacterInclusionOptionsFrame.setSizePolicy(sizePolicy7)
        self.verticalLayout_4 = QVBoxLayout(self.CharacterInclusionOptionsFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 150)
        self.character_filtering_lbl = QLabel(self.CharacterInclusionOptionsFrame)
        self.character_filtering_lbl.setObjectName(u"character_filtering_lbl")
        sizePolicy.setHeightForWidth(self.character_filtering_lbl.sizePolicy().hasHeightForWidth())
        self.character_filtering_lbl.setSizePolicy(sizePolicy)
        self.character_filtering_lbl.setFont(font8)
        self.character_filtering_lbl.setTextFormat(Qt.MarkdownText)

        self.verticalLayout_4.addWidget(self.character_filtering_lbl)

        self.HeterogeneousFrame = QFrame(self.CharacterInclusionOptionsFrame)
        self.HeterogeneousFrame.setObjectName(u"HeterogeneousFrame")
        sizePolicy3.setHeightForWidth(self.HeterogeneousFrame.sizePolicy().hasHeightForWidth())
        self.HeterogeneousFrame.setSizePolicy(sizePolicy3)
        self.horizontalLayout_18 = QHBoxLayout(self.HeterogeneousFrame)
        self.horizontalLayout_18.setSpacing(20)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.regxp_heterogeneous_lbl = QLabel(self.HeterogeneousFrame)
        self.regxp_heterogeneous_lbl.setObjectName(u"regxp_heterogeneous_lbl")
        sizePolicy.setHeightForWidth(self.regxp_heterogeneous_lbl.sizePolicy().hasHeightForWidth())
        self.regxp_heterogeneous_lbl.setSizePolicy(sizePolicy)
        self.regxp_heterogeneous_lbl.setFont(font8)
        self.regxp_heterogeneous_lbl.setTextFormat(Qt.MarkdownText)

        self.horizontalLayout_18.addWidget(self.regxp_heterogeneous_lbl)

        self.heterogeneous_checkbox = QPushButton(self.HeterogeneousFrame)
        self.characterFilteringOptionsGroup = QButtonGroup(MainWindow)
        self.characterFilteringOptionsGroup.setObjectName(u"characterFilteringOptionsGroup")
        self.characterFilteringOptionsGroup.addButton(self.heterogeneous_checkbox)
        self.heterogeneous_checkbox.setObjectName(u"heterogeneous_checkbox")
        self.heterogeneous_checkbox.setMinimumSize(QSize(41, 41))
        self.heterogeneous_checkbox.setMaximumSize(QSize(41, 41))
        self.heterogeneous_checkbox.setFont(font9)
        self.heterogeneous_checkbox.setStyleSheet(u"QPushButton {\n"
"    background-color: #e0e0e0;\n"
"    border: 2px solid #141414;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* Style for the checked state */\n"
"QPushButton:checked {\n"
"    background-color: #4CAF50; /* Change the background color when checked */\n"
"    color: white; /* Change the text color when checked */\n"
"	border:2px solid #141414;\n"
"}")
        self.heterogeneous_checkbox.setIconSize(QSize(70, 70))
        self.heterogeneous_checkbox.setCheckable(True)
        self.heterogeneous_checkbox.setChecked(False)
        self.heterogeneous_checkbox.setAutoRepeat(False)
        self.heterogeneous_checkbox.setAutoExclusive(False)

        self.horizontalLayout_18.addWidget(self.heterogeneous_checkbox)


        self.verticalLayout_4.addWidget(self.HeterogeneousFrame)

        self.URL_Frame = QFrame(self.CharacterInclusionOptionsFrame)
        self.URL_Frame.setObjectName(u"URL_Frame")
        sizePolicy3.setHeightForWidth(self.URL_Frame.sizePolicy().hasHeightForWidth())
        self.URL_Frame.setSizePolicy(sizePolicy3)
        self.URL_Frame.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_13 = QHBoxLayout(self.URL_Frame)
        self.horizontalLayout_13.setSpacing(20)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.regxp_url_lbl = QLabel(self.URL_Frame)
        self.regxp_url_lbl.setObjectName(u"regxp_url_lbl")
        sizePolicy.setHeightForWidth(self.regxp_url_lbl.sizePolicy().hasHeightForWidth())
        self.regxp_url_lbl.setSizePolicy(sizePolicy)
        self.regxp_url_lbl.setFont(font8)
        self.regxp_url_lbl.setTextFormat(Qt.MarkdownText)
        self.regxp_url_lbl.setScaledContents(False)
        self.regxp_url_lbl.setWordWrap(True)

        self.horizontalLayout_13.addWidget(self.regxp_url_lbl)

        self.url_checkbox = QPushButton(self.URL_Frame)
        self.characterFilteringOptionsGroup.addButton(self.url_checkbox)
        self.url_checkbox.setObjectName(u"url_checkbox")
        self.url_checkbox.setMinimumSize(QSize(41, 41))
        self.url_checkbox.setMaximumSize(QSize(41, 41))
        self.url_checkbox.setFont(font9)
        self.url_checkbox.setStyleSheet(u"QPushButton {\n"
"    background-color: #e0e0e0;\n"
"    border: 2px solid #141414;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* Style for the checked state */\n"
"QPushButton:checked {\n"
"    background-color: #4CAF50; /* Change the background color when checked */\n"
"    color: white; /* Change the text color when checked */\n"
"	border:2px solid #141414;\n"
"}")
        self.url_checkbox.setIconSize(QSize(70, 70))
        self.url_checkbox.setCheckable(True)
        self.url_checkbox.setChecked(True)
        self.url_checkbox.setAutoRepeat(False)
        self.url_checkbox.setAutoExclusive(False)

        self.horizontalLayout_13.addWidget(self.url_checkbox)


        self.verticalLayout_4.addWidget(self.URL_Frame)

        self.BinaryFrame = QFrame(self.CharacterInclusionOptionsFrame)
        self.BinaryFrame.setObjectName(u"BinaryFrame")
        sizePolicy.setHeightForWidth(self.BinaryFrame.sizePolicy().hasHeightForWidth())
        self.BinaryFrame.setSizePolicy(sizePolicy)
        self.horizontalLayout_17 = QHBoxLayout(self.BinaryFrame)
        self.horizontalLayout_17.setSpacing(20)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.regxp_numbersOnly_lbl = QLabel(self.BinaryFrame)
        self.regxp_numbersOnly_lbl.setObjectName(u"regxp_numbersOnly_lbl")
        sizePolicy.setHeightForWidth(self.regxp_numbersOnly_lbl.sizePolicy().hasHeightForWidth())
        self.regxp_numbersOnly_lbl.setSizePolicy(sizePolicy)
        self.regxp_numbersOnly_lbl.setFont(font8)
        self.regxp_numbersOnly_lbl.setTextFormat(Qt.MarkdownText)

        self.horizontalLayout_17.addWidget(self.regxp_numbersOnly_lbl)

        self.binary_checkbox = QPushButton(self.BinaryFrame)
        self.characterFilteringOptionsGroup.addButton(self.binary_checkbox)
        self.binary_checkbox.setObjectName(u"binary_checkbox")
        self.binary_checkbox.setMinimumSize(QSize(41, 41))
        self.binary_checkbox.setMaximumSize(QSize(41, 41))
        self.binary_checkbox.setFont(font9)
        self.binary_checkbox.setStyleSheet(u"QPushButton {\n"
"    background-color: #e0e0e0;\n"
"    border: 2px solid #141414;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* Style for the checked state */\n"
"QPushButton:checked {\n"
"    background-color: #4CAF50; /* Change the background color when checked */\n"
"    color: white; /* Change the text color when checked */\n"
"	border:2px solid #141414;\n"
"}")
        self.binary_checkbox.setIconSize(QSize(70, 70))
        self.binary_checkbox.setCheckable(True)
        self.binary_checkbox.setChecked(False)
        self.binary_checkbox.setAutoRepeat(False)
        self.binary_checkbox.setAutoExclusive(False)

        self.horizontalLayout_17.addWidget(self.binary_checkbox)


        self.verticalLayout_4.addWidget(self.BinaryFrame)

        self.disorderFrame = QFrame(self.CharacterInclusionOptionsFrame)
        self.disorderFrame.setObjectName(u"disorderFrame")
        sizePolicy3.setHeightForWidth(self.disorderFrame.sizePolicy().hasHeightForWidth())
        self.disorderFrame.setSizePolicy(sizePolicy3)
        self.horizontalLayout_16 = QHBoxLayout(self.disorderFrame)
        self.horizontalLayout_16.setSpacing(20)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.regxp_disorder_lbl = QLabel(self.disorderFrame)
        self.regxp_disorder_lbl.setObjectName(u"regxp_disorder_lbl")
        sizePolicy.setHeightForWidth(self.regxp_disorder_lbl.sizePolicy().hasHeightForWidth())
        self.regxp_disorder_lbl.setSizePolicy(sizePolicy)
        self.regxp_disorder_lbl.setFont(font8)
        self.regxp_disorder_lbl.setTextFormat(Qt.MarkdownText)

        self.horizontalLayout_16.addWidget(self.regxp_disorder_lbl)

        self.disorder_checkbox = QPushButton(self.disorderFrame)
        self.characterFilteringOptionsGroup.addButton(self.disorder_checkbox)
        self.disorder_checkbox.setObjectName(u"disorder_checkbox")
        self.disorder_checkbox.setMinimumSize(QSize(41, 41))
        self.disorder_checkbox.setMaximumSize(QSize(41, 41))
        self.disorder_checkbox.setFont(font9)
        self.disorder_checkbox.setStyleSheet(u"QPushButton {\n"
"    background-color: #e0e0e0;\n"
"    border: 2px solid #141414;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* Style for the checked state */\n"
"QPushButton:checked {\n"
"    background-color: #4CAF50; /* Change the background color when checked */\n"
"    color: white; /* Change the text color when checked */\n"
"	border:2px solid #141414;\n"
"}")
        self.disorder_checkbox.setIconSize(QSize(70, 70))
        self.disorder_checkbox.setCheckable(True)
        self.disorder_checkbox.setChecked(False)
        self.disorder_checkbox.setAutoRepeat(False)
        self.disorder_checkbox.setAutoExclusive(False)

        self.horizontalLayout_16.addWidget(self.disorder_checkbox)


        self.verticalLayout_4.addWidget(self.disorderFrame)


        self.gridLayout_5.addWidget(self.CharacterInclusionOptionsFrame, 0, 0, 1, 1)

        self.parameters_window.addTab(self.tab_6, "")

        self.gridLayout_3.addWidget(self.parameters_window, 0, 0, 1, 1)

        self.word_input = QTextEdit(self.WordInputAndParametersFrame)
        self.word_input.setObjectName(u"word_input")
        sizePolicy11.setHeightForWidth(self.word_input.sizePolicy().hasHeightForWidth())
        self.word_input.setSizePolicy(sizePolicy11)
        self.word_input.setFont(font7)
        self.word_input.setStyleSheet(u"")
        self.word_input.setFrameShadow(QFrame.Plain)
        self.word_input.setLineWidth(1)
        self.word_input.setTabChangesFocus(False)
        self.word_input.setUndoRedoEnabled(True)

        self.gridLayout_3.addWidget(self.word_input, 4, 0, 1, 3)

        self.fonts_Frame = QFrame(self.WordInputAndParametersFrame)
        self.fonts_Frame.setObjectName(u"fonts_Frame")
        sizePolicy.setHeightForWidth(self.fonts_Frame.sizePolicy().hasHeightForWidth())
        self.fonts_Frame.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.fonts_Frame)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.custom_font_directory_selection = QPushButton(self.fonts_Frame)
        self.custom_font_directory_selection.setObjectName(u"custom_font_directory_selection")
        sizePolicy5.setHeightForWidth(self.custom_font_directory_selection.sizePolicy().hasHeightForWidth())
        self.custom_font_directory_selection.setSizePolicy(sizePolicy5)
        self.custom_font_directory_selection.setMinimumSize(QSize(134, 30))
        self.custom_font_directory_selection.setFont(font)
        self.custom_font_directory_selection.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.custom_font_directory_selection)

        self.load_emoji_fonts_btn = QPushButton(self.fonts_Frame)
        self.load_emoji_fonts_btn.setObjectName(u"load_emoji_fonts_btn")
        sizePolicy5.setHeightForWidth(self.load_emoji_fonts_btn.sizePolicy().hasHeightForWidth())
        self.load_emoji_fonts_btn.setSizePolicy(sizePolicy5)
        self.load_emoji_fonts_btn.setMinimumSize(QSize(107, 30))
        self.load_emoji_fonts_btn.setFont(font)
        self.load_emoji_fonts_btn.setStyleSheet(u"QPushButton{\n"
"background-color:#212121;\n"
"color:#e6e6e6;\n"
"}")

        self.verticalLayout_3.addWidget(self.load_emoji_fonts_btn)

        self.load_appData_fonts_btn = QPushButton(self.fonts_Frame)
        self.load_appData_fonts_btn.setObjectName(u"load_appData_fonts_btn")
        sizePolicy5.setHeightForWidth(self.load_appData_fonts_btn.sizePolicy().hasHeightForWidth())
        self.load_appData_fonts_btn.setSizePolicy(sizePolicy5)
        self.load_appData_fonts_btn.setMinimumSize(QSize(121, 30))
        self.load_appData_fonts_btn.setFont(font)
        self.load_appData_fonts_btn.setStyleSheet(u"QPushButton{\n"
"background-color:#212121;\n"
"color:#e6e6e6;\n"
"}")

        self.verticalLayout_3.addWidget(self.load_appData_fonts_btn)

        self.load_system_fonts_btn = QPushButton(self.fonts_Frame)
        self.load_system_fonts_btn.setObjectName(u"load_system_fonts_btn")
        sizePolicy5.setHeightForWidth(self.load_system_fonts_btn.sizePolicy().hasHeightForWidth())
        self.load_system_fonts_btn.setSizePolicy(sizePolicy5)
        self.load_system_fonts_btn.setMinimumSize(QSize(121, 30))
        self.load_system_fonts_btn.setFont(font)
        self.load_system_fonts_btn.setStyleSheet(u"QPushButton{\n"
"background-color:#212121;\n"
"color:#e6e6e6;\n"
"}")

        self.verticalLayout_3.addWidget(self.load_system_fonts_btn)

        self.filter_fonts_input = QPlainTextEdit(self.fonts_Frame)
        self.filter_fonts_input.setObjectName(u"filter_fonts_input")
        sizePolicy12 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.filter_fonts_input.sizePolicy().hasHeightForWidth())
        self.filter_fonts_input.setSizePolicy(sizePolicy12)
        self.filter_fonts_input.setMaximumSize(QSize(16777215, 30))
        font12 = QFont()
        font12.setFamilies([u"Inter"])
        font12.setPointSize(10)
        font12.setBold(True)
        self.filter_fonts_input.setFont(font12)
        self.filter_fonts_input.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.filter_fonts_input)

        self.font_list = QListWidget(self.fonts_Frame)
        self.font_list.setObjectName(u"font_list")
        sizePolicy.setHeightForWidth(self.font_list.sizePolicy().hasHeightForWidth())
        self.font_list.setSizePolicy(sizePolicy)
        self.font_list.setFont(font6)
        self.font_list.setStyleSheet(u"")
        self.font_list.setFrameShadow(QFrame.Sunken)
        self.font_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.font_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.font_list.setAutoScrollMargin(20)
        self.font_list.setTabKeyNavigation(False)

        self.verticalLayout_3.addWidget(self.font_list)

        self.open_fs_window = QPushButton(self.fonts_Frame)
        self.open_fs_window.setObjectName(u"open_fs_window")
        self.open_fs_window.setEnabled(True)
        self.open_fs_window.setMinimumSize(QSize(200, 40))
        self.open_fs_window.setMaximumSize(QSize(200, 16777215))
        self.open_fs_window.setFont(font)
        self.open_fs_window.setAutoFillBackground(False)
        self.open_fs_window.setStyleSheet(u"QPushButton{\n"
"\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/Media/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_fs_window.setIcon(icon6)
        self.open_fs_window.setIconSize(QSize(32, 32))
        self.open_fs_window.setCheckable(False)

        self.verticalLayout_3.addWidget(self.open_fs_window, 0, Qt.AlignHCenter)


        self.gridLayout_3.addWidget(self.fonts_Frame, 0, 1, 1, 1)

        self.frame = QFrame(self.WordInputAndParametersFrame)
        self.frame.setObjectName(u"frame")
        sizePolicy7.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy7)
        self.horizontalLayout_20 = QHBoxLayout(self.frame)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_20.setContentsMargins(-1, -1, 0, 0)
        self.storeTextProfile_btn = QPushButton(self.frame)
        self.storeTextProfile_btn.setObjectName(u"storeTextProfile_btn")
        self.storeTextProfile_btn.setMinimumSize(QSize(32, 32))
        self.storeTextProfile_btn.setMaximumSize(QSize(32, 32))
        self.storeTextProfile_btn.setStyleSheet(u"QPushButton:pressed{\n"
"	 padding-left: 3px;\n"
"     padding-top: 3px;\n"
"}\n"
"QPushButton{\n"
"background-color: rgba(100,100,100,0);\n"
"border-radius:10px;\n"
"}")
        self.storeTextProfile_btn.setIcon(icon5)
        self.storeTextProfile_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_20.addWidget(self.storeTextProfile_btn)

        self.frame_profileFonts = QFrame(self.frame)
        self.frame_profileFonts.setObjectName(u"frame_profileFonts")
        sizePolicy13 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.frame_profileFonts.sizePolicy().hasHeightForWidth())
        self.frame_profileFonts.setSizePolicy(sizePolicy13)
        self.profileFonts_Frame = QHBoxLayout(self.frame_profileFonts)
        self.profileFonts_Frame.setSpacing(20)
        self.profileFonts_Frame.setObjectName(u"profileFonts_Frame")
        self.profileFonts_Frame.setContentsMargins(-1, -1, 0, -1)
        self.profile_fonts_lbl = QLabel(self.frame_profileFonts)
        self.profile_fonts_lbl.setObjectName(u"profile_fonts_lbl")
        sizePolicy2.setHeightForWidth(self.profile_fonts_lbl.sizePolicy().hasHeightForWidth())
        self.profile_fonts_lbl.setSizePolicy(sizePolicy2)
        font13 = QFont()
        font13.setFamilies([u"Inter"])
        font13.setPointSize(14)
        font13.setBold(True)
        self.profile_fonts_lbl.setFont(font13)

        self.profileFonts_Frame.addWidget(self.profile_fonts_lbl)

        self.profile_fonts_list = QComboBox(self.frame_profileFonts)
        self.profile_fonts_list.setObjectName(u"profile_fonts_list")
        sizePolicy3.setHeightForWidth(self.profile_fonts_list.sizePolicy().hasHeightForWidth())
        self.profile_fonts_list.setSizePolicy(sizePolicy3)
        self.profile_fonts_list.setMinimumSize(QSize(300, 30))
        self.profile_fonts_list.setMaximumSize(QSize(300, 40))
        self.profile_fonts_list.setFont(font)
        self.profile_fonts_list.setStyleSheet(u"/* Style the QComboBox */\n"
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
"    border-radius:0px;\n"
"}")
        self.profile_fonts_list.setMaxVisibleItems(15)

        self.profileFonts_Frame.addWidget(self.profile_fonts_list)

        self.apply_profile_font_btn = QPushButton(self.frame_profileFonts)
        self.apply_profile_font_btn.setObjectName(u"apply_profile_font_btn")
        self.apply_profile_font_btn.setMinimumSize(QSize(32, 37))
        self.apply_profile_font_btn.setMaximumSize(QSize(32, 37))
        self.apply_profile_font_btn.setStyleSheet(u"QPushButton:pressed{\n"
"	 padding-left: 3px;\n"
"     padding-top: 3px;\n"
"}\n"
"QPushButton{\n"
"background-color: rgba(100,100,100,0);\n"
"border-radius:10px;\n"
"}")
        self.apply_profile_font_btn.setIcon(icon4)
        self.apply_profile_font_btn.setIconSize(QSize(32, 37))

        self.profileFonts_Frame.addWidget(self.apply_profile_font_btn)

        self.add_profile_font_btn = QPushButton(self.frame_profileFonts)
        self.add_profile_font_btn.setObjectName(u"add_profile_font_btn")
        self.add_profile_font_btn.setMinimumSize(QSize(32, 37))
        self.add_profile_font_btn.setMaximumSize(QSize(32, 37))
        self.add_profile_font_btn.setStyleSheet(u"QPushButton:pressed{\n"
"	 padding-left: 3px;\n"
"     padding-top: 3px;\n"
"}\n"
"QPushButton{\n"
"background-color: rgba(100,100,100,0);\n"
"border-radius:10px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/Media/add_plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_profile_font_btn.setIcon(icon7)
        self.add_profile_font_btn.setIconSize(QSize(32, 37))

        self.profileFonts_Frame.addWidget(self.add_profile_font_btn)

        self.delete_profile_font_btn = QPushButton(self.frame_profileFonts)
        self.delete_profile_font_btn.setObjectName(u"delete_profile_font_btn")
        self.delete_profile_font_btn.setMinimumSize(QSize(32, 37))
        self.delete_profile_font_btn.setMaximumSize(QSize(32, 37))
        self.delete_profile_font_btn.setStyleSheet(u"QPushButton:pressed{\n"
"	 padding-left: 3px;\n"
"     padding-top: 3px;\n"
"}\n"
"QPushButton{\n"
"background-color: rgba(100,100,100,0);\n"
"border-radius:10px;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/Media/delete_minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_profile_font_btn.setIcon(icon8)
        self.delete_profile_font_btn.setIconSize(QSize(32, 32))

        self.profileFonts_Frame.addWidget(self.delete_profile_font_btn)


        self.horizontalLayout_20.addWidget(self.frame_profileFonts, 0, Qt.AlignRight)

        self.horizontalLayout_20.setStretch(1, 1)

        self.gridLayout_3.addWidget(self.frame, 3, 0, 1, 3)


        self.gridLayout_2.addWidget(self.WordInputAndParametersFrame, 0, 0, 1, 1)

        self.WC_GeneratorFrame = QFrame(self.page1)
        self.WC_GeneratorFrame.setObjectName(u"WC_GeneratorFrame")
        sizePolicy.setHeightForWidth(self.WC_GeneratorFrame.sizePolicy().hasHeightForWidth())
        self.WC_GeneratorFrame.setSizePolicy(sizePolicy)
        self.WC_GeneratorFrame.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_2 = QVBoxLayout(self.WC_GeneratorFrame)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 10)
        self.export_as_frame = QFrame(self.WC_GeneratorFrame)
        self.export_as_frame.setObjectName(u"export_as_frame")
        self.export_as_frame.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.export_as_frame.sizePolicy().hasHeightForWidth())
        self.export_as_frame.setSizePolicy(sizePolicy2)
        self.export_as_frame.setMinimumSize(QSize(100, 75))
        self.export_as_frame.setFont(font)
        self.export_as_frame.setContextMenuPolicy(Qt.NoContextMenu)
        self.gridLayout_4 = QGridLayout(self.export_as_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 5)
        self.export_format_options = QComboBox(self.export_as_frame)
        self.export_format_options.addItem("")
        self.export_format_options.addItem("")
        self.export_format_options.addItem("")
        self.export_format_options.setObjectName(u"export_format_options")
        sizePolicy7.setHeightForWidth(self.export_format_options.sizePolicy().hasHeightForWidth())
        self.export_format_options.setSizePolicy(sizePolicy7)
        self.export_format_options.setFont(font)
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

        self.gridLayout_4.addWidget(self.export_format_options, 1, 0, 1, 1)

        self.exportAs_label = QLabel(self.export_as_frame)
        self.exportAs_label.setObjectName(u"exportAs_label")
        sizePolicy1.setHeightForWidth(self.exportAs_label.sizePolicy().hasHeightForWidth())
        self.exportAs_label.setSizePolicy(sizePolicy1)
        self.exportAs_label.setFont(font)

        self.gridLayout_4.addWidget(self.exportAs_label, 0, 0, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.export_as_frame, 0, Qt.AlignHCenter)

        self.anotherFrame = QFrame(self.WC_GeneratorFrame)
        self.anotherFrame.setObjectName(u"anotherFrame")
        sizePolicy3.setHeightForWidth(self.anotherFrame.sizePolicy().hasHeightForWidth())
        self.anotherFrame.setSizePolicy(sizePolicy3)
        self.horizontalLayout_23 = QHBoxLayout(self.anotherFrame)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_23.setContentsMargins(0, -1, 75, -1)
        self.FileHandlingFrame = QFrame(self.anotherFrame)
        self.FileHandlingFrame.setObjectName(u"FileHandlingFrame")
        sizePolicy2.setHeightForWidth(self.FileHandlingFrame.sizePolicy().hasHeightForWidth())
        self.FileHandlingFrame.setSizePolicy(sizePolicy2)
        self.horizontalLayout_24 = QHBoxLayout(self.FileHandlingFrame)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.stash_last_generated_button = QPushButton(self.FileHandlingFrame)
        self.stash_last_generated_button.setObjectName(u"stash_last_generated_button")
        self.stash_last_generated_button.setMinimumSize(QSize(40, 40))
        self.stash_last_generated_button.setMaximumSize(QSize(40, 40))
        self.stash_last_generated_button.setFont(font)
        self.stash_last_generated_button.setStyleSheet(u"QPushButton {\n"
"    background-color: green; /* or any other color you want */\n"
"}\n"
"QPushButton:pressed{\n"
"	 padding-left: 3px;\n"
"     padding-top: 3px;\n"
"}")

        self.horizontalLayout_24.addWidget(self.stash_last_generated_button)

        self.delete_last_generated_button = QPushButton(self.FileHandlingFrame)
        self.delete_last_generated_button.setObjectName(u"delete_last_generated_button")
        self.delete_last_generated_button.setMinimumSize(QSize(40, 40))
        self.delete_last_generated_button.setMaximumSize(QSize(40, 40))
        self.delete_last_generated_button.setFont(font)
        self.delete_last_generated_button.setStyleSheet(u"QPushButton {\n"
"    background-color: red; /* or any other color you want */\n"
"}\n"
"QPushButton:pressed{\n"
"	 padding-left: 3px;\n"
"     padding-top: 3px;\n"
"}")

        self.horizontalLayout_24.addWidget(self.delete_last_generated_button)


        self.horizontalLayout_23.addWidget(self.FileHandlingFrame, 0, Qt.AlignLeft)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_2)

        self.random_Seed_Frame = QFrame(self.anotherFrame)
        self.random_Seed_Frame.setObjectName(u"random_Seed_Frame")
        sizePolicy2.setHeightForWidth(self.random_Seed_Frame.sizePolicy().hasHeightForWidth())
        self.random_Seed_Frame.setSizePolicy(sizePolicy2)
        self.random_Seed_Frame.setMinimumSize(QSize(250, 0))
        self.random_Seed_Frame.setMaximumSize(QSize(250, 16777215))
        self.horizontalLayout_44 = QHBoxLayout(self.random_Seed_Frame)
        self.horizontalLayout_44.setSpacing(10)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_44.setContentsMargins(-1, 0, -1, 0)
        self.random_seed_lbl = QLabel(self.random_Seed_Frame)
        self.random_seed_lbl.setObjectName(u"random_seed_lbl")
        sizePolicy4.setHeightForWidth(self.random_seed_lbl.sizePolicy().hasHeightForWidth())
        self.random_seed_lbl.setSizePolicy(sizePolicy4)
        self.random_seed_lbl.setMaximumSize(QSize(16777215, 30))
        self.random_seed_lbl.setFont(font8)

        self.horizontalLayout_44.addWidget(self.random_seed_lbl)

        self.random_seed_slider = QSlider(self.random_Seed_Frame)
        self.random_seed_slider.setObjectName(u"random_seed_slider")
        sizePolicy2.setHeightForWidth(self.random_seed_slider.sizePolicy().hasHeightForWidth())
        self.random_seed_slider.setSizePolicy(sizePolicy2)
        self.random_seed_slider.setMinimumSize(QSize(0, 40))
        self.random_seed_slider.setMaximumSize(QSize(300, 16777215))
        self.random_seed_slider.setCursor(QCursor(Qt.PointingHandCursor))
        self.random_seed_slider.setMouseTracking(False)
        self.random_seed_slider.setFocusPolicy(Qt.StrongFocus)
        self.random_seed_slider.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.random_seed_slider.setLayoutDirection(Qt.LeftToRight)
        self.random_seed_slider.setStyleSheet(u"QSlider::groove {\n"
"height: 5px;\n"
"/*width: 350px;*/\n"
"background: grey;\n"
"margin: 3px 0;\n"
"/*border: 2px solid #c17d08;\n"
"border-radius: 2px;*/\n"
"}\n"
"QSlider::handle{\n"
"    background: red;\n"
"    border: none;\n"
"    width: 15px;\n"
"    margin: -10px 0;\n"
"    border-radius: 5px;\n"
"}\n"
"QSlider::add-page {\n"
"height: 10px;\n"
"background: #e9e9e9;\n"
"border: none;\n"
"border-radius: 4px;\n"
"}\n"
"/*QSlider::sub-page {\n"
"background: #c17d08;\n"
"height: 6px;\n"
"border: 1px solid #c17d08;\n"
"border-radius: 12px;\n"
"}*/\n"
"QSlider::sub-page{\n"
"height: 15px;\n"
"background: green;\n"
"border: none;\n"
"border-radius: 5px;\n"
"}")
        self.random_seed_slider.setMinimum(0)
        self.random_seed_slider.setMaximum(999)
        self.random_seed_slider.setPageStep(1)
        self.random_seed_slider.setValue(0)
        self.random_seed_slider.setOrientation(Qt.Horizontal)
        self.random_seed_slider.setInvertedControls(False)
        self.random_seed_slider.setTickPosition(QSlider.NoTicks)
        self.random_seed_slider.setTickInterval(0)

        self.horizontalLayout_44.addWidget(self.random_seed_slider)

        self.random_seed_int_lbl = QLabel(self.random_Seed_Frame)
        self.random_seed_int_lbl.setObjectName(u"random_seed_int_lbl")
        self.random_seed_int_lbl.setFont(font8)
        self.random_seed_int_lbl.setMargin(5)
        self.random_seed_int_lbl.setIndent(-1)
        self.random_seed_int_lbl.setOpenExternalLinks(False)

        self.horizontalLayout_44.addWidget(self.random_seed_int_lbl)

        self.horizontalLayout_44.setStretch(0, 1)

        self.horizontalLayout_23.addWidget(self.random_Seed_Frame, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addWidget(self.anotherFrame)

        self.generate_wordcloud_button = QPushButton(self.WC_GeneratorFrame)
        self.generate_wordcloud_button.setObjectName(u"generate_wordcloud_button")
        self.generate_wordcloud_button.setEnabled(True)
        sizePolicy.setHeightForWidth(self.generate_wordcloud_button.sizePolicy().hasHeightForWidth())
        self.generate_wordcloud_button.setSizePolicy(sizePolicy)
        self.generate_wordcloud_button.setMinimumSize(QSize(250, 0))
        self.generate_wordcloud_button.setMaximumSize(QSize(16777215, 200))
        self.generate_wordcloud_button.setFont(font)
        self.generate_wordcloud_button.setToolTipDuration(-1)
        self.generate_wordcloud_button.setStyleSheet(u"QPushButton{\n"
"color: rgb(200,200,200);\n"
"background-color: rgb(50, 50, 50);\n"
"border: 7px solid green;\n"
"border-radius: 50px;\n"
"padding: 30px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:green;\n"
"border: 10px solid rgb(50, 50, 50);\n"
"padding-left: 50px;\n"
"padding-bottom:20px\n"
"}")
        self.generate_wordcloud_button.setText(u"")
        icon9 = QIcon()
        icon9.addFile(u":/Media/LogoAssetForButton.png", QSize(), QIcon.Normal, QIcon.Off)
        self.generate_wordcloud_button.setIcon(icon9)
        self.generate_wordcloud_button.setIconSize(QSize(100, 100))
        self.generate_wordcloud_button.setCheckable(False)
        self.generate_wordcloud_button.setChecked(False)
        self.generate_wordcloud_button.setAutoRepeat(False)
        self.generate_wordcloud_button.setAutoExclusive(False)
        self.generate_wordcloud_button.setAutoDefault(False)
        self.generate_wordcloud_button.setFlat(False)

        self.verticalLayout_2.addWidget(self.generate_wordcloud_button)


        self.gridLayout_2.addWidget(self.WC_GeneratorFrame, 1, 0, 1, 1)

        self.MaskandEmojisFrame = QFrame(self.page1)
        self.MaskandEmojisFrame.setObjectName(u"MaskandEmojisFrame")
        sizePolicy.setHeightForWidth(self.MaskandEmojisFrame.sizePolicy().hasHeightForWidth())
        self.MaskandEmojisFrame.setSizePolicy(sizePolicy)
        self.kaka = QGridLayout(self.MaskandEmojisFrame)
        self.kaka.setObjectName(u"kaka")
        self.mask_container = QFrame(self.MaskandEmojisFrame)
        self.mask_container.setObjectName(u"mask_container")
        sizePolicy6.setHeightForWidth(self.mask_container.sizePolicy().hasHeightForWidth())
        self.mask_container.setSizePolicy(sizePolicy6)
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
        sizePolicy2.setHeightForWidth(self.mask_dimensions_label.sizePolicy().hasHeightForWidth())
        self.mask_dimensions_label.setSizePolicy(sizePolicy2)
        self.mask_dimensions_label.setMaximumSize(QSize(300, 16777215))
        font14 = QFont()
        font14.setFamilies([u"Inter"])
        font14.setPointSize(9)
        font14.setBold(True)
        font14.setItalic(False)
        font14.setUnderline(False)
        font14.setStyleStrategy(QFont.PreferDefault)
        self.mask_dimensions_label.setFont(font14)
        self.mask_dimensions_label.setCursor(QCursor(Qt.ArrowCursor))

        self.verticalLayout.addWidget(self.mask_dimensions_label, 0, Qt.AlignHCenter)

        self.SelectButtonsFrame = QFrame(self.mask_container)
        self.SelectButtonsFrame.setObjectName(u"SelectButtonsFrame")
        sizePolicy2.setHeightForWidth(self.SelectButtonsFrame.sizePolicy().hasHeightForWidth())
        self.SelectButtonsFrame.setSizePolicy(sizePolicy2)
        self.horizontalLayout_3 = QHBoxLayout(self.SelectButtonsFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.mask_select_button = QPushButton(self.SelectButtonsFrame)
        self.mask_select_button.setObjectName(u"mask_select_button")
        self.mask_select_button.setMinimumSize(QSize(150, 50))
        self.mask_select_button.setMaximumSize(QSize(150, 16777215))
        self.mask_select_button.setFont(font)
        self.mask_select_button.setStyleSheet(u"QPushButton{\n"
"border:2px solid red; \n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.mask_select_button)

        self.fa_mask_select_button = QPushButton(self.SelectButtonsFrame)
        self.fa_mask_select_button.setObjectName(u"fa_mask_select_button")
        self.fa_mask_select_button.setMinimumSize(QSize(150, 50))
        self.fa_mask_select_button.setMaximumSize(QSize(150, 16777215))
        self.fa_mask_select_button.setFont(font)
        self.fa_mask_select_button.setStyleSheet(u"QPushButton{\n"
"border:2px solid red; \n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.fa_mask_select_button)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.select_destination_button = QPushButton(self.SelectButtonsFrame)
        self.select_destination_button.setObjectName(u"select_destination_button")
        self.select_destination_button.setEnabled(True)
        self.select_destination_button.setMinimumSize(QSize(150, 50))
        self.select_destination_button.setMaximumSize(QSize(150, 16777215))
        self.select_destination_button.setFont(font)
        self.select_destination_button.setStyleSheet(u"QPushButton{\n"
"border:2px solid red; \n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.select_destination_button)

        self.open_destination_folder = QPushButton(self.SelectButtonsFrame)
        self.open_destination_folder.setObjectName(u"open_destination_folder")
        self.open_destination_folder.setMinimumSize(QSize(50, 50))
        self.open_destination_folder.setMaximumSize(QSize(40, 50))
        self.open_destination_folder.setFont(font)
        self.open_destination_folder.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 170, 0);\n"
"border-radius:5px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.open_destination_folder)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.SelectButtonsFrame, 0, Qt.AlignHCenter)

        self.exportScaleFrame = QFrame(self.mask_container)
        self.exportScaleFrame.setObjectName(u"exportScaleFrame")
        sizePolicy4.setHeightForWidth(self.exportScaleFrame.sizePolicy().hasHeightForWidth())
        self.exportScaleFrame.setSizePolicy(sizePolicy4)
        self.exportScaleFrame.setMinimumSize(QSize(203, 42))
        self.horizontalLayout_35 = QHBoxLayout(self.exportScaleFrame)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.image_scale_label = QLabel(self.exportScaleFrame)
        self.image_scale_label.setObjectName(u"image_scale_label")
        sizePolicy4.setHeightForWidth(self.image_scale_label.sizePolicy().hasHeightForWidth())
        self.image_scale_label.setSizePolicy(sizePolicy4)
        self.image_scale_label.setMaximumSize(QSize(16777215, 30))
        self.image_scale_label.setFont(font8)

        self.horizontalLayout_35.addWidget(self.image_scale_label)

        self.scale_slider = QSlider(self.exportScaleFrame)
        self.scale_slider.setObjectName(u"scale_slider")
        sizePolicy2.setHeightForWidth(self.scale_slider.sizePolicy().hasHeightForWidth())
        self.scale_slider.setSizePolicy(sizePolicy2)
        self.scale_slider.setMinimumSize(QSize(0, 40))
        self.scale_slider.setMaximumSize(QSize(140, 40))
        self.scale_slider.setCursor(QCursor(Qt.PointingHandCursor))
        self.scale_slider.setMouseTracking(False)
        self.scale_slider.setFocusPolicy(Qt.StrongFocus)
        self.scale_slider.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.scale_slider.setLayoutDirection(Qt.LeftToRight)
        self.scale_slider.setStyleSheet(u"QSlider::groove {\n"
"height: 5px;\n"
"/*width: 350px;*/\n"
"background: grey;\n"
"margin: 3px 0;\n"
"/*border: 2px solid #c17d08;\n"
"border-radius: 2px;*/\n"
"}\n"
"QSlider::handle{\n"
"    background: red;\n"
"    border: none;\n"
"    width: 15px;\n"
"    margin: -10px 0;\n"
"    border-radius: 5px;\n"
"}\n"
"QSlider::add-page {\n"
"height: 10px;\n"
"background: #e9e9e9;\n"
"border: none;\n"
"border-radius: 4px;\n"
"}\n"
"/*QSlider::sub-page {\n"
"background: #c17d08;\n"
"height: 6px;\n"
"border: 1px solid #c17d08;\n"
"border-radius: 12px;\n"
"}*/\n"
"QSlider::sub-page{\n"
"height: 15px;\n"
"background: green;\n"
"border: none;\n"
"border-radius: 5px;\n"
"}")
        self.scale_slider.setMinimum(1)
        self.scale_slider.setMaximum(10)
        self.scale_slider.setPageStep(1)
        self.scale_slider.setOrientation(Qt.Horizontal)
        self.scale_slider.setInvertedControls(False)
        self.scale_slider.setTickPosition(QSlider.NoTicks)
        self.scale_slider.setTickInterval(0)

        self.horizontalLayout_35.addWidget(self.scale_slider)

        self.label_scale_slider = QLabel(self.exportScaleFrame)
        self.label_scale_slider.setObjectName(u"label_scale_slider")
        sizePolicy4.setHeightForWidth(self.label_scale_slider.sizePolicy().hasHeightForWidth())
        self.label_scale_slider.setSizePolicy(sizePolicy4)
        self.label_scale_slider.setMinimumSize(QSize(31, 40))
        self.label_scale_slider.setMaximumSize(QSize(50, 50))
        self.label_scale_slider.setFont(font8)
        self.label_scale_slider.setMargin(5)
        self.label_scale_slider.setIndent(-1)
        self.label_scale_slider.setOpenExternalLinks(False)

        self.horizontalLayout_35.addWidget(self.label_scale_slider)


        self.verticalLayout.addWidget(self.exportScaleFrame, 0, Qt.AlignHCenter)


        self.kaka.addWidget(self.mask_container, 0, 0, 1, 1)

        self.EmojiFull_Frame = QFrame(self.MaskandEmojisFrame)
        self.EmojiFull_Frame.setObjectName(u"EmojiFull_Frame")
        sizePolicy9.setHeightForWidth(self.EmojiFull_Frame.sizePolicy().hasHeightForWidth())
        self.EmojiFull_Frame.setSizePolicy(sizePolicy9)
        self.EmojiFull_Frame.setMaximumSize(QSize(16777215, 16777215))
        font15 = QFont()
        font15.setFamilies([u"Inter"])
        font15.setBold(True)
        self.EmojiFull_Frame.setFont(font15)
        self.verticalLayout_9 = QVBoxLayout(self.EmojiFull_Frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, -1, -1, 0)
        self.load_emojis_Frame = QFrame(self.EmojiFull_Frame)
        self.load_emojis_Frame.setObjectName(u"load_emojis_Frame")
        sizePolicy4.setHeightForWidth(self.load_emojis_Frame.sizePolicy().hasHeightForWidth())
        self.load_emojis_Frame.setSizePolicy(sizePolicy4)
        self.horizontalLayout_6 = QHBoxLayout(self.load_emojis_Frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.unicode_Emojis_btn = QPushButton(self.load_emojis_Frame)
        self.unicode_Emojis_btn.setObjectName(u"unicode_Emojis_btn")
        self.unicode_Emojis_btn.setEnabled(True)
        self.unicode_Emojis_btn.setMinimumSize(QSize(150, 40))
        self.unicode_Emojis_btn.setMaximumSize(QSize(150, 16777215))
        self.unicode_Emojis_btn.setFont(font)
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
        self.font_Awesome_Icons_btn.setFont(font)
        self.font_Awesome_Icons_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.font_Awesome_Icons_btn)


        self.verticalLayout_9.addWidget(self.load_emojis_Frame, 0, Qt.AlignHCenter)

        self.FilterListFrame = QFrame(self.EmojiFull_Frame)
        self.FilterListFrame.setObjectName(u"FilterListFrame")
        sizePolicy2.setHeightForWidth(self.FilterListFrame.sizePolicy().hasHeightForWidth())
        self.FilterListFrame.setSizePolicy(sizePolicy2)
        self.horizontalLayout_5 = QHBoxLayout(self.FilterListFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
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
        sizePolicy2.setHeightForWidth(self.emoji_filter_list.sizePolicy().hasHeightForWidth())
        self.emoji_filter_list.setSizePolicy(sizePolicy2)
        self.emoji_filter_list.setMinimumSize(QSize(211, 41))
        self.emoji_filter_list.setFont(font2)
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

        self.unicodeEmojis_filter_input = QPlainTextEdit(self.EmojiFull_Frame)
        self.unicodeEmojis_filter_input.setObjectName(u"unicodeEmojis_filter_input")
        sizePolicy12.setHeightForWidth(self.unicodeEmojis_filter_input.sizePolicy().hasHeightForWidth())
        self.unicodeEmojis_filter_input.setSizePolicy(sizePolicy12)
        self.unicodeEmojis_filter_input.setMaximumSize(QSize(16777215, 30))
        self.unicodeEmojis_filter_input.setFont(font12)
        self.unicodeEmojis_filter_input.setStyleSheet(u"")

        self.verticalLayout_9.addWidget(self.unicodeEmojis_filter_input, 0, Qt.AlignHCenter)

        self.FontAwesome_FilterFrame = QFrame(self.EmojiFull_Frame)
        self.FontAwesome_FilterFrame.setObjectName(u"FontAwesome_FilterFrame")
        sizePolicy2.setHeightForWidth(self.FontAwesome_FilterFrame.sizePolicy().hasHeightForWidth())
        self.FontAwesome_FilterFrame.setSizePolicy(sizePolicy2)
        self.horizontalLayout_8 = QHBoxLayout(self.FontAwesome_FilterFrame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.fontAwesome_filter_input = QPlainTextEdit(self.FontAwesome_FilterFrame)
        self.fontAwesome_filter_input.setObjectName(u"fontAwesome_filter_input")
        sizePolicy12.setHeightForWidth(self.fontAwesome_filter_input.sizePolicy().hasHeightForWidth())
        self.fontAwesome_filter_input.setSizePolicy(sizePolicy12)
        self.fontAwesome_filter_input.setMaximumSize(QSize(16777215, 30))
        self.fontAwesome_filter_input.setFont(font12)
        self.fontAwesome_filter_input.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.fontAwesome_filter_input)


        self.verticalLayout_9.addWidget(self.FontAwesome_FilterFrame, 0, Qt.AlignHCenter)

        self.emoji_list = QListWidget(self.EmojiFull_Frame)
        self.emoji_list.setObjectName(u"emoji_list")
        sizePolicy.setHeightForWidth(self.emoji_list.sizePolicy().hasHeightForWidth())
        self.emoji_list.setSizePolicy(sizePolicy)
        font16 = QFont()
        font16.setFamilies([u"Segoe UI Emoji"])
        font16.setPointSize(40)
        font16.setBold(False)
        self.emoji_list.setFont(font16)
        self.emoji_list.setStyleSheet(u"")
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
        self.emoji_list.setViewMode(QListView.IconMode)
        self.emoji_list.setUniformItemSizes(False)

        self.verticalLayout_9.addWidget(self.emoji_list)


        self.kaka.addWidget(self.EmojiFull_Frame, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.MaskandEmojisFrame, 0, 1, 2, 1)

        self.stackedWidget.addWidget(self.page1)

        self.gridLayout.addWidget(self.stackedWidget, 1, 2, 1, 1)

        self.pageButtonsFrameTop = QFrame(self.centralwidget)
        self.pageButtonsFrameTop.setObjectName(u"pageButtonsFrameTop")
        sizePolicy4.setHeightForWidth(self.pageButtonsFrameTop.sizePolicy().hasHeightForWidth())
        self.pageButtonsFrameTop.setSizePolicy(sizePolicy4)
        self.horizontalLayout = QHBoxLayout(self.pageButtonsFrameTop)
        self.horizontalLayout.setSpacing(14)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(11, 0, 11, 0)
        self.page_back_btn = QPushButton(self.pageButtonsFrameTop)
        self.pageSwitchButtonsGroup = QButtonGroup(MainWindow)
        self.pageSwitchButtonsGroup.setObjectName(u"pageSwitchButtonsGroup")
        self.pageSwitchButtonsGroup.addButton(self.page_back_btn)
        self.page_back_btn.setObjectName(u"page_back_btn")
        self.page_back_btn.setMinimumSize(QSize(32, 37))
        self.page_back_btn.setMaximumSize(QSize(32, 37))
        self.page_back_btn.setStyleSheet(u"QPushButton:pressed{\n"
"	 padding-left: 3px;\n"
"     padding-top: 3px;\n"
"}\n"
"QPushButton{\n"
"background-color: rgba(100,100,100,0);\n"
"border-radius:10px;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/Media/arrow_back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.page_back_btn.setIcon(icon10)
        self.page_back_btn.setIconSize(QSize(32, 37))

        self.horizontalLayout.addWidget(self.page_back_btn)

        self.page_forward_btn = QPushButton(self.pageButtonsFrameTop)
        self.pageSwitchButtonsGroup.addButton(self.page_forward_btn)
        self.page_forward_btn.setObjectName(u"page_forward_btn")
        self.page_forward_btn.setMinimumSize(QSize(32, 37))
        self.page_forward_btn.setMaximumSize(QSize(32, 37))
        self.page_forward_btn.setStyleSheet(u"QPushButton:pressed{\n"
"	 padding-left: 3px;\n"
"     padding-top: 3px;\n"
"}\n"
"QPushButton{\n"
"background-color: rgba(100,100,100,0);\n"
"border-radius:10px;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/Media/arrow_forward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.page_forward_btn.setIcon(icon11)
        self.page_forward_btn.setIconSize(QSize(32, 37))

        self.horizontalLayout.addWidget(self.page_forward_btn)


        self.gridLayout.addWidget(self.pageButtonsFrameTop, 0, 2, 1, 1, Qt.AlignRight)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.colormaps_dropdown.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.parameters_window.setCurrentIndex(1)
        self.profile_fonts_list.setCurrentIndex(-1)
        self.generate_wordcloud_button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WCGX - WordCloud Generator X-Treme", None))
#if QT_CONFIG(tooltip)
        self.update_settingsProfile_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Update selected Settings profile with current settings</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.update_settingsProfile_btn.setText("")
#if QT_CONFIG(tooltip)
        self.storeSettingsProfile_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Store current settings in wcgx.db", None))
#endif // QT_CONFIG(tooltip)
        self.storeSettingsProfile_btn.setText("")
        self.settingsProfiles_lbl.setText(QCoreApplication.translate("MainWindow", u"Settings Profiles", None))
#if QT_CONFIG(tooltip)
        self.deleteSettingsProfile_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Delete selected Settings profile", None))
#endif // QT_CONFIG(tooltip)
        self.deleteSettingsProfile_btn.setText("")
#if QT_CONFIG(tooltip)
        self.applySettingsProfile_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Apply selected settings", None))
#endif // QT_CONFIG(tooltip)
        self.applySettingsProfile_btn.setText("")
#if QT_CONFIG(tooltip)
        self.storeTextProfile_btn2.setToolTip(QCoreApplication.translate("MainWindow", u"Store current text in wcgx.db", None))
#endif // QT_CONFIG(tooltip)
        self.storeTextProfile_btn2.setText("")
        self.textProfiles_lbl.setText(QCoreApplication.translate("MainWindow", u"Text Profiles", None))
#if QT_CONFIG(tooltip)
        self.deleteTextProfile_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Delete selected Text profile", None))
#endif // QT_CONFIG(tooltip)
        self.deleteTextProfile_btn.setText("")
#if QT_CONFIG(tooltip)
        self.applyTextProfile_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Apply selected text", None))
#endif // QT_CONFIG(tooltip)
        self.applyTextProfile_btn.setText("")
        self.parameters_summary_label.setText(QCoreApplication.translate("MainWindow", u"WordCloud Parameters", None))
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
        self.label_color_presets.setText(QCoreApplication.translate("MainWindow", u"Color Presets", None))
        self.colormaps_dropdown.setItemText(0, QCoreApplication.translate("MainWindow", u"Default", None))
        self.colormaps_dropdown.setItemText(1, QCoreApplication.translate("MainWindow", u"Mask Image Colors", None))
        self.colormaps_dropdown.setItemText(2, QCoreApplication.translate("MainWindow", u"Dark2", None))
        self.colormaps_dropdown.setItemText(3, QCoreApplication.translate("MainWindow", u"Accent", None))
        self.colormaps_dropdown.setItemText(4, QCoreApplication.translate("MainWindow", u"Paired", None))
        self.colormaps_dropdown.setItemText(5, QCoreApplication.translate("MainWindow", u"Random Colors", None))
        self.colormaps_dropdown.setItemText(6, QCoreApplication.translate("MainWindow", u"Set1", None))
        self.colormaps_dropdown.setItemText(7, QCoreApplication.translate("MainWindow", u"Set2", None))
        self.colormaps_dropdown.setItemText(8, QCoreApplication.translate("MainWindow", u"Set3", None))
        self.colormaps_dropdown.setItemText(9, QCoreApplication.translate("MainWindow", u"Reds", None))
        self.colormaps_dropdown.setItemText(10, QCoreApplication.translate("MainWindow", u"Greens", None))
        self.colormaps_dropdown.setItemText(11, QCoreApplication.translate("MainWindow", u"Blues", None))
        self.colormaps_dropdown.setItemText(12, QCoreApplication.translate("MainWindow", u"Greys", None))
        self.colormaps_dropdown.setItemText(13, QCoreApplication.translate("MainWindow", u"Purples", None))
        self.colormaps_dropdown.setItemText(14, QCoreApplication.translate("MainWindow", u"Oranges", None))
        self.colormaps_dropdown.setItemText(15, QCoreApplication.translate("MainWindow", u"Gradient", None))
        self.colormaps_dropdown.setItemText(16, QCoreApplication.translate("MainWindow", u"plasma", None))
        self.colormaps_dropdown.setItemText(17, QCoreApplication.translate("MainWindow", u"Spectral", None))
        self.colormaps_dropdown.setItemText(18, QCoreApplication.translate("MainWindow", u"Pastel1", None))
        self.colormaps_dropdown.setItemText(19, QCoreApplication.translate("MainWindow", u"Pastel2", None))
        self.colormaps_dropdown.setItemText(20, QCoreApplication.translate("MainWindow", u"Wistia", None))
        self.colormaps_dropdown.setItemText(21, QCoreApplication.translate("MainWindow", u"winter", None))
        self.colormaps_dropdown.setItemText(22, QCoreApplication.translate("MainWindow", u"spring", None))
        self.colormaps_dropdown.setItemText(23, QCoreApplication.translate("MainWindow", u"summer", None))
        self.colormaps_dropdown.setItemText(24, QCoreApplication.translate("MainWindow", u"autumn", None))
        self.colormaps_dropdown.setItemText(25, QCoreApplication.translate("MainWindow", u"inferno", None))
        self.colormaps_dropdown.setItemText(26, QCoreApplication.translate("MainWindow", u"magma", None))
        self.colormaps_dropdown.setItemText(27, QCoreApplication.translate("MainWindow", u"twilight", None))
        self.colormaps_dropdown.setItemText(28, QCoreApplication.translate("MainWindow", u"twilight_shifted", None))
        self.colormaps_dropdown.setItemText(29, QCoreApplication.translate("MainWindow", u"hot", None))
        self.colormaps_dropdown.setItemText(30, QCoreApplication.translate("MainWindow", u"afmhot", None))
        self.colormaps_dropdown.setItemText(31, QCoreApplication.translate("MainWindow", u"cool", None))
        self.colormaps_dropdown.setItemText(32, QCoreApplication.translate("MainWindow", u"coolwarm", None))
        self.colormaps_dropdown.setItemText(33, QCoreApplication.translate("MainWindow", u"cubehelix", None))
        self.colormaps_dropdown.setItemText(34, QCoreApplication.translate("MainWindow", u"gray", None))
        self.colormaps_dropdown.setItemText(35, QCoreApplication.translate("MainWindow", u"bone", None))
        self.colormaps_dropdown.setItemText(36, QCoreApplication.translate("MainWindow", u"tab10", None))
        self.colormaps_dropdown.setItemText(37, QCoreApplication.translate("MainWindow", u"tab20", None))
        self.colormaps_dropdown.setItemText(38, QCoreApplication.translate("MainWindow", u"prism", None))
        self.colormaps_dropdown.setItemText(39, QCoreApplication.translate("MainWindow", u"ocean", None))
        self.colormaps_dropdown.setItemText(40, QCoreApplication.translate("MainWindow", u"terrain", None))
        self.colormaps_dropdown.setItemText(41, QCoreApplication.translate("MainWindow", u"rainbow", None))
        self.colormaps_dropdown.setItemText(42, QCoreApplication.translate("MainWindow", u"turbo", None))
        self.colormaps_dropdown.setItemText(43, QCoreApplication.translate("MainWindow", u"gist_ncar_r", None))

#if QT_CONFIG(tooltip)
        self.color_detection_thresh_info_lbl.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.color_detection_thresh_info_lbl.setText(QCoreApplication.translate("MainWindow", u"Color accuracy depends on:\n"
"- Color detection threshold\n"
"- Mask image (colors and size)\n"
"- WordCloud Parameters\n"
"- Font used\n"
"- Length of text\n"
"- Single chars = best results", None))
#if QT_CONFIG(tooltip)
        self.color_detection_thresh_lbl.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.color_detection_thresh_lbl.setText(QCoreApplication.translate("MainWindow", u"Color detection threshold", None))
#if QT_CONFIG(tooltip)
        self.color_thresh_slider.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.color_thresh_slider_lbl.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.color_thresh_slider_lbl.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.gradient_settings_btn.setText(QCoreApplication.translate("MainWindow", u"Gradient Settings", None))
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
        self.ColorsMaxGP.setTitle(QCoreApplication.translate("MainWindow", u"Max", None))
#if QT_CONFIG(tooltip)
        self.rcp_bright.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.rcp_bright.setText(QCoreApplication.translate("MainWindow", u"Bright", None))
#if QT_CONFIG(tooltip)
        self.rcp_gray.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.rcp_gray.setText(QCoreApplication.translate("MainWindow", u"Gray", None))
#if QT_CONFIG(tooltip)
        self.rcp_dark.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.rcp_dark.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
#if QT_CONFIG(tooltip)
        self.rcp_reset.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Reset all colors to max range </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rcp_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
#if QT_CONFIG(tooltip)
        self.colp_pink_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.colp_pink_btn.setText("")
#if QT_CONFIG(tooltip)
        self.colp_wpp_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.colp_wpp_btn.setText("")
#if QT_CONFIG(tooltip)
        self.colp_14_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.colp_14_btn.setText("")
#if QT_CONFIG(tooltip)
        self.colp_e6_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.colp_e6_btn.setText("")
        self.WordInputAndParametersFrame.setStyleSheet(QCoreApplication.translate("MainWindow", u"QListWidget{\n"
"border:2px solid gray;\n"
"color: #141414;\n"
"font: 700 11pt \"Inter\";\n"
"}", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"# Repeat Words On/Off", None))
#if QT_CONFIG(tooltip)
        self.repeat_words_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.repeat_words_label.setText(QCoreApplication.translate("MainWindow", u"## Repeat", None))
#if QT_CONFIG(tooltip)
        self.repeat_checkbox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.repeat_checkbox.setText("")
        self.parameters_window.setTabText(self.parameters_window.indexOf(self.parameters_windowPage_2), QCoreApplication.translate("MainWindow", u"Repeat", None))
        self.min_max_fontSize_lbl.setText(QCoreApplication.translate("MainWindow", u"# Min/Max font-size", None))
#if QT_CONFIG(tooltip)
        self.min_font_size_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.min_font_size_label.setText(QCoreApplication.translate("MainWindow", u"## Min Font Size", None))
#if QT_CONFIG(tooltip)
        self.min_font_size_slider.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Minimum font size</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_min_font_size_slider.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_min_font_size_slider.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.MinFSp49.setText(QCoreApplication.translate("MainWindow", u"49", None))
        self.MinFSp31.setText(QCoreApplication.translate("MainWindow", u"31", None))
        self.MinFSp21.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.MinFSp10.setText(QCoreApplication.translate("MainWindow", u"10", None))
#if QT_CONFIG(tooltip)
        self.max_font_size_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.max_font_size_label.setText(QCoreApplication.translate("MainWindow", u"## Max Font Size", None))
#if QT_CONFIG(tooltip)
        self.max_font_size_slider.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Maximum font size</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_max_font_size_slider.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_max_font_size_slider.setText(QCoreApplication.translate("MainWindow", u"28", None))
        self.MaxFSp250.setText(QCoreApplication.translate("MainWindow", u"250", None))
        self.MaxFSp150.setText(QCoreApplication.translate("MainWindow", u"150", None))
        self.MaxFSp73.setText(QCoreApplication.translate("MainWindow", u"73", None))
        self.MaxFSp50.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.parameters_window.setTabText(self.parameters_window.indexOf(self.parameters_windowPage), QCoreApplication.translate("MainWindow", u"Font Size", None))
#if QT_CONFIG(tooltip)
        self.fontstep_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.fontstep_label.setText(QCoreApplication.translate("MainWindow", u"## Font Step", None))
#if QT_CONFIG(tooltip)
        self.font_step_indicator_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.font_step_indicator_label.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"# Step size between min-max font sizes.", None))
        self.parameters_window.setTabText(self.parameters_window.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Font Step", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"# Minimum margin between words.", None))
#if QT_CONFIG(tooltip)
        self.margin_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.margin_label.setText(QCoreApplication.translate("MainWindow", u"## Margin", None))
#if QT_CONFIG(tooltip)
        self.margin_slider.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Set the margin between the generated words </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_margin_slider.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_margin_slider.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.parameters_window.setTabText(self.parameters_window.indexOf(self.parameters_windowPage3), QCoreApplication.translate("MainWindow", u"Margin", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"# The ratio of times to try horizontal fitting.\n"
"___\n"
"## If odds < 1:\n"
"- Words will be rotated if they don\u2019t fit\n"
"## If odds = 1:\n"
" - Horizontal fit is preferred, but not guaranteed!", None))
#if QT_CONFIG(tooltip)
        self.prefer_horizontal_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.prefer_horizontal_label.setText(QCoreApplication.translate("MainWindow", u"## Horizontal Odds", None))
#if QT_CONFIG(tooltip)
        self.prefer_horizontal_slider.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">1 = Mostly Horizontal Text</span></p><p><span style=\" font-size:10pt;\">0 = No Horizontal Text</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_text_orientation_slider.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_text_orientation_slider.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.parameters_window.setTabText(self.parameters_window.indexOf(self.parameters_windowPage4), QCoreApplication.translate("MainWindow", u"H. Odds", None))
        self.stopwords.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Inter'; font-size:11pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.stopwords.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Stopwords separated by space. Example: word1 word2", None))
        self.lbl_stopwords.setText(QCoreApplication.translate("MainWindow", u"# Words to ignore", None))
        self.parameters_window.setTabText(self.parameters_window.indexOf(self.parameters_windowPage6), QCoreApplication.translate("MainWindow", u"StopWords", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"The Dunning likelihood collocation score is calculated for each\n"
"bigram based on its frequency and compared to the\n"
"expected co-occurrence by random chance.\n"
"The collocation threshold is used as a filtering parameter\n"
"to include only statistically significant bigrams in the word cloud.\n"
"\n"
"- Lower collocation threshold:\n"
"   Makes it easier for word pairs(bigrams)\n"
"   to pass the significance test and be treated as phrases.\n"
"\n"
"- Higher collocation threshold:\n"
"   Bigrams must occur together\n"
"   much more frequently than expected by random chance\n"
"   to be included in the word cloud as 1 phrase.", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"# Enable/Disable the collocations algorithm.\n"
"___", None))
        self.label_collocations.setText(QCoreApplication.translate("MainWindow", u"## Collocations On/Off", None))
#if QT_CONFIG(tooltip)
        self.collocations_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"Enable/Disable collocation algorithm", None))
#endif // QT_CONFIG(tooltip)
        self.collocations_checkbox.setText("")
        self.label_collocations_thresh.setText(QCoreApplication.translate("MainWindow", u"## Collocation Threshold", None))
#if QT_CONFIG(tooltip)
        self.collocations_thresh_slider.setToolTip(QCoreApplication.translate("MainWindow", u"Adjust collocation threshold", None))
#endif // QT_CONFIG(tooltip)
        self.collocation_thresh_slider_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.parameters_window.setTabText(self.parameters_window.indexOf(self.parameters_windowPage8), QCoreApplication.translate("MainWindow", u"Collocations", None))
        self.character_filtering_lbl.setText(QCoreApplication.translate("MainWindow", u"# Character Filtering\n"
"___", None))
#if QT_CONFIG(tooltip)
        self.regxp_heterogeneous_lbl.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.regxp_heterogeneous_lbl.setText(QCoreApplication.translate("MainWindow", u"# Heterogeneous\n"
" - Any character can be a word or part of a word\n"
" - Words are in order", None))
#if QT_CONFIG(tooltip)
        self.heterogeneous_checkbox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.heterogeneous_checkbox.setText("")
#if QT_CONFIG(tooltip)
        self.regxp_url_lbl.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.regxp_url_lbl.setText(QCoreApplication.translate("MainWindow", u"# URL\n"
" - Allows any special character to be part of a word, or a single word\n"
" - example: website.com/page\n"
" - Words in random order", None))
#if QT_CONFIG(tooltip)
        self.url_checkbox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.url_checkbox.setText("")
#if QT_CONFIG(tooltip)
        self.regxp_numbersOnly_lbl.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.regxp_numbersOnly_lbl.setText(QCoreApplication.translate("MainWindow", u"# AlphaNumeric\n"
" - Single number can be a word or part of a word\n"
" - example: 0 0n3\n"
" - Words in random order", None))
#if QT_CONFIG(tooltip)
        self.binary_checkbox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.binary_checkbox.setText("")
#if QT_CONFIG(tooltip)
        self.regxp_disorder_lbl.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.regxp_disorder_lbl.setText(QCoreApplication.translate("MainWindow", u"# Disorder\n"
" - Treats all characters as a word\n"
" - Example: word1 = w o r d 1\n"
" - Words in random order", None))
#if QT_CONFIG(tooltip)
        self.disorder_checkbox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.disorder_checkbox.setText("")
        self.parameters_window.setTabText(self.parameters_window.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Char. Inc.", None))
        self.word_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"WordCloud text goes here.", None))
        self.custom_font_directory_selection.setText(QCoreApplication.translate("MainWindow", u"Custom Fonts Folder", None))
        self.load_emoji_fonts_btn.setText(QCoreApplication.translate("MainWindow", u"Load Emoji Fonts", None))
        self.load_appData_fonts_btn.setText(QCoreApplication.translate("MainWindow", u"Load appData Fonts", None))
        self.load_system_fonts_btn.setText(QCoreApplication.translate("MainWindow", u"Load System Fonts", None))
        self.filter_fonts_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filter", None))
#if QT_CONFIG(tooltip)
        self.open_fs_window.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Download fonts (opens in new window)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.open_fs_window.setText(QCoreApplication.translate("MainWindow", u" Download some fonts", None))
#if QT_CONFIG(tooltip)
        self.storeTextProfile_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Store current text in wcgx.db", None))
#endif // QT_CONFIG(tooltip)
        self.storeTextProfile_btn.setText("")
        self.profile_fonts_lbl.setText(QCoreApplication.translate("MainWindow", u"Profile Fonts:", None))
#if QT_CONFIG(tooltip)
        self.profile_fonts_list.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.apply_profile_font_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Apply currently selected profile font</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.apply_profile_font_btn.setText("")
#if QT_CONFIG(tooltip)
        self.add_profile_font_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add currently applied font to list</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.add_profile_font_btn.setText("")
#if QT_CONFIG(tooltip)
        self.delete_profile_font_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Delete selected font from list</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.delete_profile_font_btn.setText("")
        self.export_format_options.setItemText(0, QCoreApplication.translate("MainWindow", u"PNG", None))
        self.export_format_options.setItemText(1, QCoreApplication.translate("MainWindow", u"SVG", None))
        self.export_format_options.setItemText(2, QCoreApplication.translate("MainWindow", u"BOTH", None))

#if QT_CONFIG(tooltip)
        self.export_format_options.setToolTip(QCoreApplication.translate("MainWindow", u"Output file format", None))
#endif // QT_CONFIG(tooltip)
        self.exportAs_label.setText(QCoreApplication.translate("MainWindow", u"Export As", None))
#if QT_CONFIG(tooltip)
        self.stash_last_generated_button.setToolTip(QCoreApplication.translate("MainWindow", u"Stash the last generated image", None))
#endif // QT_CONFIG(tooltip)
        self.stash_last_generated_button.setText(QCoreApplication.translate("MainWindow", u"Stash", None))
#if QT_CONFIG(tooltip)
        self.delete_last_generated_button.setToolTip(QCoreApplication.translate("MainWindow", u"Delete the last generated image", None))
#endif // QT_CONFIG(tooltip)
        self.delete_last_generated_button.setText(QCoreApplication.translate("MainWindow", u"Del", None))
#if QT_CONFIG(tooltip)
        self.random_seed_lbl.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.random_seed_lbl.setText(QCoreApplication.translate("MainWindow", u"Random Seed", None))
#if QT_CONFIG(tooltip)
        self.random_seed_slider.setToolTip(QCoreApplication.translate("MainWindow", u"Off = colors and layout will be random each time\n"
"int = keep current colors and layout", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.random_seed_int_lbl.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.random_seed_int_lbl.setText(QCoreApplication.translate("MainWindow", u"Off", None))
#if QT_CONFIG(tooltip)
        self.generate_wordcloud_button.setToolTip(QCoreApplication.translate("MainWindow", u"Generate WordCloud", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.generate_wordcloud_button.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.mask_image_thumbnail.setText(QCoreApplication.translate("MainWindow", u"MASK IMAGE WILL BE PLACED HERE", None))
        self.mask_dimensions_label.setText(QCoreApplication.translate("MainWindow", u"mask_dimensions_label", None))
#if QT_CONFIG(tooltip)
        self.mask_select_button.setToolTip(QCoreApplication.translate("MainWindow", u"Select mask image from file", None))
#endif // QT_CONFIG(tooltip)
        self.mask_select_button.setText(QCoreApplication.translate("MainWindow", u"Select Mask", None))
#if QT_CONFIG(tooltip)
        self.fa_mask_select_button.setToolTip(QCoreApplication.translate("MainWindow", u"Select FontAwesome icon and set as mask image", None))
#endif // QT_CONFIG(tooltip)
        self.fa_mask_select_button.setText(QCoreApplication.translate("MainWindow", u"FontAwesome Mask", None))
#if QT_CONFIG(tooltip)
        self.select_destination_button.setToolTip(QCoreApplication.translate("MainWindow", u"Select destination for generated wordcloud", None))
#endif // QT_CONFIG(tooltip)
        self.select_destination_button.setText(QCoreApplication.translate("MainWindow", u"Select Destination", None))
#if QT_CONFIG(tooltip)
        self.open_destination_folder.setToolTip(QCoreApplication.translate("MainWindow", u"Open destination folder", None))
#endif // QT_CONFIG(tooltip)
        self.open_destination_folder.setText(QCoreApplication.translate("MainWindow", u"\u25b2", None))
#if QT_CONFIG(tooltip)
        self.image_scale_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.image_scale_label.setText(QCoreApplication.translate("MainWindow", u"Export Scale", None))
#if QT_CONFIG(tooltip)
        self.scale_slider.setToolTip(QCoreApplication.translate("MainWindow", u"Exported image size multiplier", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_scale_slider.setToolTip(QCoreApplication.translate("MainWindow", u"Exported image size will be multiplied by this number", None))
#endif // QT_CONFIG(tooltip)
        self.label_scale_slider.setText(QCoreApplication.translate("MainWindow", u"1x", None))
#if QT_CONFIG(tooltip)
        self.unicode_Emojis_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Load unicode emojis", None))
#endif // QT_CONFIG(tooltip)
        self.unicode_Emojis_btn.setText(QCoreApplication.translate("MainWindow", u"Unicode Emojis", None))
#if QT_CONFIG(tooltip)
        self.font_Awesome_Icons_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Load FontAwesome icons", None))
#endif // QT_CONFIG(tooltip)
        self.font_Awesome_Icons_btn.setText(QCoreApplication.translate("MainWindow", u"Font Awesome Icons", None))
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

#if QT_CONFIG(tooltip)
        self.emoji_filter_list.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Categories</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.unicodeEmojis_filter_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.fontAwesome_filter_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filter", None))
#if QT_CONFIG(tooltip)
        self.page_back_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Apply currently selected profile font</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.page_back_btn.setText("")
#if QT_CONFIG(tooltip)
        self.page_forward_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Apply currently selected profile font</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.page_forward_btn.setText("")
    # retranslateUi

