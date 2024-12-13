import os

def rename_files():
    for file in os.listdir():
        if file.endswith('.jpg'):
            name, ext = file.split('_')
            surname, name = name.split('-')
            new_name = f"{name}_{surname}{ext}"
            os.rename(file, new_name)

if __name__ == "__main__":
    rename_files()
