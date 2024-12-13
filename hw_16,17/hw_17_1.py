import math


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def calculator():
    print("Добро пожаловать в инженерный калькулятор!")
    print("Доступные операции:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Возведение в степень (^)")
    print("6. Факториал (factorial)")
    print("7. Число Фибоначчи (fibonacci)")
    print("8. Синус (sin), Косинус (cos), Тангенс (tan), Котангенс (cot)")
    
    while True:
        try:
            operation = input("Выберите операцию (или 'выход' для завершения): ").lower()
            
            if operation == 'выход':
                print("До свидания!")
                break

            if operation in ('+', '-', '*', '/', '^'):
                a = float(input("Введите первое число: "))
                b = float(input("Введите второе число: "))

                if operation == '+':
                    print(f"{a} + {b} = {a + b}")
                elif operation == '-':
                    print(f"{a} - {b} = {a - b}")
                elif operation == '*':
                    print(f"{a} * {b} = {a * b}")
                elif operation == '/':
                    if b != 0:
                        print(f"{a} / {b} = {a / b}")
                    else:
                        print("Ошибка: Деление на ноль!")
                elif operation == '^':
                    print(f"{a} ^ {b} = {a ** b}")
            
            elif operation == 'factorial':
                n = int(input("Введите число для вычисления факториала: "))
                if n < 0:
                    print("Ошибка: факториал для отрицательного числа не существует.")
                else:
                    print(f"Факториал {n} = {factorial(n)}")
            
            elif operation == 'fibonacci':
                n = int(input("Введите номер числа Фибоначчи: "))
                if n < 0:
                    print("Ошибка: введите неотрицательное число.")
                else:
                    print(f"Число Фибоначчи с индексом {n} = {fibonacci(n)}")
            
            elif operation in ('sin', 'cos', 'tan', 'cot'):
                angle = float(input("Введите угол в градусах: "))
                angle_rad = math.radians(angle)

                if operation == 'sin':
                    print(f"sin({angle}) = {math.sin(angle_rad)}")
                elif operation == 'cos':
                    print(f"cos({angle}) = {math.cos(angle_rad)}")
                elif operation == 'tan':
                    print(f"tan({angle}) = {math.tan(angle_rad)}")
                elif operation == 'cot':
                    if math.tan(angle_rad) != 0:
                        print(f"cot({angle}) = {1 / math.tan(angle_rad)}")
                    else:
                        print("Ошибка: тангенс равен 0, котангенс не существует.")
            
            else:
                print("Неизвестная операция. Попробуйте снова.")
        
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите числовое значение.")


calculator()
