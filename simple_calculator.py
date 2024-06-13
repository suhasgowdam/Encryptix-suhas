def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error Division by zero is not posssible."
    else:
        return x / y
    
#these are the valid simple operations
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

print("Welcome to Simple Calculator!")

while True:
    num1 = float(input("Enter first number: "))
    operation = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operation in operations:
        result = operations[operation](num1, num2)
        print("Result:", result)
    else:
        print("Invalid operation!")

    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != "yes":
        break

print("Thank you for using Simple Calculator!")
