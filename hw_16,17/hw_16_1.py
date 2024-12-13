def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def print_fibonacci_numbers(count):
    for i in range(1, count + 1):
        print(f"fibonacci number {i} = {fibonacci_recursive(i)}")


if __name__ == "__main__":
    print_fibonacci_numbers(10)