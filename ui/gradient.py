# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gradient.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSlider,
    QVBoxLayout, QWidget)
import Resources_rc

class Ui_GradientWindow(object):
    def setupUi(self, GradientWindow):
        if not GradientWindow.objectName():
            GradientWindow.setObjectName(u"GradientWindow")
        GradientWindow.resize(345, 310)
        icon = QIcon()
        icon.addFile(u":/Icon/WCGXicon2.ico", QSize(), QIcon.Normal, QIcon.Off)
        GradientWindow.setWindowIcon(icon)
        GradientWindow.setStyleSheet(u"QWidget{\n"
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
        self.gridLayout = QGridLayout(GradientWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ColorOptionsFrame = QFrame(GradientWindow)
        self.ColorOptionsFrame.setObjectName(u"ColorOptionsFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ColorOptionsFrame.sizePolicy().hasHeightForWidth())
        self.ColorOptionsFrame.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.ColorOptionsFrame)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gradient_colors_section_lbl = QLabel(self.ColorOptionsFrame)
        self.gradient_colors_section_lbl.setObjectName(u"gradient_colors_section_lbl")
        sizePolicy.setHeightForWidth(self.gradient_colors_section_lbl.sizePolicy().hasHeightForWidth())
        self.gradient_colors_section_lbl.setSizePolicy(sizePolicy)
        self.gradient_colors_section_lbl.setMinimumSize(QSize(71, 24))
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(11)
        font.setBold(True)
        self.gradient_colors_section_lbl.setFont(font)
        self.gradient_colors_section_lbl.setTextFormat(Qt.MarkdownText)

        self.verticalLayout.addWidget(self.gradient_colors_section_lbl, 0, Qt.AlignHCenter)

        self.FirsrColorFrame = QFrame(self.ColorOptionsFrame)
        self.FirsrColorFrame.setObjectName(u"FirsrColorFrame")
        sizePolicy.setHeightForWidth(self.FirsrColorFrame.sizePolicy().hasHeightForWidth())
        self.FirsrColorFrame.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.FirsrColorFrame)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.select_first_color_btn = QPushButton(self.FirsrColorFrame)
        self.select_first_color_btn.setObjectName(u"select_first_color_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.select_first_color_btn.sizePolicy().hasHeightForWidth())
        self.select_first_color_btn.setSizePolicy(sizePolicy1)
        self.select_first_color_btn.setMinimumSize(QSize(107, 30))
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setItalic(False)
        self.select_first_color_btn.setFont(font1)
        self.select_first_color_btn.setStyleSheet(u"QPushButton{\n"
"background-color:#212121;\n"
"color:#e6e6e6;\n"
"}")
        self.select_first_color_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.select_first_color_btn)

        self.first_gradient_lbl = QLabel(self.FirsrColorFrame)
        self.first_gradient_lbl.setObjectName(u"first_gradient_lbl")
        sizePolicy.setHeightForWidth(self.first_gradient_lbl.sizePolicy().hasHeightForWidth())
        self.first_gradient_lbl.setSizePolicy(sizePolicy)
        self.first_gradient_lbl.setMinimumSize(QSize(71, 24))
        self.first_gradient_lbl.setFont(font)
        self.first_gradient_lbl.setTextFormat(Qt.MarkdownText)

        self.horizontalLayout_2.addWidget(self.first_gradient_lbl)


        self.verticalLayout.addWidget(self.FirsrColorFrame, 0, Qt.AlignHCenter)

        self.SecondColorFrame = QFrame(self.ColorOptionsFrame)
        self.SecondColorFrame.setObjectName(u"SecondColorFrame")
        sizePolicy.setHeightForWidth(self.SecondColorFrame.sizePolicy().hasHeightForWidth())
        self.SecondColorFrame.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.SecondColorFrame)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.select_second_color_btn = QPushButton(self.SecondColorFrame)
        self.select_second_color_btn.setObjectName(u"select_second_color_btn")
        sizePolicy1.setHeightForWidth(self.select_second_color_btn.sizePolicy().hasHeightForWidth())
        self.select_second_color_btn.setSizePolicy(sizePolicy1)
        self.select_second_color_btn.setMinimumSize(QSize(107, 30))
        self.select_second_color_btn.setFont(font1)
        self.select_second_color_btn.setStyleSheet(u"QPushButton{\n"
"background-color:#212121;\n"
"color:#e6e6e6;\n"
"}")
        self.select_second_color_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.select_second_color_btn)

        self.second_gradient_lbl = QLabel(self.SecondColorFrame)
        self.second_gradient_lbl.setObjectName(u"second_gradient_lbl")
        sizePolicy.setHeightForWidth(self.second_gradient_lbl.sizePolicy().hasHeightForWidth())
        self.second_gradient_lbl.setSizePolicy(sizePolicy)
        self.second_gradient_lbl.setMinimumSize(QSize(71, 24))
        self.second_gradient_lbl.setFont(font)
        self.second_gradient_lbl.setTextFormat(Qt.MarkdownText)

        self.horizontalLayout.addWidget(self.second_gradient_lbl)


        self.verticalLayout.addWidget(self.SecondColorFrame, 0, Qt.AlignHCenter)

        self.TransparencyFrameAll = QFrame(self.ColorOptionsFrame)
        self.TransparencyFrameAll.setObjectName(u"TransparencyFrameAll")
        self.verticalLayout_2 = QVBoxLayout(self.TransparencyFrameAll)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.transparency_section_lbl = QLabel(self.TransparencyFrameAll)
        self.transparency_section_lbl.setObjectName(u"transparency_section_lbl")
        sizePolicy.setHeightForWidth(self.transparency_section_lbl.sizePolicy().hasHeightForWidth())
        self.transparency_section_lbl.setSizePolicy(sizePolicy)
        self.transparency_section_lbl.setMinimumSize(QSize(71, 24))
        self.transparency_section_lbl.setFont(font)
        self.transparency_section_lbl.setTextFormat(Qt.MarkdownText)

        self.verticalLayout_2.addWidget(self.transparency_section_lbl)

        self.transparencyFrame = QFrame(self.TransparencyFrameAll)
        self.transparencyFrame.setObjectName(u"transparencyFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.transparencyFrame.sizePolicy().hasHeightForWidth())
        self.transparencyFrame.setSizePolicy(sizePolicy2)
        self.horizontalLayout_3 = QHBoxLayout(self.transparencyFrame)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.transparency_slider = QSlider(self.transparencyFrame)
        self.transparency_slider.setObjectName(u"transparency_slider")
        self.transparency_slider.setMinimumSize(QSize(0, 40))
        self.transparency_slider.setMaximumSize(QSize(300, 16777215))
        self.transparency_slider.setCursor(QCursor(Qt.PointingHandCursor))
        self.transparency_slider.setMouseTracking(False)
        self.transparency_slider.setFocusPolicy(Qt.StrongFocus)
        self.transparency_slider.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.transparency_slider.setLayoutDirection(Qt.LeftToRight)
        self.transparency_slider.setStyleSheet(u"QSlider::groove {\n"
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
        self.transparency_slider.setMinimum(20)
        self.transparency_slider.setMaximum(255)
        self.transparency_slider.setPageStep(1)
        self.transparency_slider.setValue(255)
        self.transparency_slider.setOrientation(Qt.Horizontal)
        self.transparency_slider.setInvertedControls(False)
        self.transparency_slider.setTickPosition(QSlider.NoTicks)
        self.transparency_slider.setTickInterval(0)

        self.horizontalLayout_3.addWidget(self.transparency_slider)

        self.transparency_indicator_lbl = QLabel(self.transparencyFrame)
        self.transparency_indicator_lbl.setObjectName(u"transparency_indicator_lbl")
        sizePolicy2.setHeightForWidth(self.transparency_indicator_lbl.sizePolicy().hasHeightForWidth())
        self.transparency_indicator_lbl.setSizePolicy(sizePolicy2)
        self.transparency_indicator_lbl.setFont(font)
        self.transparency_indicator_lbl.setTextFormat(Qt.MarkdownText)

        self.horizontalLayout_3.addWidget(self.transparency_indicator_lbl)


        self.verticalLayout_2.addWidget(self.transparencyFrame)


        self.verticalLayout.addWidget(self.TransparencyFrameAll, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.ColorOptionsFrame, 0, 0, 1, 1)


        self.retranslateUi(GradientWindow)

        QMetaObject.connectSlotsByName(GradientWindow)
    # setupUi

    def retranslateUi(self, GradientWindow):
        GradientWindow.setWindowTitle(QCoreApplication.translate("GradientWindow", u"Gradient Options", None))
        self.gradient_colors_section_lbl.setText(QCoreApplication.translate("GradientWindow", u"## Gradient Colors", None))
        self.select_first_color_btn.setText(QCoreApplication.translate("GradientWindow", u"First Color", None))
        self.first_gradient_lbl.setText(QCoreApplication.translate("GradientWindow", u"#555555", None))
        self.select_second_color_btn.setText(QCoreApplication.translate("GradientWindow", u"Second Color", None))
        self.second_gradient_lbl.setText(QCoreApplication.translate("GradientWindow", u"#ffffff", None))
        self.transparency_section_lbl.setText(QCoreApplication.translate("GradientWindow", u"## Transparency", None))
#if QT_CONFIG(tooltip)
        self.transparency_slider.setToolTip(QCoreApplication.translate("GradientWindow", u"<html><head/><body><p>Exported image size multiplier</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.transparency_indicator_lbl.setText(QCoreApplication.translate("GradientWindow", u"255", None))
    # retranslateUi

