N = int(input('Введите число:\n'))
sqr_two = 2
count = 1

for i in range(1, N, 2):
    if sqr_two < N:
        sqr_two = sqr_two * 2
        count += 1
    else:
        break
print(count)