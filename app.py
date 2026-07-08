def add(a, b):
    """Простая функция сложения"""
    return a + b


def multiply(a, b):
    """Простая функция умножения"""
    return a * b


def divide(a, b):
    """Функция деления"""
    if b == 0:
        raise ValueError("Нельзя делить на ноль!")
    return a / b


if __name__ == "__main__":
    print(f"2 + 3 = {add(2, 3)}")
    print(f"2 * 3 = {multiply(2, 3)}")
    print(f"10 / 2 = {divide(10, 2)}")
