
num1 = input('Enter a number: ')
op = input("Provide Math Operator: ")
num2 = input('Enter another number: ')
value = []
try:
    if op == "+":
        result = float(num1) + float(num2)
        value.append(result)
        print(value)
    elif op == "-":
        result = float(num1) - float(num2)
        value.append(result)
        print(value)
    elif op == "*":
        result = float(num1) * float(num2)
        value.append(result)
        print(value)
    elif op == "/":
        result = float(num1) / float(num2)
        value.append(result)
        print(value)
    else:
        print('Invalid Input Please try again!')
except:
    print('Error Alert')
# simple random stuff.. input a number calculate the answer and put inside an array..