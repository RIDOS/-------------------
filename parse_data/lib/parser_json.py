import json


class ParseNewJSON:
    """
    Инициализирует экземпляр класса.
    """
    def __init__(self):
        self.data = {}

    """
    Добавляет пару ключ-значение в словарь данных.

    Аргументы:
        key (str): Ключ, который нужно добавить в словарь.
        value (Any): Значение, связанное с ключом.

    Возвращает:
        None
    """
    def add_data(self, key, value):
        self.data[key] = value

    """
    Преобразует объект в строку JSON.

    Аргументы:
        Строка, представляющая объект в формате JSON.

    Возвращает:
        str
    """
    def to_json(self):
        return json.dumps(self.data, ensure_ascii=False)

    def print(self):
        print(self.to_json())

    """
    Сохраняет JSON представление объекта в файл.

    Аргументы:
        filename (str): Имя файла, в который нужно сохранить JSON.

    Возвращает:
        None
    """
    def save(self, filename):
        with open(filename, "w", encoding="utf-8") as json_file:
            json_file.write(self.to_json())
