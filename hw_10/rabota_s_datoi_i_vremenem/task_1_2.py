def remove_bad_words():
    input_file = input("Введите имя исходного файла: ")
    bad_words_file = input("Введите имя файла с неприемлемыми словами: ")
    output_file = input("Введите имя итогового файла: ")

    with open(bad_words_file, 'r', encoding='utf-8') as f:
        bad_words = set(f.read().splitlines())
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for word in bad_words:
        content = content.replace(word, "")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    remove_bad_words()
