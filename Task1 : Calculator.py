num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operation = input("Select an operation(+,-,*,/): ")

if operation == '+':
    result = num1 + num2

elif operation == '-':
    result = num1 - num2

elif operation == '*':
    result = num1 * num2

elif operation == '/':
      result = num1 / num2

print("The result is:", result)


