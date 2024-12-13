def common_chars_in_files():
    files = []
    while True:
        file_name = input("Введите имя файла (или 'quit' для завершения): ")
        if file_name == 'quit':
            break
        files.append(file_name)

    common_chars = None
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            file_content = set(f.read())
            if common_chars is None:
                common_chars = file_content
            else:
                common_chars &= file_content

    with open('common_chars.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(''.join(common_chars))

if __name__ == "__main__":
    common_chars_in_files()
