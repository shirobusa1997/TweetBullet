import sys
from PyQt5.QtWidgets import *

def main():
	app = QApplication(sys.argv)
	widget = QWidget()
	widget.resize(250, 150)
	widget.setWindowTitle('sample')
	widget.show()
	sys.exit(app.exec_())

if __name == '__main__':
	main()
