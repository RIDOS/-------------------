import yaml


class ParseNewYAML:
    # Хранение данных для парсинга.
    data: dict

    """

    Класс ParseNewYAML для парсинга YAML.
    @author: Imaev A.
    """
    def __init__(self) -> None:
        self.data = {}

    def parse(self, data, format="string") -> None:
        self.data[format] = data

    def print(self) -> None:
        print(yaml.dump(self.data, default_flow_style=False, allow_unicode=True))

    def save(self, filename) -> None:
        with open(filename, 'w', encoding='utf-8') as yamlfile:
            yaml.dump(self.data, yamlfile, allow_unicode=True)
