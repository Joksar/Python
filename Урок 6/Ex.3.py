class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return (f'Имя сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        total_income = self._income["wage"] + self._income["bonus"]
        return (f'Доход с учетом премии: {total_income}')


a = Position("Семен", "Горбунков", "Экономист", {"wage": 50000, "bonus" : 20000})
print(a.get_full_name())
print(a.get_total_income())

a_1 = Position("Рикардо", "Милос", "Танцор", {"wage": 300000, "bonus" : 700000})
print(a_1.get_full_name())
print(a_1.get_total_income())