import os

file_path = "file_for_delete.txt"
if os.path.exists(file_path):
    os.remove(file_path)
else:
    print(f"There is no file found with name: {file_path}")
