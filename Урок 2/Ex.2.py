user_list = []
user_input = 0
a = 0

while True:
    user_input = input('Введите элементы списка. Введите STOP!, чтобы закончить список:')
    if user_input == "STOP!":
        break
    else:
        user_list.append(user_input)
        print(user_list)


for i in range(int(len(user_list)/2)):
    b = user_list[a+1]
    user_list[a+1] = user_list[a]
    user_list[a] = b
    a+=2

print(user_list)


