#we will implement the signal storing
import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked=True

        self.setWindowTitle("MyApplication")
        self.button=QPushButton("PressMe!!")
        self.button.setCheckable(True)
        #button.clicked.connect(self.on_click)
        self.button.released.connect(self.on_release)
        self.setCentralWidget(self.button)

    def on_click(self,checked):
        self.button_is_checked=checked
        print(self.button_is_checked)

    def on_release(self):
        self.button_is_checked=self.button.isChecked()
        print(self.button_is_checked)


app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec()