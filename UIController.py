# -*- coding: utf-8 -*-

# UIクラス指定
from UserInterfaces.mainwindow import Ui_MainWindow

# Twitterエンジンモジュール指定
import TWController as TWengine

# PyQt5モジュール参照
from PyQt5.QtWidgets import *

# UI制御クラス宣言
class UIController(QMainWindow):
# コンストラクタメソッド
    def __init__(self, parent = None):
        super(Test, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def connect_signal-slot(self):
        self.ui.pushButton.clicked.connect(self.pushed_postButton)

    def pushed_postButton(self):
        pass
