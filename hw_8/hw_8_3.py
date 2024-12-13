import re

def split_by_delimiters(text, delimiters):
    return re.split(f'[{delimiters}]', text)

text = "apple,orange;banana|grape"
delimiters = ",;|"
print(split_by_delimiters(text, delimiters))
