#-----------------------------------------------------------------------
# 1. Crear una función que realice operaciones básicas (suma, resta, 
# multiplicación y división) entre dos números, según la selección del 
# usuario, la forma de entrada de la función será los dos operandos y el
# caracter usado para la operación. entrada:(1,2,"+"), salida (3).
#-----------------------------------------------------------------------

def get_input():
    try:
        num1, num2, operation = input("Please enter below the first and second \
 numbers to be operated and the operation to be performed, separated by commas:")\
.split(',')

        num1 = int(num1.strip()) if num1.strip().isdigit() else float(num1.strip())
        num2 = int(num2.strip()) if num2.strip().isdigit() else float(num2.strip())

        operation = operation.strip()
        return num1, num2, operation
    except ValueError:
        raise ValueError("Invalid input. Make sure you enter two numbers and an\
 operation separated by commas.")

def basic_operation(num1, num2, operation):
    try:
        if operation == "+":
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        elif operation == "/":
            return num1 / num2
        elif operation == "%":
            return num1 % num2
        else:
            raise ValueError(f"Invalid operation: '{operation}'. Use +, -\
, *, / or %.")
    except ZeroDivisionError:
        return "Error: Division by zero not allowed."

print("Welcome, this is a program in which you can perform any basic operation \
you want between two numbers.")
try:
    num1, num2, operation = get_input()
    result = basic_operation(num1, num2, operation)
    print(f"The result is: {result}.")
except Exception as error:
    print(f"Error: {error}.")
    