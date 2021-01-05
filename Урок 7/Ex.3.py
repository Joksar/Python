class Cell:
    def __init__(self, cell_q: int):
        self.cell_q = cell_q

    def __str__(self):
        return f'{self.cell_q}'

    def __add__(self, other):
        return Cell(self.cell_q + other.cell_q)

    def __sub__(self, other):
        if self.cell_q - other.cell_q > 0:
            return self.cell_q - other.cell_q
        else:
            return "Разность меньше 0"

    def __mul__(self, other):
        return Cell(self.cell_q * other.cell_q)

    def __truediv__(self, other):
        return Cell(self.cell_q // other.cell_q)


    def make_order(self, cell_row):
        row = ""
        for i in range(int(self.cell_q / cell_row)):
            row += f'{"*" * cell_row}\n'
        row += f'{"*" * (self.cell_q % cell_row)}'
        return row



x = Cell(21)
y = Cell(10)

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x.make_order(5))
print(y.make_order(3))