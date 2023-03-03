n = int(input('Введите количество элементов первого набора : '))
m = int(input('Введите количество элементов второго набора : '))

print('Введите элементы первого набора : ')
first_set = set([int(input()) for _ in range(n)])

print('Введите элементы второго набора : ')
second_set = set([int(input()) for _ in range(m)])

common_elements = first_set.intersection(second_set)

for element in sorted(common_elements):
    print(element)
