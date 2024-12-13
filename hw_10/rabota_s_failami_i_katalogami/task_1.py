import os
import shutil

def move_files():
    os.makedirs('watch_me', exist_ok=True)

    for folder in ['video', 'sub']:
        for item in os.listdir(folder):
            item_path = os.path.join(folder, item)
            if os.path.isfile(item_path):
                shutil.move(item_path, 'watch_me')

if __name__ == "__main__":
    move_files()
