class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def total(self):
        whole_mass = self._length * self._width * 25 * 5
        return whole_mass

a = Road(40, 5)

print(a.total())





