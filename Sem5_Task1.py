def calculate(num1, num2, op):
  if op == '+':
    return num1 + num2
  elif op == '-':
    return num1 - num2
  elif op == '*':
    return num1 * num2
  elif op == '/':
    if num2 == 0:
      print("Error: Cannot divide by zero!")
    else:
      return num1 / num2
  else:
    print("Error: Invalid operation!")

def main():
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  op = input("Enter an operation (+, -, *, /, 0 to exit): ")
  if op == '0':
    return
  else:
    result = calculate(num1, num2, op)
    print(result)
    main()

main()