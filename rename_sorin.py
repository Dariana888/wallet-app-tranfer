import os

folder = 'C:/Users/sorin/Desktop/fotsi'

counter = 1
for file in os.listdir(folder):
    if file.endswith('.jpg'):
        old_path = os.path.join(folder, file)
        new_name = f'vacanta_{counter}.jpg'
        new_path = os.path.join(folder, new_name)

        os.rename(old_path, new_path)
        counter += 1