from itertools import count, cycle

for el in count(11):
    if el > 121:
        break
    else:
        print(el)


c = 0
for el in cycle([77,66,55,44,33,22,11]):
    if c > 14:
        break
    print (el)
    c += 1