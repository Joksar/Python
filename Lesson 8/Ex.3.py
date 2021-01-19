class NotANumber(Exception):
    def __init__(self, txt):
        self.txt = txt
a = []


while True:
    x = input("Введите число или stop, тобы выйти: ")
    if x == "stop":
        break
    try:
        if not x.isdigit():
            raise NotANumber("Вы ввели не число: ")
        a.append(x)
        print(a)
    except NotANumber as e:
        print(e)

