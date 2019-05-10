# -*- coding: utf-8 -*-
# 標準モジュール参照
import sys
import re

# UIクラス指定
from mainwindow import Ui_MainWindow
from widget import Ui_Form as widget

# Twitterエンジンモジュール指定
from TWController import TWController

# PyQt5モジュール参照
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# UI制御クラス宣言
class UIController(QWidget):
# コンストラクタメソッド
    def __init__(self, parent = None):
        super(UIController, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.tw = TWController()
        self.tw.authorize_user()

        self.ui = widget()
        self.ui.setupUi(self)
        self.connect_signal_slot()
        self.updated_text()

        self.ui.UserInformation.setText(self.tw.UserName + " (@" + self.tw.UserID + ")")
        # self.ui.profileimg = QImage(self.tw.get_user_image())
        # self.ui.label.setPixmap(QPixmap.fromImage(self.ui.profileimg))

        print("UIController : CONSTRUCTOR PROCESS COMPLETE")

    def __del__(self):
        print("UIController : DESTRUCTOR PROCESS COMPLETE")

    def connect_signal_slot(self):
        self.ui.PostButton.clicked.connect(self.pushed_postButton)
        self.ui.PostEditor.textChanged.connect(self.updated_text)

    def updated_text(self):
        self.post = self.post_raw = self.ui.PostEditor.toPlainText()

        self.post_raw = re.sub(' ', "", self.post_raw)
        self.post_raw = re.sub('\n', "", self.post_raw)
        self.post_raw = re.sub('　', "", self.post_raw)

        print("UPDATE : " + self.post_raw)
        self.ui.TextLengthIndicator.setText(str(self.tw.check_textlength(self.post_raw)) + " / " + str(self.tw.max_length) + "[Byte]")
        if self.tw.can_post():
            self.ui.PostButton.setEnabled(True)
        else:
            self.ui.PostButton.setEnabled(False)

    def refresh_PostEditor(self):
        self.ui.PostEditor.setText("")

    def pushed_postButton(self):
            self.tw.post_tweet(self.post)
            self.refresh_PostEditor()

# 単体テスト時処理
if __name__ == '__main__':
    app = QApplication(sys.argv)
    tmp = UIController()
    tmp.show()
    sys.exit(app.exec())
