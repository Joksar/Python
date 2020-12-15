revenue = int(input("Введите объем выручки в рублях: "))

expenses = int(input("Введите объем издержек в рублях: "))


income = revenue - expenses

losses = expenses - revenue
if revenue > expenses:
    print ("Вы получаете прибыль в размере ", income)
    print ("Рентабельность = ", revenue/expenses)
    emp_number = int(input("Введите кол.во сотрудников: "))
    print("Прибыль на человека = ", income / emp_number)
else:
    print ("Ваши убытки составляют: ", losses)



