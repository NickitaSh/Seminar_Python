S = int(input('Введите сумму:\n'))
P = int(input('Введите произведение:\n'))

for x in range(1, 1001):
    for y in range(1, 1001):
        if x + y == S and x * y == P:
            print(f'Переменная X равна: {x}\n Переменная Y равна: {y}')
            break