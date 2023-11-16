# TODO здесь писать код
class Matrix:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.data = []
        self.result = []

    def __str__(self):
        result = ''
        if not self.result:
            for item in self.data:
                result += '\t'.join(str(elem) for elem in item)
                result += '\n'
        else:
            for item in self.result:
                result += '\t'.join(str(elem) for elem in item)
                result += '\n'
        return result

    def add(self, new_matrix):
        self.result = [[self.data[i][j] + new_matrix.data[i][j] for j in range(self.col)] for i in range(self.row)]
        return self.__str__()

    def subtract(self, new_matrix):
        self.result = [[self.data[i][j] - new_matrix.data[i][j] for j in range(self.col)] for i in range(self.row)]
        return self.__str__()

    def multiply(self, new_matrix):
        self.result = [[0 for _ in range(self.row)] for _ in range(new_matrix.col)]
        for m in range(self.row):
            for n in range(new_matrix.col):
                for o in range(self.col):
                    self.result[m][n] += self.data[m][o] * new_matrix.data[o][n]
        return self.__str__()

    def transpose(self):
        self.result = [[self.data[j][i] for j in range(self.row)] for i in range(self.col)]
        self.row, self.col = self.col, self.row
        return self.__str__()


# Примеры работы с классом:

# Создание экземпляров класса Matrix
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

# Тестирование операций
print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1.add(m2))

print("Вычитание матриц:")
print(m1.subtract(m2))

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print("Умножение матриц:")
print(m1.multiply(m3))

print("Транспонирование матрицы 1:")
print(m1.transpose())
