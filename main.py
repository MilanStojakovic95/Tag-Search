import sys
from pathlib import Path

# Add 'src' folder to sys.path so Python can find your modules
sys.path.append(str(Path(__file__).parent / "src"))

from ui.main_window import MainWindow
from PyQt6.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
