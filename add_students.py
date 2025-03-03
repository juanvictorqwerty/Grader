import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon

import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grader")
        self.setGeometry(100, 100, 1920, 1080)
        self.setWindowIcon(QIcon('icon.png'))
        self.initUI()

    def initUI(self):
        self.GoBack = QPushButton('Back', self)
        self.GoBack.setGeometry(10, 10, 150, 100)
        self.GoBack.clicked.connect(self.go_home)
        print("Back")
        
    def go_home(self):
        subprocess.Popen([sys.executable, 'main.py'])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())