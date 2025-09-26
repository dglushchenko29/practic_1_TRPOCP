def read_data():
    try:
        with open('data.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Файл не найден"
