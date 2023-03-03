n = int(input('Введите количество кустов: '))

berries = [int(input('Введите количество ягод на кусте {}: '.format(i))) for i in range(n)]

max_berries = 0
for i in range(n):
    berry_sum = berries[i] + berries[(i-1)%n] + berries[(i+1)%n]
    max_berries = max(max_berries, berry_sum)

print(f'Максимальное количество ягод, собранное за один проход: {max_berries}')