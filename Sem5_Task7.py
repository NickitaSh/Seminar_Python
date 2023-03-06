def sum_of_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_n(n - 1)

def verify_equality(n):
    left_side = sum_of_n(n)
    right_side = n * (n + 1) / 2
    return left_side == right_side

print(verify_equality(5))