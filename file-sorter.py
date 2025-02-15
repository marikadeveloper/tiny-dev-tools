# Organize files in a directory by type
# Usage: python file-sorter.py

import os
import shutil

EXTENSIONS = {
    "Assets": ["jpg", "jpeg", "png", "gif", "bmp", "svg", "ico"],
    "Documents": ["pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "txt", "md"],
    "Scripts": ["py", "js", "html", "php", "java", "c", "cpp"],
    "Stylesheets": ["css", "scss", "less"]
}

def organize_files(directory="."):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            for folder, exts in EXTENSIONS.items():
                if file.lower().endswith(tuple(exts)):
                    os.makedirs(folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(folder, file))
                    print(f"Moved {file} → {folder}/")

organize_files()
