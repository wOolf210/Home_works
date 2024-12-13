def main():
    n = input("Введите длину списка: ")

    if not n.isdigit():
        print("Ошибка: длина списка должна быть числом.")
        return

    n = int(n)

    print("Введите элементы списка через пробел:")
    elements = input().split()

    if not all(x.isdigit() for x in elements):
        print("Ошибка: все элементы списка должны быть числами.")
        return

    elements = list(map(int, elements))

    odd_numbers = [x for x in elements if x % 2 != 0]
    even_numbers = [x for x in elements if x % 2 == 0]

    print(" ".join(map(str, odd_numbers)))
    print(" ".join(map(str, even_numbers)))

    if len(odd_numbers) > len(even_numbers):
        print("NO")
    else:
        print("YES")

if __name__ == "__main__":
    main()