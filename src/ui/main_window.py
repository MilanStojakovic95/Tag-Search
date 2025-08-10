from PyQt6.QtWidgets import (
    QMainWindow, QVBoxLayout, QWidget,
    QPushButton, QFileDialog, QTableWidget, QTableWidgetItem, QHeaderView
)
from PyQt6.QtGui import QIcon, QPixmap
from utils.file_utils import scan_videos, generate_thumbnail
from core.database import insert_video, get_all_videos
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Library Manager")
        self.resize(1000, 600)

        layout = QVBoxLayout()

        # Scan button
        self.scan_button = QPushButton("Scan Folder")
        self.scan_button.clicked.connect(self.open_folder_dialog)
        layout.addWidget(self.scan_button)

        # Table for videos (now with 4 columns: Thumbnail, Name, Path, Extension)
        self.video_table = QTableWidget()
        self.video_table.setColumnCount(4)
        self.video_table.setHorizontalHeaderLabels(["Thumbnail", "Name", "Path", "Extension"])
        self.video_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.video_table.setIconSize(QPixmap(120, 80).size())
        self.video_table.setSortingEnabled(True)
        layout.addWidget(self.video_table)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Load existing DB videos at startup
        self.load_videos()

    def open_folder_dialog(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder to Scan")
        if folder:
            videos = scan_videos(folder)
            for v in videos:
                insert_video(v)
            self.load_videos()

    def load_videos(self):
        self.video_table.setRowCount(0)
        videos = get_all_videos()
        for row_num, (name, path, ext) in enumerate(videos):
            self.video_table.insertRow(row_num)

            # Thumbnail
            thumb_path = generate_thumbnail(path)
            if thumb_path and os.path.exists(thumb_path):
                icon = QIcon(thumb_path)
            else:
                icon = QIcon()  # Empty if no thumbnail
            thumb_item = QTableWidgetItem()
            thumb_item.setIcon(icon)
            self.video_table.setItem(row_num, 0, thumb_item)

            # Name
            self.video_table.setItem(row_num, 1, QTableWidgetItem(name))
            # Path
            self.video_table.setItem(row_num, 2, QTableWidgetItem(path))
            # Extension
            self.video_table.setItem(row_num, 3, QTableWidgetItem(ext))
