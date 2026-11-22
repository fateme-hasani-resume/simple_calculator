
def calculate(a, b, operator):

    if operator == "+":
        return a + b

    elif operator == "-":
        return a - b

    elif operator == "*":
        return a * b

    elif operator == "/":
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b

    else:
        return "Invalid operator."


first_number = float(input("Enter first number: "))

operator = input("Choose an operator (+, -, *, /): ")

second_number = float(input("Enter second number: "))

result = calculate(first_number, second_number, operator)

print("Result:", result)
