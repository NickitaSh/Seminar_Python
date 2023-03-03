# Solution 1 (using list)
month_number = int(input('Введите номер месяца:\n'))
seasons = ['Зима', 'Весна', 'Лето', 'Осень']
index = (month_number - 1) // 3
season = seasons[index]
print(f'Решение с помощью list.Это - {season}')

month_number = int(input('Введите номер месяца:\n'))
season_map = {
    1: 'Зима',
    2: 'Зима',
    3: 'Зима',
    4: 'Весна',
    5: 'Весна',
    6: 'Весна',
    7: 'Лето',
    8: 'Лето',
    9: 'Лето',
    10: 'Осень',
    11: 'Осень',
    12: 'Осень',
}
season = season_map[month_number]
print(f'Решение с помощью dict.Это - {season}')
