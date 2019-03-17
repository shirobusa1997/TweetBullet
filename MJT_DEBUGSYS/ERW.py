# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ExceptionRemindWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 119)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 251, 16))
        self.label.setObjectName("label")
        self.ExceptionInformation = QtWidgets.QTextEdit(Form)
        self.ExceptionInformation.setGeometry(QtCore.QRect(10, 30, 381, 81))
        self.ExceptionInformation.setObjectName("ExceptionInformation")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "処理中に例外が発生しました。"))

