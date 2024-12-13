def merge_files():
    files = []
    while True:
        file_name = input("Введите имя файла (или 'quit' для завершения): ")
        if file_name == 'quit':
            break
        files.append(file_name)

    with open('merged_file.txt', 'w', encoding='utf-8') as output_file:
        for file in files:
            with open(file, 'r', encoding='utf-8') as f:
                output_file.write(f.read())

if __name__ == "__main__":
    merge_files()
