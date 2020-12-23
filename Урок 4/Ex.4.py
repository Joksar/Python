my_list = [1,2,3,4,5,5,4,3,2,1,10,13,12,14,16,15,16,14]

def generator(list_1):
    for i in range(len(list_1)):
        if list_1[i] not in list_1[:i] and list_1[i] not in list_1[i+1:]:
            yield list_1[i]

g = generator(my_list)

print(list(g))


###### Почему оно заработало после замены or на and???
