from lxml import etree as et
import xml.dom.minidom as minidom


class ParseNewXML:
    """

    Класс ParseNewXML для парсинга XML.
    @author: Imaev A.
    """
    def __init__(self):
        self.root = et.Element('xml', version="1.0", encoding="utf-8")

        self.str = et.SubElement(self.root, 'string')
        self.int_array = et.SubElement(self.root, 'int_array')
        self.str_array = et.SubElement(self.root, 'str_array')

    """
    Парсинг XML документа.

    Параметры:
        data: Данные для парсинга.
        format: Формат данных для парсинга.

    Возвращает:
        None
    """
    def parse(self, data, format="string") -> None:
        if format == "string":
            # Формирование строки.
            et.SubElement(self.str, 'value').text = data
        elif format == "int_array":
            # Формирование контейнера для массива чисел.
            if len(self.int_array) == 0:
                et.SubElement(self.int_array, 'values')
            values = et.SubElement(self.int_array.find('values'), 'value')
            values.text = data
        elif format == "str_array":
            # Формирование контейнера для массива строк.
            if len(self.str_array) == 0:
                et.SubElement(self.str_array, 'values')
            values = et.SubElement(self.str_array.find('values'), 'value')
            values.text = data

    """
    Вспомогательный метод для вывода XML документа.

    Параметры:
        elem: XML документ.

    Возвращает:
        None
    """
    def prettify(self, elem) -> str:
        rough_string = et.tostring(elem, pretty_print=True)
        reparsed = minidom.parseString(rough_string)
        return reparsed.toxml()

    """
    Вывод XML документа.

    Возвращает:
        None
    """
    def print(self) -> None:
        pretty_xml = self.prettify(self.root)
        print(pretty_xml.strip())

    """
    Сохранение XML документа.

    Параметры:
        filename: Путь к файлу для сохранения XML документа.

    Возвращает:
        None
    """
    def save(self, filename) -> None:
        pretty_xml = self.prettify(self.root)
        with open(filename, 'w') as f:
            f.write(pretty_xml)
