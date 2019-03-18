# 標準モジュール参照
import sys

# UIクラスデータ参照
from ERW import Ui_Form

# PyQt5モジュール参照
from PyQt5.QtWidgets import *

class MJT_DEBUGSYS_UIC():
    def __init__(self):
        pass

    def catch_exception(self, e):
        O_ERW = Ui_Form()
        O_ERW.ExceptionInformation.setPlainText(e)
        O_ERW.show()

        sys.exit()