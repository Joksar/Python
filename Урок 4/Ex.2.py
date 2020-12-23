my_list = [11,34,25,93,156,7,3,65,100,8]


def generator (list_1):
    for i in range(0,len(list_1)):
        if len(list_1[0:i+1]) < len(list_1) and list_1[i+1] > list_1[i]:
            yield list_1[i+1]

g = generator(my_list)
print (list(g))

