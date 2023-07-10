# Importing required module
import os

# Taking Label folder Path
folder_path = "/home/hp/Documents/Annotation/labels"

for file_name in os.listdir(folder_path):
    if file_name.endswith(".txt") and os.path.getsize(os.path.join(folder_path, file_name)) == 0:
        file_path = os.path.join(folder_path, file_name)
        os.remove(file_path)
        print(f"File {file_name} removed successfully.")
        
print("All empty label.txt files have been removed.")

