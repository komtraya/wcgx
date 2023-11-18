# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fsw.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import Resources_rc

class Ui_FontSquirrelWindow(object):
    def setupUi(self, FontSquirrelWindow):
        if not FontSquirrelWindow.objectName():
            FontSquirrelWindow.setObjectName(u"FontSquirrelWindow")
        FontSquirrelWindow.resize(1001, 820)
        FontSquirrelWindow.setMinimumSize(QSize(1000, 820))
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setBold(True)
        FontSquirrelWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Icon/WCGXicon2.ico", QSize(), QIcon.Normal, QIcon.Off)
        FontSquirrelWindow.setWindowIcon(icon)
        FontSquirrelWindow.setStyleSheet(u"QWidget{\n"
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
"}")
        self.gridLayout = QGridLayout(FontSquirrelWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 11, 0, 1, 1)

        self.frame_2 = QFrame(FontSquirrelWindow)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, -1, 70, -1)
        self.select_category_lbl = QLabel(self.frame_2)
        self.select_category_lbl.setObjectName(u"select_category_lbl")
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setKerning(True)
        self.select_category_lbl.setFont(font1)
        self.select_category_lbl.setLineWidth(1)
        self.select_category_lbl.setMidLineWidth(0)
        self.select_category_lbl.setAlignment(Qt.AlignCenter)
        self.select_category_lbl.setMargin(0)
        self.select_category_lbl.setIndent(-1)
        self.select_category_lbl.setOpenExternalLinks(False)

        self.gridLayout_2.addWidget(self.select_category_lbl, 0, 0, 1, 1)

        self.download_category_btn = QPushButton(self.frame_2)
        self.downloadButtonsGroup = QButtonGroup(FontSquirrelWindow)
        self.downloadButtonsGroup.setObjectName(u"downloadButtonsGroup")
        self.downloadButtonsGroup.addButton(self.download_category_btn)
        self.download_category_btn.setObjectName(u"download_category_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.download_category_btn.sizePolicy().hasHeightForWidth())
        self.download_category_btn.setSizePolicy(sizePolicy1)
        self.download_category_btn.setMinimumSize(QSize(211, 40))
        self.download_category_btn.setMaximumSize(QSize(16777215, 40))
        font2 = QFont()
        font2.setFamilies([u"Inter"])
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setItalic(False)
        self.download_category_btn.setFont(font2)
        self.download_category_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #32d026;\n"
"	color: #212121;\n"
"}\n"
"QPushButton:pressed{\n"
"	 padding-left: 3px;\n"
"     padding-top: 3px;\n"
"}")

        self.gridLayout_2.addWidget(self.download_category_btn, 2, 1, 1, 1)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.horizontalLayout2 = QHBoxLayout(self.frame)
        self.horizontalLayout2.setSpacing(0)
        self.horizontalLayout2.setObjectName(u"horizontalLayout2")
        self.horizontalLayout2.setContentsMargins(0, -1, -1, -1)
        self.fs_category_list = QComboBox(self.frame)
        self.fs_category_list.addItem("")
        self.fs_category_list.addItem("")
        self.fs_category_list.addItem("")
        self.fs_category_list.addItem("")
        self.fs_category_list.addItem("")
        self.fs_category_list.addItem("")
        self.fs_category_list.addItem("")
        self.fs_category_list.addItem("")
        self.fs_category_list.addItem("")
        self.fs_category_list.addItem("")
        self.fs_category_list.addItem("")
        self.fs_category_list.addItem("")
        self.fs_category_list.addItem("")
        self.fs_category_list.addItem("")
        self.fs_category_list.addItem("")
        self.fs_category_list.setObjectName(u"fs_category_list")
        sizePolicy.setHeightForWidth(self.fs_category_list.sizePolicy().hasHeightForWidth())
        self.fs_category_list.setSizePolicy(sizePolicy)
        self.fs_category_list.setMinimumSize(QSize(211, 43))
        font3 = QFont()
        font3.setFamilies([u"Inter"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.fs_category_list.setFont(font3)
        self.fs_category_list.setStyleSheet(u"/* Style the QComboBox */\n"
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
        self.fs_category_list.setMaxVisibleItems(20)
        self.fs_category_list.setIconSize(QSize(32, 32))
        self.fs_category_list.setFrame(True)

        self.horizontalLayout2.addWidget(self.fs_category_list)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, 9)
        self.total_fonts_lbl = QLabel(self.frame_3)
        self.total_fonts_lbl.setObjectName(u"total_fonts_lbl")
        self.total_fonts_lbl.setFont(font1)
        self.total_fonts_lbl.setMargin(5)
        self.total_fonts_lbl.setIndent(-1)
        self.total_fonts_lbl.setOpenExternalLinks(False)

        self.horizontalLayout_4.addWidget(self.total_fonts_lbl)

        self.font_count_lbl = QLabel(self.frame_3)
        self.font_count_lbl.setObjectName(u"font_count_lbl")
        self.font_count_lbl.setMinimumSize(QSize(49, 29))
        font4 = QFont()
        font4.setFamilies([u"Inter"])
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setKerning(True)
        self.font_count_lbl.setFont(font4)
        self.font_count_lbl.setMargin(5)
        self.font_count_lbl.setIndent(-1)
        self.font_count_lbl.setOpenExternalLinks(False)

        self.horizontalLayout_4.addWidget(self.font_count_lbl, 0, Qt.AlignHCenter)


        self.horizontalLayout2.addWidget(self.frame_3)


        self.gridLayout_2.addWidget(self.frame, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 3, 0, 1, 1, Qt.AlignHCenter)

        self.info_lbl = QLabel(FontSquirrelWindow)
        self.info_lbl.setObjectName(u"info_lbl")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.info_lbl.sizePolicy().hasHeightForWidth())
        self.info_lbl.setSizePolicy(sizePolicy2)
        self.info_lbl.setMinimumSize(QSize(600, 50))
        self.info_lbl.setFont(font4)
        self.info_lbl.setTextFormat(Qt.MarkdownText)
        self.info_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.info_lbl.setWordWrap(True)

        self.gridLayout.addWidget(self.info_lbl, 10, 0, 1, 1, Qt.AlignHCenter)

        self.FS_FullFrame = QFrame(FontSquirrelWindow)
        self.FS_FullFrame.setObjectName(u"FS_FullFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.FS_FullFrame.sizePolicy().hasHeightForWidth())
        self.FS_FullFrame.setSizePolicy(sizePolicy3)
        self.FS_FullFrame.setFont(font)
        self.verticalLayout_9 = QVBoxLayout(self.FS_FullFrame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(20, 0, -1, -1)
        self.Masks_FilterFrame = QFrame(self.FS_FullFrame)
        self.Masks_FilterFrame.setObjectName(u"Masks_FilterFrame")
        sizePolicy.setHeightForWidth(self.Masks_FilterFrame.sizePolicy().hasHeightForWidth())
        self.Masks_FilterFrame.setSizePolicy(sizePolicy)
        self.horizontalLayout_8 = QHBoxLayout(self.Masks_FilterFrame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")

        self.verticalLayout_9.addWidget(self.Masks_FilterFrame, 0, Qt.AlignHCenter)

        self.downloadImageFA_Frame = QFrame(self.FS_FullFrame)
        self.downloadImageFA_Frame.setObjectName(u"downloadImageFA_Frame")
        sizePolicy.setHeightForWidth(self.downloadImageFA_Frame.sizePolicy().hasHeightForWidth())
        self.downloadImageFA_Frame.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.downloadImageFA_Frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.verticalLayout_9.addWidget(self.downloadImageFA_Frame, 0, Qt.AlignHCenter)

        self.download_info_lbl = QLabel(self.FS_FullFrame)
        self.download_info_lbl.setObjectName(u"download_info_lbl")
        sizePolicy.setHeightForWidth(self.download_info_lbl.sizePolicy().hasHeightForWidth())
        self.download_info_lbl.setSizePolicy(sizePolicy)
        self.download_info_lbl.setMinimumSize(QSize(500, 98))
        self.download_info_lbl.setFont(font1)
        self.download_info_lbl.setLineWidth(1)
        self.download_info_lbl.setMidLineWidth(0)
        self.download_info_lbl.setTextFormat(Qt.MarkdownText)
        self.download_info_lbl.setScaledContents(False)
        self.download_info_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.download_info_lbl.setWordWrap(True)
        self.download_info_lbl.setMargin(0)
        self.download_info_lbl.setIndent(-1)
        self.download_info_lbl.setOpenExternalLinks(False)

        self.verticalLayout_9.addWidget(self.download_info_lbl, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.FS_FullFrame, 0, 0, 1, 1)

        self.downloading_lbl = QLabel(FontSquirrelWindow)
        self.downloading_lbl.setObjectName(u"downloading_lbl")
        sizePolicy.setHeightForWidth(self.downloading_lbl.sizePolicy().hasHeightForWidth())
        self.downloading_lbl.setSizePolicy(sizePolicy)
        self.downloading_lbl.setFont(font1)
        self.downloading_lbl.setMargin(0)
        self.downloading_lbl.setIndent(-1)
        self.downloading_lbl.setOpenExternalLinks(False)

        self.gridLayout.addWidget(self.downloading_lbl, 9, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 6, 0, 1, 1)


        self.retranslateUi(FontSquirrelWindow)

        QMetaObject.connectSlotsByName(FontSquirrelWindow)
    # setupUi

    def retranslateUi(self, FontSquirrelWindow):
        FontSquirrelWindow.setWindowTitle(QCoreApplication.translate("FontSquirrelWindow", u"Download Font Squirrel Fonts", None))
#if QT_CONFIG(tooltip)
        self.select_category_lbl.setToolTip(QCoreApplication.translate("FontSquirrelWindow", u"Exported image size will be multiplied by this number", None))
#endif // QT_CONFIG(tooltip)
        self.select_category_lbl.setText(QCoreApplication.translate("FontSquirrelWindow", u"Select category of fonts to download:", None))
#if QT_CONFIG(tooltip)
        self.download_category_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.download_category_btn.setText(QCoreApplication.translate("FontSquirrelWindow", u"Download Category", None))
        self.fs_category_list.setItemText(0, QCoreApplication.translate("FontSquirrelWindow", u"Blackletter", None))
        self.fs_category_list.setItemText(1, QCoreApplication.translate("FontSquirrelWindow", u"Calligraphic", None))
        self.fs_category_list.setItemText(2, QCoreApplication.translate("FontSquirrelWindow", u"Comic", None))
        self.fs_category_list.setItemText(3, QCoreApplication.translate("FontSquirrelWindow", u"Dingbat", None))
        self.fs_category_list.setItemText(4, QCoreApplication.translate("FontSquirrelWindow", u"Handdrawn", None))
        self.fs_category_list.setItemText(5, QCoreApplication.translate("FontSquirrelWindow", u"Display", None))
        self.fs_category_list.setItemText(6, QCoreApplication.translate("FontSquirrelWindow", u"Monospaced", None))
        self.fs_category_list.setItemText(7, QCoreApplication.translate("FontSquirrelWindow", u"Novelty", None))
        self.fs_category_list.setItemText(8, QCoreApplication.translate("FontSquirrelWindow", u"Pixel", None))
        self.fs_category_list.setItemText(9, QCoreApplication.translate("FontSquirrelWindow", u"Programming", None))
        self.fs_category_list.setItemText(10, QCoreApplication.translate("FontSquirrelWindow", u"Retro", None))
        self.fs_category_list.setItemText(11, QCoreApplication.translate("FontSquirrelWindow", u"Script", None))
        self.fs_category_list.setItemText(12, QCoreApplication.translate("FontSquirrelWindow", u"Serif", None))
        self.fs_category_list.setItemText(13, QCoreApplication.translate("FontSquirrelWindow", u"Stencil", None))
        self.fs_category_list.setItemText(14, QCoreApplication.translate("FontSquirrelWindow", u"All", None))

#if QT_CONFIG(tooltip)
        self.total_fonts_lbl.setToolTip(QCoreApplication.translate("FontSquirrelWindow", u"Exported image size will be multiplied by this number", None))
#endif // QT_CONFIG(tooltip)
        self.total_fonts_lbl.setText(QCoreApplication.translate("FontSquirrelWindow", u"Font Families:", None))
#if QT_CONFIG(tooltip)
        self.font_count_lbl.setToolTip(QCoreApplication.translate("FontSquirrelWindow", u"Exported image size will be multiplied by this number", None))
#endif // QT_CONFIG(tooltip)
        self.font_count_lbl.setText(QCoreApplication.translate("FontSquirrelWindow", u"21", None))
        self.info_lbl.setText("")
#if QT_CONFIG(tooltip)
        self.download_info_lbl.setToolTip(QCoreApplication.translate("FontSquirrelWindow", u"Exported image size will be multiplied by this number", None))
#endif // QT_CONFIG(tooltip)
        self.download_info_lbl.setText(QCoreApplication.translate("FontSquirrelWindow", u"- Fonts will be downloaded from Font Squirrel\n"
"- Files are downloaded in .zip format\n"
"- WCGX will unzip all downloaded font families automatically, transfer the fonts in a new folder named after the font category you downloaded, delete all other files, including the original zip file.\n"
"- All font names contain the \"-webfont\" suffix - they will be renamed to eliminate that.", None))
#if QT_CONFIG(tooltip)
        self.downloading_lbl.setToolTip(QCoreApplication.translate("FontSquirrelWindow", u"Exported image size will be multiplied by this number", None))
#endif // QT_CONFIG(tooltip)
        self.downloading_lbl.setText("")
    # retranslateUi

