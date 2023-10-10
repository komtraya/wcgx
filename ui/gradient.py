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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSlider, QVBoxLayout, QWidget)
import Resources_rc

class Ui_GradientWindow(object):
    def setupUi(self, GradientWindow):
        if not GradientWindow.objectName():
            GradientWindow.setObjectName(u"GradientWindow")
        GradientWindow.resize(500, 505)
        GradientWindow.setMinimumSize(QSize(500, 505))
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
        self.gradientPropertiesFrame = QFrame(self.ColorOptionsFrame)
        self.gradientPropertiesFrame.setObjectName(u"gradientPropertiesFrame")
        self.propertiesLayout = QVBoxLayout(self.gradientPropertiesFrame)
        self.propertiesLayout.setSpacing(10)
        self.propertiesLayout.setObjectName(u"propertiesLayout")
        self.propertiesLayout.setContentsMargins(0, 0, 0, 0)
        self.gpFrame = QFrame(self.gradientPropertiesFrame)
        self.gpFrame.setObjectName(u"gpFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.gpFrame.sizePolicy().hasHeightForWidth())
        self.gpFrame.setSizePolicy(sizePolicy1)
        self.horizontalLayout_38 = QHBoxLayout(self.gpFrame)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.gradient_transition_lbl = QLabel(self.gpFrame)
        self.gradient_transition_lbl.setObjectName(u"gradient_transition_lbl")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.gradient_transition_lbl.sizePolicy().hasHeightForWidth())
        self.gradient_transition_lbl.setSizePolicy(sizePolicy2)
        self.gradient_transition_lbl.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setKerning(True)
        self.gradient_transition_lbl.setFont(font)
        self.gradient_transition_lbl.setTextFormat(Qt.MarkdownText)

        self.horizontalLayout_38.addWidget(self.gradient_transition_lbl)

        self.gradient_push_slider = QSlider(self.gpFrame)
        self.gradient_push_slider.setObjectName(u"gradient_push_slider")
        self.gradient_push_slider.setMinimumSize(QSize(0, 40))
        self.gradient_push_slider.setMaximumSize(QSize(150, 16777215))
        self.gradient_push_slider.setCursor(QCursor(Qt.PointingHandCursor))
        self.gradient_push_slider.setMouseTracking(False)
        self.gradient_push_slider.setFocusPolicy(Qt.StrongFocus)
        self.gradient_push_slider.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.gradient_push_slider.setLayoutDirection(Qt.LeftToRight)
        self.gradient_push_slider.setStyleSheet(u"QSlider::groove {\n"
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
        self.gradient_push_slider.setMinimum(0)
        self.gradient_push_slider.setMaximum(50)
        self.gradient_push_slider.setSingleStep(5)
        self.gradient_push_slider.setPageStep(5)
        self.gradient_push_slider.setValue(15)
        self.gradient_push_slider.setTracking(True)
        self.gradient_push_slider.setOrientation(Qt.Horizontal)
        self.gradient_push_slider.setInvertedControls(False)
        self.gradient_push_slider.setTickPosition(QSlider.NoTicks)
        self.gradient_push_slider.setTickInterval(0)

        self.horizontalLayout_38.addWidget(self.gradient_push_slider)

        self.gradient_push_indicator_lbl = QLabel(self.gpFrame)
        self.gradient_push_indicator_lbl.setObjectName(u"gradient_push_indicator_lbl")
        sizePolicy2.setHeightForWidth(self.gradient_push_indicator_lbl.sizePolicy().hasHeightForWidth())
        self.gradient_push_indicator_lbl.setSizePolicy(sizePolicy2)
        self.gradient_push_indicator_lbl.setMinimumSize(QSize(29, 0))
        self.gradient_push_indicator_lbl.setMaximumSize(QSize(50, 50))
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setKerning(True)
        self.gradient_push_indicator_lbl.setFont(font1)
        self.gradient_push_indicator_lbl.setMargin(5)
        self.gradient_push_indicator_lbl.setIndent(-1)
        self.gradient_push_indicator_lbl.setOpenExternalLinks(False)

        self.horizontalLayout_38.addWidget(self.gradient_push_indicator_lbl)


        self.propertiesLayout.addWidget(self.gpFrame, 0, Qt.AlignHCenter)

        self.TransparencyFrame = QFrame(self.gradientPropertiesFrame)
        self.TransparencyFrame.setObjectName(u"TransparencyFrame")
        self.poop = QHBoxLayout(self.TransparencyFrame)
        self.poop.setObjectName(u"poop")
        self.transparency_section_lbl = QLabel(self.TransparencyFrame)
        self.transparency_section_lbl.setObjectName(u"transparency_section_lbl")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.transparency_section_lbl.sizePolicy().hasHeightForWidth())
        self.transparency_section_lbl.setSizePolicy(sizePolicy3)
        self.transparency_section_lbl.setMinimumSize(QSize(137, 0))
        font2 = QFont()
        font2.setFamilies([u"Inter"])
        font2.setPointSize(9)
        font2.setBold(True)
        self.transparency_section_lbl.setFont(font2)
        self.transparency_section_lbl.setTextFormat(Qt.MarkdownText)

        self.poop.addWidget(self.transparency_section_lbl)

        self.transparency_slider = QSlider(self.TransparencyFrame)
        self.transparency_slider.setObjectName(u"transparency_slider")
        self.transparency_slider.setMinimumSize(QSize(0, 40))
        self.transparency_slider.setMaximumSize(QSize(150, 16777215))
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

        self.poop.addWidget(self.transparency_slider)

        self.transparency_indicator_lbl = QLabel(self.TransparencyFrame)
        self.transparency_indicator_lbl.setObjectName(u"transparency_indicator_lbl")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.transparency_indicator_lbl.sizePolicy().hasHeightForWidth())
        self.transparency_indicator_lbl.setSizePolicy(sizePolicy4)
        font3 = QFont()
        font3.setFamilies([u"Inter"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.transparency_indicator_lbl.setFont(font3)
        self.transparency_indicator_lbl.setTextFormat(Qt.MarkdownText)

        self.poop.addWidget(self.transparency_indicator_lbl)


        self.propertiesLayout.addWidget(self.TransparencyFrame, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.gradientPropertiesFrame)

        self.FirsrColorFrame = QFrame(self.ColorOptionsFrame)
        self.FirsrColorFrame.setObjectName(u"FirsrColorFrame")
        sizePolicy.setHeightForWidth(self.FirsrColorFrame.sizePolicy().hasHeightForWidth())
        self.FirsrColorFrame.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.FirsrColorFrame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.select_first_color_btn = QPushButton(self.FirsrColorFrame)
        self.select_first_color_btn.setObjectName(u"select_first_color_btn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.select_first_color_btn.sizePolicy().hasHeightForWidth())
        self.select_first_color_btn.setSizePolicy(sizePolicy5)
        self.select_first_color_btn.setMinimumSize(QSize(107, 30))
        font4 = QFont()
        font4.setFamilies([u"Inter"])
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setItalic(False)
        self.select_first_color_btn.setFont(font4)
        self.select_first_color_btn.setStyleSheet(u"QPushButton{\n"
"background-color:#aa0000;\n"
"color:#e6e6e6;\n"
"}")
        self.select_first_color_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.select_first_color_btn)

        self.first_gradient_lbl = QLabel(self.FirsrColorFrame)
        self.first_gradient_lbl.setObjectName(u"first_gradient_lbl")
        sizePolicy.setHeightForWidth(self.first_gradient_lbl.sizePolicy().hasHeightForWidth())
        self.first_gradient_lbl.setSizePolicy(sizePolicy)
        self.first_gradient_lbl.setMinimumSize(QSize(71, 24))
        self.first_gradient_lbl.setFont(font3)
        self.first_gradient_lbl.setTextFormat(Qt.MarkdownText)
        self.first_gradient_lbl.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.horizontalLayout_2.addWidget(self.first_gradient_lbl)


        self.verticalLayout.addWidget(self.FirsrColorFrame, 0, Qt.AlignHCenter)

        self.SecondColorFrame = QFrame(self.ColorOptionsFrame)
        self.SecondColorFrame.setObjectName(u"SecondColorFrame")
        sizePolicy.setHeightForWidth(self.SecondColorFrame.sizePolicy().hasHeightForWidth())
        self.SecondColorFrame.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.SecondColorFrame)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 10)
        self.select_second_color_btn = QPushButton(self.SecondColorFrame)
        self.select_second_color_btn.setObjectName(u"select_second_color_btn")
        sizePolicy5.setHeightForWidth(self.select_second_color_btn.sizePolicy().hasHeightForWidth())
        self.select_second_color_btn.setSizePolicy(sizePolicy5)
        self.select_second_color_btn.setMinimumSize(QSize(107, 30))
        self.select_second_color_btn.setFont(font4)
        self.select_second_color_btn.setStyleSheet(u"QPushButton{\n"
"background-color:#00ff00;\n"
"color:#e6e6e6;\n"
"}")
        self.select_second_color_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.select_second_color_btn)

        self.second_gradient_lbl = QLabel(self.SecondColorFrame)
        self.second_gradient_lbl.setObjectName(u"second_gradient_lbl")
        sizePolicy.setHeightForWidth(self.second_gradient_lbl.sizePolicy().hasHeightForWidth())
        self.second_gradient_lbl.setSizePolicy(sizePolicy)
        self.second_gradient_lbl.setMinimumSize(QSize(71, 24))
        self.second_gradient_lbl.setFont(font3)
        self.second_gradient_lbl.setTextFormat(Qt.MarkdownText)
        self.second_gradient_lbl.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.horizontalLayout.addWidget(self.second_gradient_lbl)


        self.verticalLayout.addWidget(self.SecondColorFrame, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.ColorOptionsFrame, 1, 0, 1, 1)

        self.gradientTypeFrame = QFrame(GradientWindow)
        self.gradientTypeFrame.setObjectName(u"gradientTypeFrame")
        self.gradientType_Frame = QVBoxLayout(self.gradientTypeFrame)
        self.gradientType_Frame.setSpacing(0)
        self.gradientType_Frame.setObjectName(u"gradientType_Frame")
        self.gradientType_Frame.setContentsMargins(0, 0, 0, 0)
        self.StraightDiagonalFrame = QFrame(self.gradientTypeFrame)
        self.StraightDiagonalFrame.setObjectName(u"StraightDiagonalFrame")
        sizePolicy4.setHeightForWidth(self.StraightDiagonalFrame.sizePolicy().hasHeightForWidth())
        self.StraightDiagonalFrame.setSizePolicy(sizePolicy4)
        self.horizontalLayout_18 = QHBoxLayout(self.StraightDiagonalFrame)
        self.horizontalLayout_18.setSpacing(20)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.straight_diagonal_lbl = QLabel(self.StraightDiagonalFrame)
        self.straight_diagonal_lbl.setObjectName(u"straight_diagonal_lbl")
        sizePolicy6 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.straight_diagonal_lbl.sizePolicy().hasHeightForWidth())
        self.straight_diagonal_lbl.setSizePolicy(sizePolicy6)
        self.straight_diagonal_lbl.setMinimumSize(QSize(218, 0))
        self.straight_diagonal_lbl.setFont(font)
        self.straight_diagonal_lbl.setTextFormat(Qt.MarkdownText)

        self.horizontalLayout_18.addWidget(self.straight_diagonal_lbl)

        self.straight_diagonal_checkbox = QPushButton(self.StraightDiagonalFrame)
        self.gradientOrientationButtonGroup = QButtonGroup(GradientWindow)
        self.gradientOrientationButtonGroup.setObjectName(u"gradientOrientationButtonGroup")
        self.gradientOrientationButtonGroup.addButton(self.straight_diagonal_checkbox)
        self.straight_diagonal_checkbox.setObjectName(u"straight_diagonal_checkbox")
        self.straight_diagonal_checkbox.setMinimumSize(QSize(41, 41))
        self.straight_diagonal_checkbox.setMaximumSize(QSize(41, 41))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(9)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setKerning(True)
        self.straight_diagonal_checkbox.setFont(font5)
        self.straight_diagonal_checkbox.setStyleSheet(u"QPushButton {\n"
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
        self.straight_diagonal_checkbox.setIconSize(QSize(70, 70))
        self.straight_diagonal_checkbox.setCheckable(True)
        self.straight_diagonal_checkbox.setChecked(False)
        self.straight_diagonal_checkbox.setAutoRepeat(False)
        self.straight_diagonal_checkbox.setAutoExclusive(False)

        self.horizontalLayout_18.addWidget(self.straight_diagonal_checkbox)


        self.gradientType_Frame.addWidget(self.StraightDiagonalFrame)

        self.diagonal45Frame = QFrame(self.gradientTypeFrame)
        self.diagonal45Frame.setObjectName(u"diagonal45Frame")
        sizePolicy4.setHeightForWidth(self.diagonal45Frame.sizePolicy().hasHeightForWidth())
        self.diagonal45Frame.setSizePolicy(sizePolicy4)
        self.horizontalLayout_20 = QHBoxLayout(self.diagonal45Frame)
        self.horizontalLayout_20.setSpacing(20)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.diagonal45_lbl = QLabel(self.diagonal45Frame)
        self.diagonal45_lbl.setObjectName(u"diagonal45_lbl")
        sizePolicy6.setHeightForWidth(self.diagonal45_lbl.sizePolicy().hasHeightForWidth())
        self.diagonal45_lbl.setSizePolicy(sizePolicy6)
        self.diagonal45_lbl.setFont(font)
        self.diagonal45_lbl.setTextFormat(Qt.MarkdownText)

        self.horizontalLayout_20.addWidget(self.diagonal45_lbl)

        self.diagonal45_checkbox = QPushButton(self.diagonal45Frame)
        self.gradientOrientationButtonGroup.addButton(self.diagonal45_checkbox)
        self.diagonal45_checkbox.setObjectName(u"diagonal45_checkbox")
        self.diagonal45_checkbox.setMinimumSize(QSize(41, 41))
        self.diagonal45_checkbox.setMaximumSize(QSize(41, 41))
        self.diagonal45_checkbox.setFont(font5)
        self.diagonal45_checkbox.setStyleSheet(u"QPushButton {\n"
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
        self.diagonal45_checkbox.setIconSize(QSize(70, 70))
        self.diagonal45_checkbox.setCheckable(True)
        self.diagonal45_checkbox.setChecked(True)
        self.diagonal45_checkbox.setAutoRepeat(False)
        self.diagonal45_checkbox.setAutoExclusive(False)

        self.horizontalLayout_20.addWidget(self.diagonal45_checkbox)


        self.gradientType_Frame.addWidget(self.diagonal45Frame)


        self.gridLayout.addWidget(self.gradientTypeFrame, 0, 0, 1, 1, Qt.AlignHCenter)


        self.retranslateUi(GradientWindow)

        QMetaObject.connectSlotsByName(GradientWindow)
    # setupUi

    def retranslateUi(self, GradientWindow):
        GradientWindow.setWindowTitle(QCoreApplication.translate("GradientWindow", u"Gradient Options", None))
#if QT_CONFIG(tooltip)
        self.gradient_transition_lbl.setToolTip(QCoreApplication.translate("GradientWindow", u"<html><head/><body><p>Exported image size multiplier</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.gradient_transition_lbl.setText(QCoreApplication.translate("GradientWindow", u"## Transition point", None))
#if QT_CONFIG(tooltip)
        self.gradient_push_slider.setToolTip(QCoreApplication.translate("GradientWindow", u"<html><head/><body><p>Color transition point</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.gradient_push_indicator_lbl.setToolTip(QCoreApplication.translate("GradientWindow", u"<html><head/><body><p>Exported image size will be multiplied by this number</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.gradient_push_indicator_lbl.setText(QCoreApplication.translate("GradientWindow", u"15", None))
        self.transparency_section_lbl.setText(QCoreApplication.translate("GradientWindow", u"## Transparency", None))
        self.transparency_indicator_lbl.setText(QCoreApplication.translate("GradientWindow", u"255", None))
        self.select_first_color_btn.setText(QCoreApplication.translate("GradientWindow", u"1st color", None))
        self.first_gradient_lbl.setText(QCoreApplication.translate("GradientWindow", u"#aa0000", None))
        self.select_second_color_btn.setText(QCoreApplication.translate("GradientWindow", u"2nd color", None))
        self.second_gradient_lbl.setText(QCoreApplication.translate("GradientWindow", u"#00ff00", None))
#if QT_CONFIG(tooltip)
        self.straight_diagonal_lbl.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.straight_diagonal_lbl.setText(QCoreApplication.translate("GradientWindow", u"# Straight diagonal\n"
" - From left to right", None))
#if QT_CONFIG(tooltip)
        self.straight_diagonal_checkbox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.straight_diagonal_checkbox.setText("")
#if QT_CONFIG(tooltip)
        self.diagonal45_lbl.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.diagonal45_lbl.setText(QCoreApplication.translate("GradientWindow", u"# Diagonal 45\n"
" - 45-degree angle (left to right)", None))
#if QT_CONFIG(tooltip)
        self.diagonal45_checkbox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.diagonal45_checkbox.setText("")
    # retranslateUi

