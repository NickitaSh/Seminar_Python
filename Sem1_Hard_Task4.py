total_count = int(input('Введите общее количество журавликов: \n'))
x = total_count / 6
petya_count, katya_count, sergey_count = x, 4*x, x
print(f'Петя сделал: {petya_count}')
print(f'Катя сделала: {katya_count}')
print(f'Сергей сделал: {sergey_count}')