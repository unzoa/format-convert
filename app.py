import os
from PIL import Image

def convert_webp_to_jpg(directory):
    files = os.listdir(directory)
    for file in files:
        if file.lower().endswith('.webp'):
            webp_path = os.path.join(directory, file)
            with Image.open(webp_path) as img:
                jpg_path = os.path.splitext(webp_path)[0] + '.jpg'
                img.convert('RGB').save(jpg_path, 'JPEG')
                print(f"Converted {webp_path} to {jpg_path}")
                os.remove(webp_path)
                print(f"Deleted original file {webp_path}")

if __name__ == "__main__":
    current_directory = os.getcwd()
    convert_webp_to_jpg(current_directory)
    print("All .webp files have been converted to .jpg files and the original .webp files have been deleted.")
    input("Press Enter to exit...")
