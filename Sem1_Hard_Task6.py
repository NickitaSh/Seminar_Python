num_ticket = input('Введите номер билета:\n')
sum1 = 0
sum2 = 0

for i in range(len(num_ticket)):
    if i < 3:
        sum1 += int(num_ticket[i])
    else:
        sum2 += int(num_ticket[i])


if sum1 == sum2:
    print('Ваш билет счастливый')
else:
    print('Ваш билет несчастливый')