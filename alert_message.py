#WAP to show alert box on the button click

import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QWidget,QPushButton,QMessageBox
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        button=QPushButton("Click Me..!!")
        button.clicked.connect(self.on_click)
        self.setCentralWidget(button)


    def on_click(self):
        alert1=QMessageBox()
        alert1.setText("You are seeing the Qmessage Box component")
        alert1.exec()


app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec()