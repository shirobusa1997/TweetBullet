# -*- coding: utf-8 -*-
# 標準モジュール参照
import sys
import re
import threading

# UIクラス指定
from widget import Ui_Form as widget

# Twitterエンジンモジュール指定
from TWController import TWController

# PyQt5モジュール参照
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# キーコンボ監視クラス参照
from pyhooked import Hook, KeyboardEvent, MouseEvent

# UI制御クラス宣言
class UIController(QWidget):
    widgetsize_w = 400
    widgetsize_h = 150
    animduration = 150
    active = False

# コンストラクタメソッド
    def __init__(self, parent = None):
        super(UIController, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.tw = TWController()
        self.tw.authorize_user()

        self.ui = widget()
        self.ui.setupUi(self)
        self.desktop = QDesktopWidget()
        self.framesize = self.frameSize()
        self.connect_signal_slot()
        self.updated_text()

        self.ui.UserInformation.setText(self.tw.UserName + " (@" + self.tw.UserID + ")")
        # self.ui.profileimg = QImage(self.tw.get_user_image())
        # self.ui.label.setPixmap(QPixmap.fromImage(self.ui.profileimg))

        self.animation = QPropertyAnimation(self, b'pos', self)
        self.move(QPoint(self.desktop.width() + 10, self.desktop.height() - 900))
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        self.active = False
        self.change_interface_state()

        print("UIController : CONSTRUCTOR PROCESS COMPLETE")

        hk = Hook()
        hk.handler = self.handle_events
        self.key_thread = threading.Thread(target=hk.hook)
        self.key_thread.setDaemon(True)
        self.key_thread.start()

    def __del__(self):
        print("UIController : DESTRUCTOR PROCESS COMPLETE")

    def handle_events(self, args):
        if isinstance(args, KeyboardEvent):
            if args.current_key == 'O' and args.event_type == 'key up' and 'Rcontrol' in args.pressed_key:
                print("Thread : Trigger KeyCombo was pressed")
                self.change_interface_state()

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

    # def keyPressEvent(self, event):
    #     modifires = QApplication.keyboardModifiers()
    #     if modifires == Qt.ControlModifier:
    #         if event.key() == Qt.Key_O:
    #             self.change_interface_state()

    def refresh_PostEditor(self):
        self.ui.PostEditor.setText("")

    def pushed_postButton(self):
        self.tw.post_tweet(self.post)
        self.refresh_PostEditor()

    def change_interface_state(self):
        if self.active:
            self.close_interface()
        else:
            self.open_interface()

    def open_interface(self):
        self.setFocus(True)
        self.active = True
        self.animation.setDuration(self.animduration)
        self.animation.setStartValue(QPoint(self.desktop.width() + 10, self.desktop.height() - 900))
        self.animation.setEndValue(QPoint(self.desktop.width() - 450, self.desktop.height() - 900))
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.animation.start()

    def close_interface(self):
        self.setFocus(False)
        self.active = False
        self.animation.setDuration(self.animduration)
        self.animation.setStartValue(QPoint(self.desktop.width() - 450, self.desktop.height() - 900))
        self.animation.setEndValue(QPoint(self.desktop.width() + 10, self.desktop.height() - 900))
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.animation.start()

# 単体テスト時処理
if __name__ == '__main__':
    app = QApplication(sys.argv)
    tmp = UIController()
    tmp.show()
    sys.exit(app.exec())
