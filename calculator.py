def addition(a, b):
    return a + b

def substraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def main():
    print("Command-line calculator")
    num1 = float(input("Enter num1:"))
    num2 = float(input("enter num2:"))

    operator = input("Which operation do you want to perform (+, -, *, /)?")

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

if __name__ == "__main__":
    main()










    