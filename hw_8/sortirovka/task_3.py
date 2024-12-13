def longest_string(strings):
    max_len = max(len(s) for s in strings)
    for s in strings:
        print('*' * (max_len - len(s)) + s)

strings = ['da', 'net', 'poka']
print(max(len(s) for s in strings))
longest_string(strings)
