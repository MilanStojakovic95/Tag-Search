import os
import cv2
from PIL import Image, ImageDraw, ImageFont

VIDEO_EXTENSIONS = (".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv")

def scan_videos(folder):
    videos = []
    for root, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(VIDEO_EXTENSIONS):
                videos.append(os.path.join(root, file))
    return videos

def generate_thumbnail(video_path, size=(120, 80)):
    """Generate a thumbnail from the first frame of the video.
       Falls back to a placeholder if extraction fails."""
    os.makedirs("data/thumbnails", exist_ok=True)
    thumb_path = os.path.join("data/thumbnails", os.path.basename(video_path) + ".jpg")

    # If already exists, return it
    if os.path.exists(thumb_path):
        return thumb_path

    try:
        cap = cv2.VideoCapture(video_path)
        success, frame = cap.read()
        cap.release()

        if success and frame is not None:
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            img.thumbnail(size)
            img.save(thumb_path, "JPEG")
            return thumb_path
    except Exception as e:
        print(f"Thumbnail generation failed for {video_path}: {e}")

    # Fallback: create placeholder
    return create_placeholder_thumbnail(video_path, size, thumb_path)

def create_placeholder_thumbnail(video_path, size, save_path):
    """Create a simple placeholder image with the file name."""
    img = Image.new("RGB", size, color=(50, 50, 50))
    draw = ImageDraw.Draw(img)

    filename = os.path.basename(video_path)
    filename_no_ext = os.path.splitext(filename)[0]

    # Try to use a simple font
    try:
        font = ImageFont.load_default()
    except:
        font = None

    draw.text((5, size[1]//3), filename_no_ext[:15], fill=(200, 200, 200), font=font)
    img.save(save_path, "JPEG")
    return save_path
