class Matrix:
    def __init__(self, array):
        self.array = array

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.array)):
            for j in range(len(self.array[i])):
                summa = self.array[i][j] + other.array[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.array[i]):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)

    def __str__(self):
        return str(f'{self.array[0]}\n{self.array[1]}\n{self.array[2]}')


x = Matrix([[15,71,10,23,53], [11,22,33,44,55], [99, 88, 77, 66, 55]])
y = Matrix([[15,71,10,23,53], [11,22,33,44,55], [99, 88, 77, 66, 55]])

print (x + y)




