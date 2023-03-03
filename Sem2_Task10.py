n = int(input('Введите общее количество монеток:\n'))
count = 0
for i in range(n):
    if i % 2 == 0:
        count += 1
print(f'Количество монет которое нужно перевернуть равно: {count}')
