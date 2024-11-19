import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QWidget
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Click in me")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, k):
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, k):
        self.label.setText("mousePressEvent")

    def mouseReleaseEvent(self, k):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, k):
        self.label.setText("mouseDoubleClickEvent")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()