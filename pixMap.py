#Using QLabel To print the image
from PyQt6.QtWidgets import QApplication,QLabel,QWidget,QVBoxLayout
from PyQt6.QtGui import QPixmap
import os
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout=QVBoxLayout()
        self.setLayout(layout)
        widget=QLabel()
        widget.setPixmap(QPixmap("thumb16.jpg"))
        widget.setScaledContents(True)
        layout.addWidget(widget)


app=QApplication([sys.argv])
widnow=MainWindow()
widnow.show()
app.exec()