from sys import argv
script_name, wage, hours, bonus = argv
salary = int(wage)*int(hours)+int(bonus)
print(f'Зарплата сотрудника составит {salary} рублей.')