import sys
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QMenu,QToolBar
from PyQt6.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Awesome App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)


    def onMyToolBarButtonClick(self, s):
      print("click", s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()