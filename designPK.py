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
import files_rcPK

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(258, 101)
        icon = QIcon()
        icon.addFile(u":/icons/imgonline-com-ua-Transparent-backgr-N6LTI4dQx2q.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background-color: rgb(85, 0, 0);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PassKey Generator By LehaBezuglov", None))
        self.label.setText("")
        self.label.setStyleSheet("color: #00CC00")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
    # retranslateUi

