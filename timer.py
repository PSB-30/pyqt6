import sys
import os
from PyQt6.QtCore import QTimer, QTime
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class ShutdownApp(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the timer and time variable
        self.timer = QTimer(self)
        self.time_left = QTime(0, 1, 0)  # Set to 10 minutes for example

        # Setup the UI
        self.setWindowTitle("Shutdown Timer")
        self.setGeometry(300, 300, 300, 200)
        self.layout = QVBoxLayout()

        # Label to display countdown
        self.timer_label = QLabel(self)
        self.update_timer_label()

        # Start button to start the countdown
        self.start_button = QPushButton("Start Countdown", self)
        self.start_button.clicked.connect(self.start_timer)

        # Shutdown button (optional)
        self.shutdown_button = QPushButton("Shutdown Now", self)
        self.shutdown_button.clicked.connect(self.shutdown_system)

        # Add widgets to layout
        self.layout.addWidget(self.timer_label)
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.shutdown_button)

        # Set the layout for the widget
        self.setLayout(self.layout)

        # Connect the timer's timeout signal to the handler function
        self.timer.timeout.connect(self.update_time)

    def start_timer(self):
        """Start the countdown timer."""
        self.timer.start(1000)  # Timer will tick every second
        self.start_button.setEnabled(False)  # Disable the start button while the timer is running

    def update_time(self):
        """Update the countdown time and check if it has reached zero."""
        self.time_left = self.time_left.addSecs(-1)  # Subtract 1 second from the timer
        self.update_timer_label()

        # When time reaches zero, trigger shutdown
        if self.time_left == QTime(0, 0, 0):
            self.timer.stop()
            self.shutdown_system()

    def update_timer_label(self):
        """Update the label with the remaining time."""
        self.timer_label.setText(f"Time Left: {self.time_left.toString('mm:ss')}")

    def shutdown_system(self):
        """Shutdown the system after timer ends."""
        if sys.platform == "win32":
            os.system("shutdown /s /f /t 0")  # For Windows
        elif sys.platform == "darwin" or sys.platform == "linux":
            os.system("sudo shutdown -h now")  # For macOS and Linux (may require sudo)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShutdownApp()
    window.show()
    sys.exit(app.exec())
