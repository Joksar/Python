low_salary = []
employees = 0
total_sal = 0

with open("Ex.3.txt", "r", encoding="UTF-8") as text_3:
    for line in text_3:
        x = line.split(":")
        y = x[0]
        x = int(x[1])
        employees += 1
        if x < 20000:
            low_salary.append(y)
            total_sal += x
        else:
            total_sal += x

low_salary = str(low_salary)
medium = total_sal / employees
print(f'Сотрудники с зп меньше 20000: {low_salary}.')

print(f'Средняя зп: {medium}')
