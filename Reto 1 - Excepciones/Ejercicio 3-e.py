#-----------------------------------------------------------------------
# 3. Escribir una función que reciba una lista de números y devuelva 
# solo aquellos que son primos. La función debe recibir una lista de 
# enteros y retornar solo aquellos que sean primos.
#-----------------------------------------------------------------------
def prime_number(num_list):
    try:
        if not isinstance(num_list, list):
            raise TypeError("The argument must be a list.")
            
        primes = []
        for i in num_list:
            if not isinstance(i, int):
                raise ValueError(f"The value '{i}' is not int.")
            
            if i < 2:
                continue
            for j in range (2, i):
                if i % j == 0:
                    break
            else:
                primes.append(i)
        return primes

    except(TypeError, ValueError) as e:
        print(f"Error: {e}")
        return None
    
print("Welcome, this is a program in which you will receive the prime numbers\
 present in a list that you provide.")

try:
    num_list = list(map(int, input("Enter the numbers to be verified, separated\
 by commas:").split(',')))
    result = prime_number(num_list)
    
    if result is not None:
        print("This are the prime numbers in your list: ", result)
    else:
        print("The primes could not be calculated due to an error.")

except Exception as error:
    print(f"Error: {error}.")