#This project focus on disabling the button
import sys
from PyQt6.QtWidgets import QApplication,QPushButton,QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("button Disabled on click")
        self.button=QPushButton("Press Me")
        self.button.clicked.connect(self.on_click)
        self.setCentralWidget(self.button)

    def on_click(self):
        self.button.setText("I got updated with new values")
        self.button.setEnabled(False)
        self.setWindowTitle("My new window")


app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec()