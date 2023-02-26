num = int(input('Введите целое положительное число:\n'))
max_num = 0
while num > 0:
    if max_num < num % 10:
        max_num = num % 10
    num = num // 10
print(max_num)