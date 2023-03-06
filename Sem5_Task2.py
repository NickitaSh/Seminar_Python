def count_even_odd(num, even_count=0, odd_count=0):
  if num == 0:
    return even_count, odd_count
  else:
    digit = num % 10
    if digit % 2 == 0:
      even_count += 1
    else:
      odd_count += 1
    return count_even_odd(num // 10, even_count, odd_count)

num = int(input("Enter a number: "))
even_count, odd_count = count_even_odd(num)
print("Even digits:", even_count)
print("Odd digits:", odd_count)