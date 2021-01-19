class MyZeroDivison(Exception):
    def __init__(self, txt):
        self.txt = txt

print("найти кратное двух чисел")
try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    if b == 0:
        raise MyZeroDivison("Ты идиот?")
    else:
        print(a / b)

except MyZeroDivison as e:
    print(e)

