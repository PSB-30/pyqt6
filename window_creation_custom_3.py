#Creeating window with custome components
import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QPushButton
from PyQt6.QtCore import QSize
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Custom window")
        button=QPushButton("Press Me!!")

        #to align it to center
        self.setCentralWidget(button)
        self.setFixedSize(400,300)


app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec()