lines = 0

with open("Ex_2.txt", "r", encoding="UTF-8") as file:
    for line in file:
        lines+=1
        print(f'В строке {lines}: {len(line)} символов')
        x = line.split(" ")

        print(f'В строке {lines}: {len(x)} слов')

    print(f'Число строк: {lines}')

