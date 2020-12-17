my_list = [11,5,3,1]

while True:
    element = int(input('Введите новый элемент списка: '))
    if element in my_list:
        my_list.insert(my_list.index(element), element)
        print(my_list)
    else:
        my_list.append(element)
        my_list.sort(reverse=True)
        print(my_list)

