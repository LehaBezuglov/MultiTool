# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(320, 127)
        icon = QIcon()
        icon.addFile(u":/icons/icons/global-_1_.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background-color: rgb(28,84,45);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel {\n"
"	color: rgb(170, 255, 255);\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(15)
        self.pushButton.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/calculator.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/key-chain.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)

        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MultiTool by LehaBezuglov", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0438\u0440\u0438\u0442\u0435 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440 \u043f\u0430\u0440\u043e\u043b\u0435\u0439", None))
    # retranslateUi

