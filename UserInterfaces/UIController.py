# -*- coding: utf-8 -*-

# UIクラス指定
from UserInterfaces.mainwindow import Ui_MainWindow

# PyQt5モジュール参照
from PyQt5.QtWidgets import *

# UI制御クラス宣言
class UIController(QMainWindow):
# コンストラクタメソッド
    def __init__(self, parent = None):
        super(Test, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)