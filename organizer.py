import os
import shutil

path = os.path.expanduser("~/Downloads")

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3", ".wav"]
}

def organize_files():
    print(f"Scanning folder: {path}")
    
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            
            for folder_name, extensions in file_types.items():
                if file_extension in extensions:
                    folder_path = os.path.join(path, folder_name)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    
                    try:
                        shutil.move(file_path, os.path.join(folder_path, filename))
                        print(f"Moved: {filename} to {folder_name}")
                    except Exception as e:
                        print(f"Failed to move {filename}: {e}")

if __name__ == "__main__":
    organize_files()