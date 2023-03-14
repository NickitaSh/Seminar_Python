class Matrix:
    def __init__(self, data):
        self.matrix = data

    def __str__(self):
        rows = []
        for row in self.matrix:
            row_str = '\t'.join(str(elem) for elem in row)
            rows.append(row_str)
        return '\n'.join(rows)

    def __add__(self, other):
        new_data = []
        for i in range(len(self.matrix)):
            new_row = []
            for j in range(len(self.matrix[0])):
                new_elem = self.matrix[i][j] + other.matrix[i][j]
                new_row.append(new_elem)
            new_data.append(new_row)
        return Matrix(new_data)


m1_data = [[31, 22],
           [37, 43],
           [51, 86]]

m2_data = [[3, 5, 32],
           [2, 4, 6],
           [-1, 64, -8]]

m1 = Matrix(m1_data)
m2 = Matrix(m2_data)

print(f'm1:\n{m1}')
print()

print(f'm2:\n{m2}')
print()

m3 = m1 + m2
print(f'm3 = m1 + m2:\n{m3}')
