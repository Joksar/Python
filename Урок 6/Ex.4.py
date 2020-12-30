import random

class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Поехали!")

    def stop(self):
        print("Стой!")

    def turn(self):
        x = random.randint(0,1)
        if x == 0:
            print ("Поворот налево")
        else:
            print ("Поворот направо")

    def show_speed(self):
        print(f'Скорость = {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Превышение скорости!")
        else:
            print("Скорость в норме")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Превышение скорости!")
        else:
            print("Скорость в норме")

class PoliceCar(Car):
    pass



car_1 = TownCar(70, "Yellow", "Lancer EVO IX", False)
car_1.show_speed()
car_1.turn()

car_2 = PoliceCar(300, "Black", "Aventador", True)
car_2.show_speed()
car_2.turn()

car_3 = WorkCar(300, "Black", "Aventador", False)
car_3.show_speed()
car_3.turn()





