import os
import shutil


path = input("enter the path of the folder to organize: ")


file_types = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    "Documents": ['.pdf', '.docx', '.txt', '.doc', '.pptx', '.xlsx'],
    "Videos": ['.mp4', '.avi', '.mov', '.mkv']
}


for file in os.listdir(path):
    file_path = os.path.join(path, file)

    
    if os.path.isdir(file_path):
        continue

    
    _, ext = os.path.splitext(file)

    moved = False
    for folder, extensions in file_types.items():
        if ext.lower() in extensions:
            folder_path = os.path.join(path, folder)
            os.makedirs(folder_path, exist_ok=True)
            shutil.move(file_path, os.path.join(folder_path, file))
            moved = True
            break

    if not moved:
        other_path = os.path.join(path, "Others")
        os.makedirs(other_path, exist_ok=True)
        shutil.move(file_path, os.path.join(other_path, file))

print("Files have been organized successfully!")
