#Задача4
revenue = int(input('Введите выручку фирмы :\n'))
costs = int(input('Введите издержки фирмы :\n'))
profit = revenue - costs
if (profit > 0):
    print(f'Ваш финансовый результат - прибыль) = {profit}')
    print('Значит вычисляем рентабельность выручки(соотношение прибыли к выручки')
    print(f'Рентабельность выручки = {profit / revenue}')
    count_employees = int(input('Введите количество сотрудников :\n'))
    print(f'Прибыль  в расчете на одного сотрудника :\n {profit / count_employees}')
else:
    print(f'У вас отрицательный финансовый результат :\n {profit}')
