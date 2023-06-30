# create a new exception class called "MathematicalError" from BaseException class
class MathematicalError(Exception):
    pass

def parse_input(user_input):
    input_list = user_input.split()
    
    # Check if input consists of 3 elements
    if len(input_list) != 3:
        raise MathematicalError("Invalid input format")

    try:
        # Try to convert first and third input to float
        n1 = float(input_list[0])
        n2 = float(input_list[2])
    except ValueError:
        # Raise MathematicalError if conversion to float fails
        raise MathematicalError("Invalid numeric input")

    # Check if the operator is valid
    valid_operators = ['+', '-', '*', '/']
    if input_list[1] not in valid_operators:
        raise MathematicalError("Invalid operator")

    return n1, input_list[1], n2

def calculate(n1, op, n2):
    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2
    if op == '*':
        return n1 * n2
    if op == '/':
        return n1 / n2

while True:
    user_input = input('>>> ')
    if user_input == 'quit':
        break
    
    try:
        n1, op, n2 = parse_input(user_input)
        result = calculate(n1, op, n2)
        print(result)
    except MathematicalError as error:
        print("Error:", error)
