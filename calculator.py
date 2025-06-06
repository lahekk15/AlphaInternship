"""a = int(input("Enter Num1:"))
b = int(input("Enter Num2:"))
operator = input("Which opertion do you want to perform?")

if operator == '+':
    sum = a + b
    print(sum)

elif operator == '-':
    difference = a - b
    print(difference)

elif operator == '*':
    product = a * b
    print(product)

elif operator == '/':
    divide = a / b
    print(divide)

else:
    print("Enter operator correctly")"""

def addition(a, b):
    return a + b

def substraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def divide(a, b):
    return a / b

def main():
    print("Command-line calculator")
    num1 = float(input("Enter num1:"))
    num2 = float(input("enter num2:"))

    operator = input("Which operation do you want to perform?")

    if operator == '+':
        print("Result:" ,addition(num1,num2))

    elif operator == '-':
        print("Result:" ,substraction(num1,num2))

    elif operator == '*':
        print("Result:" ,multiplication(num1,num2))

    elif operator == '/':
        print("Result:" ,divide(num1,num2))

    else:
        print("enter operator correctly")










    