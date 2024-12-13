def create_matrix():
    matrix = []
    print("Введите элементы матрицы 3x3 построчно, через пробел:")
    for _ in range(3):
        row = list(map(int, input().split()))
        if len(row) != 3:
            print("Ошибка: строка должна содержать ровно 3 числа.")
            return None
        matrix.append(row)
    return matrix

def calculate_diagonal_sum(matrix):
    return sum(matrix[i][i] for i in range(3))

def main():
    matrix = create_matrix()
    if matrix is None:
        return

    diagonal_sum = calculate_diagonal_sum(matrix)
    print("Матрица:")
    for row in matrix:
        print(" ".join(map(str, row)))

    print(f"Сумма элементов главной диагонали: {diagonal_sum}")

if __name__ == "__main__":
    main()
