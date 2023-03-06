# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowtyUdBN.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(566, 459)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.505, y1:0, x2:0.510211, y2:1, stop:0 rgba(89, 89, 89, 255), stop:0.978947 rgba(0, 0, 0, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont()
        font.setFamily(u"MV Boli")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"border-radius: 5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")

        self.verticalLayout.addWidget(self.pushButton)

        self.gl_tasks2 = QGridLayout()
        self.gl_tasks2.setObjectName(u"gl_tasks2")

        self.verticalLayout.addLayout(self.gl_tasks2)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(34)
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setContentsMargins(37, 0, 0, 0)

        self.verticalLayout.addLayout(self.gridLayout_6)

        self.gl_tasks = QGridLayout()
        self.gl_tasks.setObjectName(u"gl_tasks")
        self.gl_tasks.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout.setHorizontalSpacing(43)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(18, 0, 14, 0)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamily(u"MV Boli")
        font1.setPointSize(13)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 0, 127);\n"
"background-color: qlineargradient(spread:pad, x1:0.52, y1:1, x2:0.531421, y2:0.318, stop:0 rgba(232, 232, 232, 0), stop:1 rgba(255, 255, 255, 0));")

        self.gridLayout.addWidget(self.label_3, 10, 1, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(255, 0, 127);\n"
"background-color: qlineargradient(spread:pad, x1:0.52, y1:1, x2:0.531421, y2:0.318, stop:0 rgba(232, 232, 232, 0), stop:1 rgba(255, 255, 255, 0));")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.date = QLineEdit(self.centralwidget)
        self.date.setObjectName(u"date")
        self.date.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.date, 9, 1, 1, 1)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.comboBox, 13, 1, 1, 1)

        self.time = QLineEdit(self.centralwidget)
        self.time.setObjectName(u"time")
        self.time.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.time, 11, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 0, 127);\n"
"background-color: qlineargradient(spread:pad, x1:0.52, y1:1, x2:0.531421, y2:0.318, stop:0 rgba(232, 232, 232, 0), stop:1 rgba(255, 255, 255, 0));")

        self.gridLayout.addWidget(self.label_2, 8, 1, 1, 1)

        self.tb_new_task_title = QLineEdit(self.centralwidget)
        self.tb_new_task_title.setObjectName(u"tb_new_task_title")
        self.tb_new_task_title.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tb_new_task_title.sizePolicy().hasHeightForWidth())
        self.tb_new_task_title.setSizePolicy(sizePolicy1)
        self.tb_new_task_title.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.tb_new_task_title, 2, 0, 1, 1)

        self.btn_new_task = QPushButton(self.centralwidget)
        self.btn_new_task.setObjectName(u"btn_new_task")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_new_task.sizePolicy().hasHeightForWidth())
        self.btn_new_task.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(27)
        font2.setBold(True)
        self.btn_new_task.setFont(font2)
        self.btn_new_task.setLayoutDirection(Qt.LeftToRight)
        self.btn_new_task.setStyleSheet(u"border-radius: 20px;\n"
"background-color: qlineargradient(spread:pad, x1:0.515684, y1:0.398, x2:0.510211, y2:1, stop:0.0368421 rgba(181, 0, 70, 255), stop:1 rgba(66, 0, 25, 255));\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.gridLayout.addWidget(self.btn_new_task, 0, 1, 4, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamily(u"MV Boli")
        font3.setPointSize(12)
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"color: rgb(255, 0, 127);\n"
"background-color: qlineargradient(spread:pad, x1:0.52, y1:1, x2:0.531421, y2:0.318, stop:0 rgba(232, 232, 232, 0), stop:1 rgba(255, 255, 255, 0));")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"color: rgb(255, 0, 127);\n"
"background-color: qlineargradient(spread:pad, x1:0.52, y1:1, x2:0.531421, y2:0.318, stop:0 rgba(232, 232, 232, 0), stop:1 rgba(255, 255, 255, 0));")

        self.gridLayout.addWidget(self.label_10, 12, 1, 1, 1)

        self.tb_new_task_description = QTextEdit(self.centralwidget)
        self.tb_new_task_description.setObjectName(u"tb_new_task_description")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tb_new_task_description.sizePolicy().hasHeightForWidth())
        self.tb_new_task_description.setSizePolicy(sizePolicy3)
        self.tb_new_task_description.setStyleSheet(u"background-color: rgb(250, 250, 250);\n"
"border-radius: 8px;")

        self.gridLayout.addWidget(self.tb_new_task_description, 8, 0, 8, 1)

        self.btn_sort = QPushButton(self.centralwidget)
        self.btn_sort.setObjectName(u"btn_sort")
        sizePolicy2.setHeightForWidth(self.btn_sort.sizePolicy().hasHeightForWidth())
        self.btn_sort.setSizePolicy(sizePolicy2)
        font4 = QFont()
        font4.setFamily(u"MV Boli")
        font4.setPointSize(13)
        font4.setBold(True)
        self.btn_sort.setFont(font4)
        self.btn_sort.setLayoutDirection(Qt.LeftToRight)
        self.btn_sort.setStyleSheet(u"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.247, y1:0.943273, x2:0.968, y2:0.023, stop:0 rgba(12, 12, 155, 255), stop:1 rgba(117, 183, 255, 255));\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.gridLayout.addWidget(self.btn_sort, 14, 1, 3, 1)


        self.gl_tasks.addLayout(self.gridLayout, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gl_tasks)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 566, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"TODO LIST ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Time :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Task title :", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
#if QT_CONFIG(tooltip)
        self.btn_new_task.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>press to add new task</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_new_task.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Description :", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Priority :", None))
#if QT_CONFIG(tooltip)
        self.btn_sort.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>click to sort based on priority</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_sort.setText(QCoreApplication.translate("MainWindow", u"SORT Tasks ", None))
    # retranslateUi

 
