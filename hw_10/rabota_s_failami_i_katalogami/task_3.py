import os
import shutil

def move_files_from_list():
    with open('list.tsv', 'r') as f:
        files = f.read().splitlines()

    os.makedirs('list', exist_ok=True)

    for file in files:
        if os.path.isfile(file):
            shutil.move(file, 'list')

if __name__ == "__main__":
    move_files_from_list()
