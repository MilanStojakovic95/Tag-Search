from PyQt6.QtWidgets import QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Library Manager")
        self.setGeometry(100, 100, 800, 600)
        self.label = QLabel("Welcome to Video Library Manager!", self)
        self.label.move(50, 50)