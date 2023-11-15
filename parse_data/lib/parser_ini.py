import configparser
import json


class ParseNewINI:
    # Конфигурация для парсинга ini.
    config: configparser.ConfigParser

    """

    Класс ParseNewINI для парсинга ini.
    @author: Imaev A.
    """
    def __init__(self):
        self.config = configparser.ConfigParser()

    """
    Парсинг ini документа.

    Параметры:
        data: Данные для парсинга.
        format: Формат данных для парсинга.

    Возвращает:
        None
    """
    def parse(self, data, format="string") -> None:
        section_name = format + '_data'
        if not self.config.has_section(section_name):
            self.config.add_section(section_name)

        if format == "int_array":
            data_str = json.dumps(data)
            self.config.set(section_name, 'int_array', data_str)
        elif format == "str_array":
            data_str = json.dumps(data)
            self.config.set(section_name, 'str_array', data_str)
        else:
            self.config.set(section_name, 'string', data)

    """Вспомогательный метод для вывода ini документа."""
    def print(self) -> None:
        for section in self.config.sections():
            print(f"[{section}]")
            for key, value in self.config[section].items():
                print(f"{key} = {value}")

    """
    Сохранение ini документа.

    Параметры:
        filename: Имя файла для сохранения.

    Возвращает:
        None
    """
    def save(self, filename):
        with open(filename, 'w') as configfile:
            self.config.write(configfile)
