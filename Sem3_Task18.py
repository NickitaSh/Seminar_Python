N = int(input('Введите количество элементов: '))
x = int(input('Введите число: '))
a = [int(i) for i in range(N)]
number = 0
for i in range(len(a)):
    if (x - a[i]) < x - number and x - a[i] > 0:
        number = i
print(a[number])
