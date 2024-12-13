def remove_last_line():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    with open('output.txt', 'w') as f:
        f.writelines(lines[:-1])

if __name__ == "__main__":
    remove_last_line()
