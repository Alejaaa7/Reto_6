#-----------------------------------------------------------------------
# 4. Escribir una función que reciba una lista de números enteros y 
# retorne la mayor suma entre dos elementos consecutivos.
#-----------------------------------------------------------------------

def largest_sum(list_of_ints):
    try:
        if not isinstance(list_of_ints, list):
            raise TypeError("The argument must be a list.")
        
        if len(list_of_ints) < 2:
            raise ValueError("The list must contain at least two integers.")
        
        for n in list_of_ints:
            if not isinstance(n, int):
                raise ValueError(f"The value '{n}' must be an int.")
            

        max_sum = list_of_ints[0] + list_of_ints[1]
        for i in range(1, len(list_of_ints) - 1):
            new_sum = list_of_ints[i] + list_of_ints[i + 1]
            if new_sum > max_sum:
                max_sum = new_sum
        
        return max_sum
    
    except(TypeError, ValueError) as error:
        print(f"Error: {error}")

while True:
    try:
        first_input = input("Enter the numbers separated by comas: ")
        list_of_ints = [x.strip() for x in first_input.split(',')]
        
        if len(list_of_ints) < 2:
            raise ValueError("You must enter at least two numbers.")
        
        final_list = []
        for i in list_of_ints:
            try:
                num = int(i)
                final_list.append(num)
            except ValueError:
                raise ValueError(f"'{i}' is not a valid integer.")
        break
    
    except ValueError as error:
        print(f"Error: {error}. Please try again.")

result = largest_sum(final_list)

if result is not None:
    print(f"The highest sum of two consecutive numbers is: {result}.")