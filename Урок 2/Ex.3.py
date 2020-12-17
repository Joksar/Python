#Через список
month = int(input("ВВедите номер месяца: "))
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
fall = [9, 10, 11]

if month in winter:
    print("Месяц зимний")
elif month in spring:
    print('Месяц весенний')
elif month in summer:
    print('Месяц летний')
elif month in fall:
    print('Месяц осенний')
#########################################################
#Через словарь

month = int(input("ВВедите номер месяца: "))
year = {'Зима':[12,1,2],
        'Весна':[3,4,5],
        'Лето':[6,7,8],
        'Осень':[9,10,11],
        }
if month in year["Зима"]:
    print('Месяц зимний')
elif month in year['Весна']:
    print('Месяц весенний')
elif month in year['Лето']:
    print('Месяц летний')
elif month in year['Осень']:
    print('Месяц осенний')