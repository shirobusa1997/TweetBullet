# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 140)
        MainWindow.setMinimumSize(QtCore.QSize(400, 140))
        MainWindow.setMaximumSize(QtCore.QSize(400, 140))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.PostEditor = QtWidgets.QTextEdit(self.centralWidget)
        self.PostEditor.setGeometry(QtCore.QRect(10, 20, 381, 91))
        self.PostEditor.setObjectName("PostEditor")
        self.PostButton = QtWidgets.QPushButton(self.centralWidget)
        self.PostButton.setGeometry(QtCore.QRect(330, 110, 61, 23))
        self.PostButton.setObjectName("PostButton")
        self.TextLengthIndicator = QtWidgets.QLabel(self.centralWidget)
        self.TextLengthIndicator.setGeometry(QtCore.QRect(10, 110, 151, 20))
        font = QtGui.QFont()
        font.setFamily("游ゴシック")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.TextLengthIndicator.setFont(font)
        self.TextLengthIndicator.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TextLengthIndicator.setObjectName("TextLengthIndicator")
        self.UserInformation = QtWidgets.QLabel(self.centralWidget)
        self.UserInformation.setGeometry(QtCore.QRect(10, 0, 221, 20))
        font = QtGui.QFont()
        font.setFamily("游ゴシック")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.UserInformation.setFont(font)
        self.UserInformation.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.UserInformation.setObjectName("UserInformation")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(300, 20, 90, 90))
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.PostEditor.textChanged.connect(self.TextLengthIndicator.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "[Dev] Mojatter"))
        self.PostButton.setText(_translate("MainWindow", "Post"))
        self.TextLengthIndicator.setText(_translate("MainWindow", "[Remaining TextLength]"))
        self.UserInformation.setText(_translate("MainWindow", "[UserName] (@[UserID])"))


