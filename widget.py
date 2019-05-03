# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 150)
        Form.setMinimumSize(QtCore.QSize(400, 150))
        Form.setMaximumSize(QtCore.QSize(400, 150))
        self.UserInformation = QtWidgets.QLabel(Form)
        self.UserInformation.setGeometry(QtCore.QRect(10, 10, 221, 20))
        font = QtGui.QFont()
        font.setFamily("游ゴシック")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.UserInformation.setFont(font)
        self.UserInformation.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.UserInformation.setObjectName("UserInformation")
        self.TextLengthIndicator = QtWidgets.QLabel(Form)
        self.TextLengthIndicator.setGeometry(QtCore.QRect(10, 120, 151, 20))
        font = QtGui.QFont()
        font.setFamily("游ゴシック")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.TextLengthIndicator.setFont(font)
        self.TextLengthIndicator.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TextLengthIndicator.setObjectName("TextLengthIndicator")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(300, 30, 90, 90))
        self.label.setText("")
        self.label.setObjectName("label")
        self.PostEditor = QtWidgets.QTextEdit(Form)
        self.PostEditor.setGeometry(QtCore.QRect(10, 30, 381, 91))
        self.PostEditor.setObjectName("PostEditor")
        self.PostButton = QtWidgets.QPushButton(Form)
        self.PostButton.setGeometry(QtCore.QRect(330, 120, 61, 23))
        self.PostButton.setObjectName("PostButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.UserInformation.setText(_translate("Form", "[UserName] (@[UserID])"))
        self.TextLengthIndicator.setText(_translate("Form", "[Remaining TextLength]"))
        self.PostButton.setText(_translate("Form", "Post"))

