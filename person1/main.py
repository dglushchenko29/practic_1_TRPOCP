# Новая функциональность от dev3
print("Начало программы от разработчика 3")

from utils import read_data

if __name__ == "__main__":
    data = read_data()
    print("Данные из файла:", data)
    print("Это изменение от Person1!")
