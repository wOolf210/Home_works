import re

def extract_vowel_words(text):
    return re.findall(r'\b[aeiouAEIOU]\w*', text)

text = "Apple is a fruit, and it is amazing."
print(extract_vowel_words(text))
