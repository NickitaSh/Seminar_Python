fields = ['Название', 'Цена', 'Количество', 'Ед.']
lst = [(i, {k: input(f'{k}: ') for k in fields}) for i in range(1, 4)]

for i in lst:
    print(i)
