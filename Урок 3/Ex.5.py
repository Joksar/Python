def sum(list):
    sum_list = 0
    for i in range(len(list)):
        sum_list += int(list[i])
    return sum_list

total_sum = 0
while True:
    numbers = (input("Введите числа через пробел; введите q, чтобы выйти: "))
    if numbers == "q":
        break
    elif "q" in numbers:
        x = numbers.split(" ")
        x.pop()
        y = sum(x)
        total_sum += y
        print(f'Сумма введенных чисел = {y}, сумма всех введенных чисел = {total_sum}')
        break
    else:
        x = numbers.split(" ")
        y = sum(x)
        total_sum += y
        print(f'Сумма введенных чисел = {y}, сумма всех введенных чисел = {total_sum}')

