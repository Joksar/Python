a = 1
b = 42

day = 1
print(f'1-ый день: {a} км.')
while a < b:
    a = a + a*0.1
    day +=1

    print(f'{day}-ый день: {a:.2f} км.')
