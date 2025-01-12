def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Cannot divide by 0"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide'."