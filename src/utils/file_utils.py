import os

# Scans videos from path

VIDEO_EXTENSIONS = {'.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv', '.webm'}

def scan_videos(folder_path):
    video_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in VIDEO_EXTENSIONS:
                full_path = os.path.join(root, file)
                video_files.append(full_path)
    return video_files
