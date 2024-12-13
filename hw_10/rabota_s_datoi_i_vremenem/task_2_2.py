def transliterate():
    direction = input("Введите направление транслитерации (ru-to-en или en-to-ru): ").strip()
    input_text = input("Введите текст для транслитерации: ").strip()

    cyrillic_to_latin = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'y', 'э': 'e', 'ю': 'yu', 'я': 'ya'
    }

    latin_to_cyrillic = {v: k for k, v in cyrillic_to_latin.items()}

    if direction == "ru-to-en":
        result = ''.join(cyrillic_to_latin.get(char, char) for char in input_text.lower())
    elif direction == "en-to-ru":
        result = ''.join(latin_to_cyrillic.get(char, char) for char in input_text.lower())
    else:
        result = "Неизвестное направление"

    print(f"Транслитерированный текст: {result}")

if __name__ == "__main__":
    transliterate()
