# 標準モジュール参照
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# UIクラス参照
from UIController import UIController as UI

# Twitter機能制御クラス参照
from TWController import TWController as TW

# キーコンボ監視クラス参照
# import TriggerChecker

class Test():
    # コンストラクタメソッド
    def __init__(self):
        self.ui = UI()

    def activate(self):
        self.ui.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainsys = Test()
    mainsys.activate()
    sys.exit(app.exec())