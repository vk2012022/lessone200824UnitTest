def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b

def modulo(a, b):
    if b == 0:
        raise ValueError("Невозможно найти остаток при делении на ноль")
    return a % b
