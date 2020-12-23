def fact_1(number):
    x = list(range(1, number+1))
    y = 1
    for i in range(len(x)):
        y = (y*x[i])
        yield y

# def fact(number):
#     y = 1
#     for i in range(1, number+1):
#         y = (y*i)
#         yield y

for el in fact_1(5):
    print (el)

# for el in fact(5):
#     print(el)