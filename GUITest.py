#!/usr/bin/env python
# coding: utf-8

import sys
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
	w_width = 400
	w_height = 150

	def __init__(self, parent = None):
		super(MainWindow, self).__init__(parent)

		self.setGeometry(300, 50, self.w_width, self.w_height)
		self.setWindowTitle('Mojatter')

if __name__ == '__main__':
	app = QApplication(sys.argv)
	main_window = MainWindow()
	main_window.show()
	sys.exit(app.exec_())
