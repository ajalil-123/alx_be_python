
def perform_operation(num1, num2, operation):
    """performs aithmetic operations based on the input given"""
    if operation == "add":
        return num1 + num2         # adds the inputs and returns the results
    elif operation == "subtract":
        return num1 - num2          # subtracts the inputs and returns the results
    elif operation == "multiply":
        return num1 * num2           # multiplies the inputs and returns the results
    elif operation == "divide":
        if num2 == 0:
            print("Cannot divide by zero.") # handles division by zero
        else:
            return num1/num2





