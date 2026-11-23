import os
import shutil

EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar"]
}

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print("Folder path does not exist.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isdir(file_path):
            continue

        ext = os.path.splitext(filename)[1].lower()
        moved = False

        for folder, ext_list in EXTENSIONS.items():
            if ext in ext_list:
                target_dir = os.path.join(folder_path, folder)
                os.makedirs(target_dir, exist_ok=True)
                shutil.move(file_path, os.path.join(target_dir, filename))
                moved = True
                break

        if not moved:
            other_dir = os.path.join(folder_path, "Others")
            os.makedirs(other_dir, exist_ok=True)
            shutil.move(file_path, os.path.join(other_dir, filename))

    print("Folder organized successfully.")

if __name__ == "__main__":
    path = input("Enter folder path to organize: ").strip()
    organize_folder(path)