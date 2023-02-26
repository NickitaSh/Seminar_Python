def my_rating(a, value):
    max_value = max(a)
    if value > max_value:
        a.insert(0, value)
    elif value in a:
        a.insert(a.index(value), value)
    else:
        a.append(value)


my_list = [7, 5, 3, 3, 2]
print(my_list)
my_rating(my_list, 3)
print(my_list)
