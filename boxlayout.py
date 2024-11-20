from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QMainWindow,QLabel,QVBoxLayout
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BoxLayout")
        self.label=QLabel("Welcome")
        self.button1=QPushButton("Top Button")
        self.button2=QPushButton("Bottom Button")

        layoyt=QVBoxLayout()
        layoyt.addWidget(self.button1)
        layoyt.addWidget(self.button2)
        self.setLayout(layoyt)

        container = QWidget()
        container.setLayout(layoyt)

        self.setCentralWidget(container)
app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec()