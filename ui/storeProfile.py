# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'storeProfile.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QPlainTextEdit,
    QPushButton, QSizePolicy, QWidget)
import Resources_rc

class Ui_StoreProfileWindow(object):
    def setupUi(self, StoreProfileWindow):
        if not StoreProfileWindow.objectName():
            StoreProfileWindow.setObjectName(u"StoreProfileWindow")
        StoreProfileWindow.setWindowModality(Qt.WindowModal)
        StoreProfileWindow.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StoreProfileWindow.sizePolicy().hasHeightForWidth())
        StoreProfileWindow.setSizePolicy(sizePolicy)
        StoreProfileWindow.setMinimumSize(QSize(400, 300))
        StoreProfileWindow.setMaximumSize(QSize(400, 300))
        icon = QIcon()
        icon.addFile(u":/Media/Settings_CogWheel.png", QSize(), QIcon.Normal, QIcon.Off)
        StoreProfileWindow.setWindowIcon(icon)
        StoreProfileWindow.setLayoutDirection(Qt.LeftToRight)
        StoreProfileWindow.setAutoFillBackground(False)
        StoreProfileWindow.setStyleSheet(u"QWidget{\n"
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
        StoreProfileWindow.setSizeGripEnabled(False)
        StoreProfileWindow.setModal(True)
        self.horizontalLayout_3 = QHBoxLayout(StoreProfileWindow)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(20, -1, 20, 20)
        self.frame = QFrame(StoreProfileWindow)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMaximumSize(QSize(500, 500))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.profile_name = QPlainTextEdit(self.frame)
        self.profile_name.setObjectName(u"profile_name")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.profile_name.sizePolicy().hasHeightForWidth())
        self.profile_name.setSizePolicy(sizePolicy2)
        self.profile_name.setMaximumSize(QSize(300, 40))
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(14)
        font.setBold(True)
        self.profile_name.setFont(font)
        self.profile_name.setStyleSheet(u"color:#141414;")

        self.gridLayout.addWidget(self.profile_name, 1, 0, 1, 1, Qt.AlignHCenter)

        self.buttons_Frame = QFrame(self.frame)
        self.buttons_Frame.setObjectName(u"buttons_Frame")
        self.buttons_Frame.setMaximumSize(QSize(400, 100))
        self.horizontalLayout = QHBoxLayout(self.buttons_Frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancel_store_btn = QPushButton(self.buttons_Frame)
        self.cancel_store_btn.setObjectName(u"cancel_store_btn")
        self.cancel_store_btn.setEnabled(True)
        self.cancel_store_btn.setMinimumSize(QSize(150, 40))
        self.cancel_store_btn.setMaximumSize(QSize(150, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setItalic(False)
        self.cancel_store_btn.setFont(font1)
        self.cancel_store_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.cancel_store_btn)

        self.okay_store_btn = QPushButton(self.buttons_Frame)
        self.okay_store_btn.setObjectName(u"okay_store_btn")
        self.okay_store_btn.setEnabled(True)
        self.okay_store_btn.setMinimumSize(QSize(150, 40))
        self.okay_store_btn.setMaximumSize(QSize(150, 16777215))
        self.okay_store_btn.setFont(font1)
        self.okay_store_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.okay_store_btn)


        self.gridLayout.addWidget(self.buttons_Frame, 2, 0, 1, 1)

        self.label_x = QLabel(self.frame)
        self.label_x.setObjectName(u"label_x")
        sizePolicy.setHeightForWidth(self.label_x.sizePolicy().hasHeightForWidth())
        self.label_x.setSizePolicy(sizePolicy)
        self.label_x.setMinimumSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamilies([u"Inter"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_x.setFont(font2)
        self.label_x.setFrameShadow(QFrame.Plain)
        self.label_x.setTextFormat(Qt.AutoText)
        self.label_x.setAlignment(Qt.AlignCenter)
        self.label_x.setWordWrap(True)
        self.label_x.setMargin(0)

        self.gridLayout.addWidget(self.label_x, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.gridLayout.setRowMinimumHeight(0, 1)

        self.horizontalLayout_3.addWidget(self.frame)


        self.retranslateUi(StoreProfileWindow)

        QMetaObject.connectSlotsByName(StoreProfileWindow)
    # setupUi

    def retranslateUi(self, StoreProfileWindow):
        StoreProfileWindow.setWindowTitle(QCoreApplication.translate("StoreProfileWindow", u"Store Profile", None))
        self.profile_name.setPlaceholderText(QCoreApplication.translate("StoreProfileWindow", u"Profile Name", None))
#if QT_CONFIG(tooltip)
        self.cancel_store_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.cancel_store_btn.setText(QCoreApplication.translate("StoreProfileWindow", u"CANCEL", None))
#if QT_CONFIG(tooltip)
        self.okay_store_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.okay_store_btn.setText(QCoreApplication.translate("StoreProfileWindow", u"OK", None))
        self.label_x.setText("")
    # retranslateUi

