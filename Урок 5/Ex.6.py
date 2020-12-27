### Тут буду комментировать, потому что сам офигел, пока решал.
subjects = {}
total = 0
import re

with open ("Ex.6.txt", "r", encoding="UTF-8") as read_file:
    """Читаю из файла построчно"""
    for line in read_file:
        line: list[str] = line.split(":")
        """ Делю строку. Элемент [0] станет ключом словаря, остальное использую
        для извлечения кол.ва часов по дисциплинам"""
        hour_line = str(line[1])
        """строка, из которой буду извлекать часы """
        hour_line = re.split(r'\(|\)| - | ', hour_line)
        """разбиваю строку по символам, чтобы извлечь числа"""
        for el in hour_line:
            """проверка, является ли элемент числительным"""
            try:
                number = int(el)
                total += number
                """если да, то сумма всех числительных в строке идет в значение словаря"""
            except:
                ValueError
        total = str(total)
        subjects[line[0]] = int(total)
        """добавляю пару ключ-значение в словарь"""
        total = 0
print (subjects)




