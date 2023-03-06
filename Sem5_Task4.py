def getSum(n, sum):
    if n == 0:
        return sum
    else:
        elem = (-0.5)**n
        sum += elem
        return getSum(n-1, sum)

n = int(input("Enter the number of items: "))
print("The number of elements is {}, their sum is {}".format(n, getSum(n, 0)))