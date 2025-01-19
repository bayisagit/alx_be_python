def safe_divide(numerator,denominator):
    try:
        numerator=float(numerator)
        denominator=float(denominator)
        return f"The result of the division is {numerator/denominator}"
    except ZeroDivisionError:
        return f"Error: Cannot divide by zero."
    except ValueError:
        return f"Error: Please enter numeric values only."