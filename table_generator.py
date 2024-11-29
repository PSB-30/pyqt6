import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton


class MultiplicationTableApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Multiplication Table Generator")
        self.setGeometry(100, 100, 300, 200)

        # Create widgets
        self.number_input = QLineEdit(self)
        self.number_input.setPlaceholderText("Enter a number")

        self.generate_button = QPushButton("Generate Table", self)
        self.table_label = QLabel(self)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.number_input)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.table_label)

        self.setLayout(layout)

        # Connect button to action
        self.generate_button.clicked.connect(self.generate_table)

    def generate_table(self):
        try:
            # Get the number from input
            num = int(self.number_input.text())

            # Generate the multiplication table
            table = ""
            for i in range(1, 11):
                table += f"{num} x {i} = {num * i}\n"

            # Set the generated table to QLabel
            self.table_label.setText(table)

        except ValueError:
            # If the input is not a valid number, show an error message
            self.table_label.setText("Please enter a valid number.")


# Main code to run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MultiplicationTableApp()
    window.show()
    sys.exit(app.exec())
