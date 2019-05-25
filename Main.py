# 標準モジュール参照
import sys
import threading
import time

# PyQt関連モジュール参照
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# UIクラス参照
from UIController import UIController as UI

# Twitter機能制御クラス参照
from TWController import TWController as TW

# キーコンボ監視クラス参照
# from TriggerChecker import TriggerChecker as TC

class Test():
    # コンストラクタメソッド
    def __init__(self):
        self.ui = UI()
        # self.T_keywatchdog = threading.Thread(target = TC)

    def run(self):
        self.ui.show()
        self.ui.open_interface()
        print("hello")
        # self.T_keywatchdog.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainsys = Test()
    mainsys.run()
    # mainsys.T_keywatchdog.join()
    sys.exit(app.exec())