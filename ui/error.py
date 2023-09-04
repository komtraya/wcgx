# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)
import Resources_rc

class Ui_Error(object):
    def setupUi(self, Error):
        if not Error.objectName():
            Error.setObjectName(u"Error")
        Error.resize(220, 196)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Error.sizePolicy().hasHeightForWidth())
        Error.setSizePolicy(sizePolicy)
        Error.setMaximumSize(QSize(300, 16777215))
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(11)
        font.setBold(True)
        Error.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Icon/WCGXicon2.ico", QSize(), QIcon.Normal, QIcon.Off)
        Error.setWindowIcon(icon)
        Error.setStyleSheet(u"QWidget{\n"
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
"}")
        self.centralwidget = QWidget(Error)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.anotherLayout = QVBoxLayout(self.frame)
        self.anotherLayout.setSpacing(20)
        self.anotherLayout.setObjectName(u"anotherLayout")
        self.anotherLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.anotherLayout.setContentsMargins(25, 0, 25, 0)
        self.error_lbl = QLabel(self.frame)
        self.error_lbl.setObjectName(u"error_lbl")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.error_lbl.sizePolicy().hasHeightForWidth())
        self.error_lbl.setSizePolicy(sizePolicy3)
        self.error_lbl.setFont(font)
        self.error_lbl.setStyleSheet(u"color:red;")
        self.error_lbl.setTextFormat(Qt.MarkdownText)
        self.error_lbl.setScaledContents(False)
        self.error_lbl.setWordWrap(True)
        self.error_lbl.setMargin(5)

        self.anotherLayout.addWidget(self.error_lbl, 0, Qt.AlignHCenter)

        self.close_btn = QPushButton(self.frame)
        self.close_btn.setObjectName(u"close_btn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy4)
        self.close_btn.setMinimumSize(QSize(121, 30))
        self.close_btn.setMaximumSize(QSize(194, 30))
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(False)
        self.close_btn.setFont(font1)
        self.close_btn.setStyleSheet(u"QPushButton{\n"
"background-color:#212121;\n"
"color:#e6e6e6;\n"
"}")

        self.anotherLayout.addWidget(self.close_btn, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1, Qt.AlignHCenter)

        Error.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Error)
        self.statusbar.setObjectName(u"statusbar")
        Error.setStatusBar(self.statusbar)

        self.retranslateUi(Error)

        QMetaObject.connectSlotsByName(Error)
    # setupUi

    def retranslateUi(self, Error):
        Error.setWindowTitle(QCoreApplication.translate("Error", u"Error", None))
        self.error_lbl.setText(QCoreApplication.translate("Error", u"Error Message", None))
        self.close_btn.setText(QCoreApplication.translate("Error", u"OK", None))
    # retranslateUi

