# 標準モジュール参照
import sys
import time

# PyQt関連モジュール参照
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# UIクラス参照
from UIController import UIController as UI

# Twitter機能制御クラス参照
from TWController import TWController as TW

class Core():
    # コンストラクタメソッド
    def __init__(self):
        self.ui = UI()
        # self.T_keywatchdog = threading.Thread(target = TC)

    def run(self):
        self.ui.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainsys = Core()
    mainsys.run()
    # mainsys.T_keywatchdog.join()
    sys.exit(app.exec())