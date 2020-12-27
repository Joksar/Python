numbers = {
    "One":"Один",
    "Two":"Два",
    "Three":"Три",
    "Four":"Четыре",
}

with open("Ex.4_new.txt", "w", encoding="UTF-8") as write_text:
    with open ("Ex.4.txt", "r", encoding="UTF-8") as read_text:
        for line in read_text:
            line = line.split(" ")
            for key, val in numbers.items():
                if key in line[0]:
                    line[0] = val
                    line = str(" ".join(line))
                    print(line)
                    write_text.write(line)
