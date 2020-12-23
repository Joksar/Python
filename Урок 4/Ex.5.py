from functools import reduce
my_list = []

def my_func(prev_el, el):
    return prev_el * el

for i in range(100,1001):
    if i%2 == 0:
        my_list.append(i)

print(reduce(my_func, my_list))