# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'authorization.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pin_Dialog(object):
    def setupUi(self, Pin_Dialog):
        Pin_Dialog.setObjectName("Pin_Dialog")
        Pin_Dialog.resize(380, 100)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Pin_Dialog.sizePolicy().hasHeightForWidth())
        Pin_Dialog.setSizePolicy(sizePolicy)
        Pin_Dialog.setMinimumSize(QtCore.QSize(380, 100))
        Pin_Dialog.setMaximumSize(QtCore.QSize(380, 100))
        self.buttonBox = QtWidgets.QDialogButtonBox(Pin_Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(210, 70, 161, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setMaximumSize(QtCore.QSize(380, 50))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.textEdit = QtWidgets.QTextEdit(Pin_Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textEdit.setFont(font)
        self.textEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Pin_Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 361, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Pin_Dialog)
        # self.buttonBox.accepted.connect(Pin_Dialog.accept)
        # self.buttonBox.rejected.connect(Pin_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Pin_Dialog)

    def retranslateUi(self, Pin_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Pin_Dialog.setWindowTitle(_translate("Pin_Dialog", "Dialog"))
        self.label.setText(_translate("Pin_Dialog", "認証ページに表示されたPINコードを入力してください。"))


