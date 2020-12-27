with open ("Ex.5.txt", "w", encoding="UTF-8") as write_file:
    write_file.write("0 560 2 44 971 11 94 360 17")

sum = 0
with open ("Ex.5.txt", "r", encoding="UTF-8") as read_file:
    for line in read_file:
        line = line.split(" ")
        for el in line:
            number = int(el)
            sum += number
        print (f'Сумма чисел в файле = {sum}')


