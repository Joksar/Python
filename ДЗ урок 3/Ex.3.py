def max_sum(x,y,z):
    my_list = [x,y,z]
    my_list.remove(min(my_list))
    return sum(my_list)


sum = max_sum(11, 21, 19)
print(sum)
