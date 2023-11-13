# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gallery.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QButtonGroup, QFrame,
    QGridLayout, QHBoxLayout, QListView, QListWidget,
    QListWidgetItem, QPlainTextEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import Resources_rc

class Ui_GalleryWindow(object):
    def setupUi(self, GalleryWindow):
        if not GalleryWindow.objectName():
            GalleryWindow.setObjectName(u"GalleryWindow")
        GalleryWindow.resize(1000, 820)
        GalleryWindow.setMinimumSize(QSize(1000, 820))
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setBold(True)
        GalleryWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Icon/WCGXicon2.ico", QSize(), QIcon.Normal, QIcon.Off)
        GalleryWindow.setWindowIcon(icon)
        GalleryWindow.setStyleSheet(u"QWidget{\n"
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
"}")
        self.gridLayout = QGridLayout(GalleryWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Masks_FullFrame = QFrame(GalleryWindow)
        self.Masks_FullFrame.setObjectName(u"Masks_FullFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Masks_FullFrame.sizePolicy().hasHeightForWidth())
        self.Masks_FullFrame.setSizePolicy(sizePolicy)
        self.Masks_FullFrame.setFont(font)
        self.verticalLayout_9 = QVBoxLayout(self.Masks_FullFrame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(20, -1, -1, -1)
        self.Masks_FilterFrame = QFrame(self.Masks_FullFrame)
        self.Masks_FilterFrame.setObjectName(u"Masks_FilterFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Masks_FilterFrame.sizePolicy().hasHeightForWidth())
        self.Masks_FilterFrame.setSizePolicy(sizePolicy1)
        self.horizontalLayout_8 = QHBoxLayout(self.Masks_FilterFrame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.fa_filter_input = QPlainTextEdit(self.Masks_FilterFrame)
        self.fa_filter_input.setObjectName(u"fa_filter_input")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.fa_filter_input.sizePolicy().hasHeightForWidth())
        self.fa_filter_input.setSizePolicy(sizePolicy2)
        self.fa_filter_input.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.fa_filter_input.setFont(font1)
        self.fa_filter_input.setStyleSheet(u"color:#141414;")

        self.horizontalLayout_8.addWidget(self.fa_filter_input)


        self.verticalLayout_9.addWidget(self.Masks_FilterFrame, 0, Qt.AlignHCenter)

        self.downloadImageFA_Frame = QFrame(self.Masks_FullFrame)
        self.downloadImageFA_Frame.setObjectName(u"downloadImageFA_Frame")
        sizePolicy1.setHeightForWidth(self.downloadImageFA_Frame.sizePolicy().hasHeightForWidth())
        self.downloadImageFA_Frame.setSizePolicy(sizePolicy1)
        self.horizontalLayout_3 = QHBoxLayout(self.downloadImageFA_Frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.export_fa_png_btn = QPushButton(self.downloadImageFA_Frame)
        self.downloadButtonsGroup = QButtonGroup(GalleryWindow)
        self.downloadButtonsGroup.setObjectName(u"downloadButtonsGroup")
        self.downloadButtonsGroup.addButton(self.export_fa_png_btn)
        self.export_fa_png_btn.setObjectName(u"export_fa_png_btn")
        self.export_fa_png_btn.setMinimumSize(QSize(40, 40))
        self.export_fa_png_btn.setMaximumSize(QSize(40, 40))
        font2 = QFont()
        font2.setFamilies([u"Inter"])
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setItalic(False)
        self.export_fa_png_btn.setFont(font2)
        self.export_fa_png_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #32d026;\n"
"    color: #212121;\n"
"}\n"
"QPushButton:pressed{\n"
"	 padding-left: 3px;\n"
"     padding-top: 3px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.export_fa_png_btn)

        self.export_fa_svg_btn = QPushButton(self.downloadImageFA_Frame)
        self.downloadButtonsGroup.addButton(self.export_fa_svg_btn)
        self.export_fa_svg_btn.setObjectName(u"export_fa_svg_btn")
        self.export_fa_svg_btn.setMinimumSize(QSize(40, 40))
        self.export_fa_svg_btn.setMaximumSize(QSize(40, 40))
        self.export_fa_svg_btn.setFont(font2)
        self.export_fa_svg_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #32d026;\n"
"	color: #212121;\n"
"}\n"
"QPushButton:pressed{\n"
"	 padding-left: 3px;\n"
"     padding-top: 3px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.export_fa_svg_btn)


        self.verticalLayout_9.addWidget(self.downloadImageFA_Frame, 0, Qt.AlignHCenter)

        self.masks_list = QListWidget(self.Masks_FullFrame)
        self.masks_list.setObjectName(u"masks_list")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.masks_list.sizePolicy().hasHeightForWidth())
        self.masks_list.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Emoji"])
        font3.setPointSize(40)
        font3.setBold(False)
        self.masks_list.setFont(font3)
        self.masks_list.setStyleSheet(u"QListWidget::item:selected {\n"
"    background: rgba(0,200,0,200);\n"
"}\n"
"QListWidget::item:hover {\n"
"    background: rgba(0,200,0,200);\n"
"}\n"
"QListWidget{\n"
"background:#141414;\n"
"border-radius:0px;\n"
"border:1px solid #e6e6e6;\n"
"}")
        self.masks_list.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.masks_list.setAutoScroll(False)
        self.masks_list.setAutoScrollMargin(20)
        self.masks_list.setTextElideMode(Qt.ElideNone)
        self.masks_list.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.masks_list.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.masks_list.setMovement(QListView.Snap)
        self.masks_list.setProperty("isWrapping", True)
        self.masks_list.setResizeMode(QListView.Adjust)
        self.masks_list.setLayoutMode(QListView.SinglePass)
        self.masks_list.setViewMode(QListView.IconMode)
        self.masks_list.setUniformItemSizes(False)

        self.verticalLayout_9.addWidget(self.masks_list)


        self.gridLayout.addWidget(self.Masks_FullFrame, 0, 0, 1, 1)


        self.retranslateUi(GalleryWindow)

        QMetaObject.connectSlotsByName(GalleryWindow)
    # setupUi

    def retranslateUi(self, GalleryWindow):
        GalleryWindow.setWindowTitle(QCoreApplication.translate("GalleryWindow", u"Mask Gallery", None))
        self.fa_filter_input.setPlaceholderText(QCoreApplication.translate("GalleryWindow", u"Filter", None))
#if QT_CONFIG(tooltip)
        self.export_fa_png_btn.setToolTip(QCoreApplication.translate("GalleryWindow", u"Export selected icon", None))
#endif // QT_CONFIG(tooltip)
        self.export_fa_png_btn.setText(QCoreApplication.translate("GalleryWindow", u"PNG", None))
#if QT_CONFIG(tooltip)
        self.export_fa_svg_btn.setToolTip(QCoreApplication.translate("GalleryWindow", u"Export selected icon", None))
#endif // QT_CONFIG(tooltip)
        self.export_fa_svg_btn.setText(QCoreApplication.translate("GalleryWindow", u"SVG", None))
    # retranslateUi

