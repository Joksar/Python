class Complex:
    def __init__(self, c_number):
        self.c_number = c_number

    def __add__(self, other):
        return Complex(complex(self.c_number) + complex(other.c_number))

    def __mul__(self, other):
        return Complex(complex(self.c_number) * complex(other.c_number))

    def __str__(self):
        return f'{self.c_number}'


a = complex(6, 3)
b = complex(2, 1)
comp_1 = Complex(a)
comp_2 = Complex(b)
print(comp_1 + comp_2)
print(comp_1 * comp_2)
