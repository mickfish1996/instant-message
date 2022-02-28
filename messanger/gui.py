from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow 
from PyQt5.QtCore import QSize, Qt
import sys

class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Messanger")
        self.setFixedSize(QSize(600, 400))
app = QApplication(sys.argv)
        
window = Gui()
window.show()
        
app.exec()
        
        
        
