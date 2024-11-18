import sys
from NeQt.QtWidgets import QApplication,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QWidget
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My New App..!!")
        self.input=QLineEdit()
        self.label=QLabel()
        self.input.textChanged.connect(self.label.setText)

        layout=QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input)

        container=QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec()