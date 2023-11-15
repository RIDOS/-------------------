from lib.parser_xml import ParseNewXML
from lib.parser_ini import ParseNewINI
from lib.parser_yaml import ParseNewYAML
from lib.parser_json import ParseNewJSON


def main():
    # Данные для парсинга.
    title = "Сектор газа - Я устал"
    description = """
        Я вернулся с работы, дорогая, я не пьян.
        Еле-еле опускаюсь я на жесткий диван.
        Я сегодня за червонец две смены отпахал,
        И я устал, я устал.
        Я сегодня за чирик две смены отпахал,
        И я устал, я устал.
    """

    arr = [[20 * 0.315 * i + 1 for j in range(20)] for i in range(20)]

    str_arr = [
        "Remember that piano",
        "So delightful unusual",
        "That classic sensation",
        "Sentimental confusion",
    ]

    # Парсинг XML документа.
    xml = ParseNewXML()
    xml.parse(data=title, format="string")
    xml.parse(data=description, format="string")

    for row in arr:
        xml.parse(data=" ".join(map(str, row)), format="int_array")

    for item in str_arr:
        xml.parse(data=item, format="str_array")

    xml.print()
    xml.save('src/output.xml')

    # Парсинг ini документа.
    ini = ParseNewINI()
    ini.parse(data=title, format="string")
    ini.parse(data=description, format="long_string")
    ini.parse(data=arr, format="int_array")
    ini.parse(data=str_arr, format="str_array")
    ini.print()
    ini.save('src/output.ini')

    # Парсинг YAML документа.
    yaml_data = ParseNewYAML()
    yaml_data.parse(data=title, format="string")
    yaml_data.parse(data=description, format="long_string")
    yaml_data.parse(data=arr, format="int_array")
    yaml_data.parse(data=str_arr, format="str_array")
    yaml_data.print()
    yaml_data.save('src/output.yaml')

    # Парсинг JSON документа.
    json_data = ParseNewJSON()
    json_data.add_data(key="title", value=title)
    json_data.add_data(key="description", value=description)
    json_data.add_data(key="arr", value=arr)
    json_data.add_data(key="str_arr", value=str_arr)
    json_data.print()
    json_data.save('src/output.json')


if __name__ == '__main__':
    main()
