import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

#initialize
root = QWidget()
start_button = QPushButton("START")
radio_button1 = QRadioButton()

#set parameters
root.resize(320, 400)
root.setWindowTitle("SetUP")

#show
root.show()
sys.exit(app.exec_())

"""
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        start_button = QPushButton("START")
        radio_button1 = QRadioButton()
        start_button.clicked.connect(self.click_method(self))

    def click_method(self):
        print("hallo")


app = QApplication(sys.argv)
main_win = MainWindow()
main_win.show()
sys.exit(app.exec_())
"""


