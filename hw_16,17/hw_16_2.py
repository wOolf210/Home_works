def is_power_of_two(num):
    return num > 0 and (num & (num - 1)) == 0


if __name__ == "__main__":
    num = int(input("Введите число: "))
    print(is_power_of_two(num))