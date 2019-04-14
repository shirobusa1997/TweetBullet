# -*- coding: utf-8 -*-
# 標準モジュール参照
import sys

# UIクラス指定
from mainwindow import Ui_MainWindow

# Twitterエンジンモジュール指定
from TWController import TWController

# PyQt5モジュール参照
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# UI制御クラス宣言
class UIController(QMainWindow):
# コンストラクタメソッド
    def __init__(self, parent = None):
        super(UIController, self).__init__(parent)

        self.tw = TWController()
        self.tw.authorize_user()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_signal_slot()
        self.updated_text()

        print("Initialize section : ALL GREEN")

    def connect_signal_slot(self):
        self.ui.PostButton.clicked.connect(self.pushed_postButton)
        self.ui.PostEditor.textChanged.connect(self.updated_text)

    def updated_text(self):
        self.post = self.ui.PostEditor.toPlainText()
        print("UPDATE : " + self.post)
        self.ui.TextLengthIndicator.setText(str(self.tw.check_textlength(self.post)) + " / " + str(self.tw.max_length))
        if self.tw.can_post():
            self.ui.PostButton.setEnabled(True)
        else:
            self.ui.PostButton.setEnabled(False)

    def pushed_postButton(self):
            self.tw.post_tweet(self.post)

# 単体テスト時処理
if __name__ == '__main__':
    app = QApplication(sys.argv)
    tmp = UIController()
    tmp.show()
    sys.exit(app.exec())