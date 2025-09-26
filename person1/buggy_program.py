def calculate(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

def multiply(x, y):
    return x * y

def advanced_calc(values):
    total = sum(values)
    if len(values) == 0:  # ИСПРАВЛЕНИЕ: проверка на пустой список
        return "Ошибка: пустой список"
    return calculate(total, len(values))  # ИСПРАВЛЕНИЕ: делим на количество элементов

if __name__ == "__main__":
    result = calculate(10, 2)
    print(f"Результат деления: {result}")
    
    result2 = multiply(5, 4)
    print(f"Результат умножения: {result2}")
    
    result3 = advanced_calc([1, 2, 3])
    print(f"Продвинутый расчет: {result3}")
