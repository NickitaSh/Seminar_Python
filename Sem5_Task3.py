def getInverse(num):
    if num < 10:
        return num
    else:
        last_digit = num % 10
        reduce_num = num // 10
        return (last_digit * (10**(len(str(reduce_num))))) + getInverse(reduce_num)

num = 5678543

print(f'Inverse of {num} is {getInverse(num)}')

