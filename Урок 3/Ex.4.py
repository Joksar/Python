# #Через **
def power(x, y):
    return x**y

print (power(11, -3))


######Через цикл

def power_2(x, y):
    y=-y
    x_1=x
    for i in range(2,y+1):
        x = x*x_1
    return 1/x

print(power_2(11,-3))