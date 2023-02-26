N = int(input('Введите количество элементов: '))
print(N)
A = [i for i in range(1, N + 1)]
print(A)
num = int(input('Введите число: '))
count = 0
for el in A:
    if num == el:
        count += 1
if count == 0:
    print(f'Число не встречается')
else:
    print(f'Число встречается {count} раз')
