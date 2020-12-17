all_goods = {}
stat = {
    "название":[],
    "цена":[],
    "количество":[],
    "ед":["шт"]
}

a=1
while True:
    add_good = input("Нажмите enter для добавления товара, введите stop для выхода")
    if add_good == "stop":
        break
    else:
        name = input("Введите наименование товара: ")
        price = int(input('Введите стоимость товара'))
        quant = int(input('Введите кол.во товара'))
        measure = input("Введите единицу измерения: ")
        stat["название"].append(name)
        stat["цена"].append(price)
        stat["количество"].append(quant)

        x = (a, {"название":name,
                 "цена":price,
                 "количество":quant,
                 "ед":measure})
        # print(tuple(x))
        all_goods[a] = tuple(x)
        a+=1


print (all_goods[1])
print (all_goods[3])

print("Аналитика товаров\n")
for key in stat:
    print(key, ' : ', stat[key])