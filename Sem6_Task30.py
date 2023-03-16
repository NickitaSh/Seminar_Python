a = []
a1 = int(input("Enter the first element: "))
d = int(input("Enter the common difference: "))
n = int(input("Enter the number of elements: "))

for i in range(n):
    a_n = a1 + (i * d)
    a.append(a_n)

print("The array with arithmetic progression elements:", a)
