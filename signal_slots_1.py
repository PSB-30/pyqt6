#singal = Actions
#Slot=Function which will perform that action
#we are printing the state of the widgets by sending signal to it

import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QPushButton
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Signal & Slot Exmaple")
        button=QPushButton("Press Me..!!")
        self.setCentralWidget(button)
        button.setCheckable(True)
        button.clicked.connect(self.on_click)
        button.clicked.connect(self.on_toggele)


    def on_click(self):
        print("Clicked")

    def on_toggele(self,checked):
        print("Clicked ??",checked)


app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec()