import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

class HelloWorldApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt6 Hello World")
        self.setGeometry(100, 100, 300, 200)

        # Central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # QLabel
        self.label = QLabel("Click the button to see a message!")
        self.layout.addWidget(self.label)

        # QPushButton
        self.button = QPushButton("Click Me")
        self.button.clicked.connect(self.on_button_click)  # Connect the button click to a method
        self.layout.addWidget(self.button)

    def on_button_click(self):
        self.label.setText("Hello, World!")  # Update the label text

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HelloWorldApp()
    window.show()
    sys.exit(app.exec())
