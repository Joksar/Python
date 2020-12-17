my_list = [1, 3.14, "word", True, [1, 2, 3, 4], ("John", "Carl","Emily"),{"Name":"Volfgang","Surname":"Mozart"}, {1,1,2,2}]
print(type(my_list[5]))



for i in range(len(my_list)):
    a = (type(my_list[i]))
    print (f'Элемент списка под номером {i+1} - {a}')