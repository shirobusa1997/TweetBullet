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

        print("Initialize section : ALL GREEN")

    def connect_signal_slot(self):
        self.ui.PostButton.clicked.connect(self.pushed_postButton)
        self.ui.PostEditor.textChanged.connect(self.updated_text)

    def updated_text(self):
        self.post = self.ui.PostEditor.toPlainText()
        print("UPDATE : " + self.post)
        self.ui.TextLengthIndicator.setText(str(self.tw.textlength) + " / " + self.tw.max_length)

    def pushed_postButton(self):
        if self.tw.can_post:
            self.tw.post_tweet(self.post)
        else:
            print("ERROR : ツイート内容を最大長以内に修正してください。(Your text is too long!!)")

# 単体テスト時処理
if __name__ == '__main__':
    app = QApplication(sys.argv)
    tmp = UIController()
    tmp.show()
    sys.exit(app.exec())