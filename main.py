import sys
import os

# Ensure src is on the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from ui.main_window import MainWindow
from core.database import init_db
from PyQt6.QtWidgets import QApplication

def main():
    init_db()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
