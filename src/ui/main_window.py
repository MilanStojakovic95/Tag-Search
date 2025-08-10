from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog, QTextEdit
from utils.file_utils import scan_videos
from core.database import insert_video

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Library Manager")
        self.resize(900, 600)

        layout = QVBoxLayout()

        self.scan_button = QPushButton("Scan Folder")
        self.scan_button.clicked.connect(self.open_folder_dialog)
        layout.addWidget(self.scan_button)

        self.result_box = QTextEdit()
        self.result_box.setReadOnly(True)
        layout.addWidget(self.result_box)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_folder_dialog(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder to Scan")
        if folder:
            videos = scan_videos(folder)
            self.result_box.clear()
            if videos:
                self.result_box.append(f"Found {len(videos)} video(s):\n")
                for v in videos:
                    insert_video(v)  # store in DB
                    self.result_box.append(v)
            else:
                self.result_box.append("No videos found in the selected folder.")
