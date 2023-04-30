# python simple calculator v 1.0.0

# setting all values to 0
result = 0
num1 = ""
num2 = ""
operation = ""

# asking to user what numbers you want using command
while True:
    num1 = input('Hi, fill out this first number: ')
    if num1.isdecimal():
        print(num1)
    else:
        print('please, only char numeric')
        continue
    num2 = input('and, fill out the second number: ')
    if num2.isdecimal():
        print(num2)
    else:
        print('please, only char numeric')
        continue
    operation = input('operation(+,-,*,/): ')

    if operation == "+":
        result = int(num1) + int(num2)
        print(f'the result is: {result}')
        break
    elif operation == "-":
        result = int(num1) - int(num2)
        print(f'the result is: {result}')
        break
    elif operation == "*":
        result = int(num1) * int(num2)
        print(f'the result is: {result}')
        break
    elif operation == "/":
        result = int(num1) / int(num2)
        print(f'the result is: {result}')
        break
    else:
        print('Your operation is invalid, please try again')
    continue

