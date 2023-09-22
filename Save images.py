import os
import shutil

def main():
    extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".svg", ".raw", ".nef", ".cr2", ".webp", ".ico", ".heif", ".heic", ".psd", ".ai"]

    downloads_folder = os.path.expanduser("C:/Users/sande/Downloads")
    pictures_folder = os.path.expanduser("C:/Users/sande/OneDrive/Pictures/Saved Pictures")

    downloads = os.listdir(downloads_folder)

    for download in downloads:
        _, extension = os.path.splitext(download) #breaks the file into two parts.  The base for _, and the extension in extension
        if extension in extensions:
            source_path = os.path.join(downloads_folder, download) #Joins the downloads folder path to the download file to create a full path
            destination_path = os.path.join(pictures_folder, download) #Joins the pictures folder path to the download to the download file to set a destination path
            shutil.move(source_path, destination_path)
            print(f"Moved {download} to {pictures_folder}")
        else:
            print(f"{download} is not an image file, nothing to move.")

if __name__ == "__main__":
    main()








