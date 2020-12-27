with open ("new_file_ex_1.txt", "w", encoding="UTF-8") as f_1:
    while True:
        x = (input("Введите, что записать в файл или нажмите enter, чтобы выйти: "))
        if x == "":
            break
        f_1.write(x + "\n")

with open ("new_file_ex_1.txt", "r", encoding="UTF-8") as f_2:
    for line in f_2:
        print(line)
