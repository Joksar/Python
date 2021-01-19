class NotANumber(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    equipment_list = []

    def add_to_list(self, dict):
        self.dict = dict
        Warehouse.equipment_list.append(self.dict)
        return Warehouse.equipment_list


class Equipment:
    def __init__(self, name, price, year, quantity):
        self.name = name
        self.price = price
        self.year = year
        self.quantity = quantity


class Computer(Equipment):
    def __init__(self, name, price, year, quantity, model):
        super().__init__(name, price, year, quantity)
        self.model = model

    def eq_dict(self):
        eq_list = {}
        eq_list["name"] = self.name
        eq_list["price"] = self.price
        eq_list["year"] = self.year
        eq_list["quantity"] = self.quantity
        eq_list["model"] = self.model

        return eq_list


class Phone(Equipment):
    def __init__(self, name, price, year, quantity, model, color):
        super().__init__(name, price, year, quantity)
        self.model = model
        self.color = color

    def eq_dict(self):
        eq_list = {}
        eq_list["name"] = self.name
        eq_list["price"] = self.price
        eq_list["year"] = self.year
        eq_list["quantity"] = self.quantity
        eq_list["model"] = self.model
        eq_list["color"] = self.color

        return eq_list


while True:
    equipment_type = input("Введите тип техники или stop, чтобы закончить: ")
    if equipment_type == "stop":
        break
    elif equipment_type.lower() == "laptop" or equipment_type.lower() == "desktop":
        equipment_price = input("Введите стоимость техники: ")
        equipment_year = input("Введите год выпуска техники: ")
        equipment_quant = input("Введите кол-во единиц техники: ")
        try:
            if not equipment_price.isdigit() or not equipment_year.isdigit() or not equipment_quant.isdigit():
                raise NotANumber("Неверный формат данных")
        except NotANumber as e:
            print(e)
            continue
        equipment_model = input("Введите модель устройста: ")
        pc_1 = Computer(equipment_type, equipment_price, equipment_year, equipment_quant, equipment_model)
        final_list = pc_1.eq_dict()
        house_1 = Warehouse()
        print(house_1.add_to_list(final_list))
    elif equipment_type.lower() == "phone":
        equipment_price = input("Введите стоимость техники: ")
        equipment_year = input("Введите год выпуска техники: ")
        equipment_quant = input("Введите кол-во единиц техники: ")
        try:
            if not equipment_price.isdigit() or not equipment_year.isdigit() or not equipment_quant.isdigit():
                raise NotANumber("Неверный формат данных")
        except NotANumber as e:
            print(e)
            continue
        equipment_model = input("Введите модель устройста: ")
        equipment_color = input("Введите цвет устройства: ")
        ph_1 = Phone(equipment_type, equipment_price, equipment_year, equipment_quant, equipment_model, equipment_color)
        final_list = ph_1.eq_dict()
        house_1 = Warehouse()
        print(house_1.add_to_list(final_list))
