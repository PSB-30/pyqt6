#Using QLabel To print the image
from PyQt6.QtWidgets import QApplication,QLabel,QWidget,QVBoxLayout,QComboBox
import os
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout=QVBoxLayout()
        self.setLayout(layout)
        widget=QLabel("Combo box")
        my_items=QComboBox()
        my_items.addItems(['Maths','Physics','Chemistry'])
        # my_items.setEditable(True)
        my_items.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)

        layout.addWidget(widget)
        layout.addWidget(my_items)



app=QApplication([sys.argv])
window=MainWindow()
window.show()

app.exec()