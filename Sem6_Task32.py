a = [3, 6, 1, 5, 2, 8, 9]
min_val = 3   
max_val = 6

indices = [i for i, x in enumerate(a) if min_val <= x <= max_val]
print("The indices of array elements within the given range are:", indices)
