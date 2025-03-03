import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grader")
        self.setGeometry(100, 100, 1920, 1080)
        self.setWindowIcon(QIcon('icon.png'))
        self.initUI()

    def initUI(self):
        self.AddStudentsButton = QPushButton('Open AddStudents', self)
        self.AddStudentsButton.setGeometry(100, 100, 150, 100)
        self.AddStudentsButton.setStyleSheet("background-color: red")
        self.AddStudentsButton.clicked.connect(self.open_add_students)

        self.ShowStudentsButton = QPushButton('Open ShowStudents', self)
        self.ShowStudentsButton.setGeometry(200, 200, 150, 100)
        self.ShowStudentsButton.setStyleSheet("background-color: blue")
        self.ShowStudentsButton.clicked.connect(self.open_show_students)

    def open_add_students(self):
        subprocess.Popen([sys.executable, 'add_students.py'])

    def open_show_students(self):
        subprocess.Popen([sys.executable, 'show_students.py'])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())