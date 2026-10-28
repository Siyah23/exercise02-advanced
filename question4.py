num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))
operation = input("enter an operatiion(+, -, *, /, %, **): ")
if operation == "+":
  result = num1 + num2
elif operation == "-":
  result = num1 - num2
elif operation == "*":
  result = num1 * num2
elif operation == "/":
  if num2 == 0:
    print("error: cannot divide by zero. ")
  else:
    result = num1 / num2
    print("result:", result)
elif operation == "%":
  if num2 ==0:
    print("error: cannot calculate modulus by zero. ")
  else:
    result = num1 % num2
    print("result:", result)
elif operation == "**":
  result = num1 ** num2
else:
  print("invalid operation")
if operation in ["+", "-", "*", "**"]:
  print("result:", result)