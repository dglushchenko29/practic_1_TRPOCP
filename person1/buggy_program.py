def calculate(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"  # Новый код
    return a / b

def multiply(x, y):
    return x * y

def advanced_calc(values):
    total = sum(values)
    return calculate(total, 0)  # ОШИБКА: деление на ноль!

if __name__ == "__main__":
    result = calculate(10, 2)
    print(f"Результат деления: {result}")
    
    result2 = multiply(5, 4)
    print(f"Результат умножения: {result2}")
    
    # Новая функциональность с ошибкой
    result3 = advanced_calc([1, 2, 3])
    print(f"Продвинутый расчет: {result3}")
