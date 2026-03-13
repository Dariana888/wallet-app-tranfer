import os

folder = "C:/Users/Admin/OneDrive/Desktop/raport"

files = 0
folders = 0
total_size = 0
for item in os.listdir(folder):
    path = os.path.join(folder, item)
    if os.path.isfile(path):
        files += 1
        total_size += os.path.getsize(path)
    elif os.path.isdir(path):
        folders += 1

print("Fisiere: ", files)
print("Foldere: ", folders)
print("Dimensiune: ", total_size, " bytes")