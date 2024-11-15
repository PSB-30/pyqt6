
#Creating a window Using the QWidget
from PyQt6.QtWidgets import QApplication,QWidget,QLabel
import sys
app=QApplication(sys.argv)


window=QWidget()
window.show()
window.setWindowTitle("MyfirstPythonApp")
window.setGeometry(100,100,200,200)



sys.exit(app.exec())
