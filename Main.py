# 標準モジュール参照
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# UIクラス参照
from UserInterfaces.UIController import *

# Twitter機能制御クラス参照
from TWController import *

class Test(Object):
    # コンストラクタメソッド
    def __init__(self, parent = None):
        super(Test, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	main_window = Test()
	main_window.show()
	sys.exit(app.exec_())