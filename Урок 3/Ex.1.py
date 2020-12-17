def div(num_1, num_2):
    try:
        z = num_1 / num_2
    except ZeroDivisionError:
        z = "На ноль не делим"
    return z


x = float(input("Введите число x: "))
y = float(input("Введите число y: "))

print(div(x, y))