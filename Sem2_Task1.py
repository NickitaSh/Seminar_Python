a = int(input('Введите результат в первый день:\n'))
b = int(input('Введите конечный результат:\n'))
assert b > a
count = 0
while a < b:
    a += 0.1*a
    count += 1
print(count + 1)

