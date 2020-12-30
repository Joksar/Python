
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")

class Pen(Stationery):
    def draw(self):
        print("Ручка потекла.")

class Pencil(Stationery):
    def draw(self):
        print("Стержень сломался.")

class Handle(Stationery):
    def draw(self):
        print("Маркер не пишет.")

a = Pen("Kugel")
a.draw()

b = Pencil("KOHINOOR")
b.draw()

c = Handle("MAGIC")
c.draw()