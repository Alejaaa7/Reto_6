#-----------------------------------------------------------------------
# 2. Realice una función que permita validar si una palabra es un 
# palíndromo. Condición: No se vale hacer slicing para invertir la 
# palabra y verificar que sea igual a la original.
#-----------------------------------------------------------------------


def is_palindrome(word):
    try:
        if not isinstance(word, str):
            raise TypeError("The entered value is not a text string.")

        if not word.isalpha():
            raise ValueError("The word must contain only letters, without spaces\
 or symbols.")

        word = word.lower()
        for i in range(len(word) // 2):
            if word[i] != word[-(i + 1)]:
                return False
        return True

    except (TypeError, ValueError) as e:
        print(f"Error: {e}.")
        return None  # Usamos None para indicar que la verificación falló por una excepción

# Programa principal
print("Welcome. This program checks whether a word is a palindrome.")

try:
    word = input("Please enter the word to be verified:").strip()
    result = is_palindrome(word)

    if result is True:
        print("This word is a palindrome!")
    elif result is False:
        print("This word is NOT a palindrome.")
    else:
        print("The word could not be verified due to an input error.")

except Exception as e:
    print(f"Error: {e}.")
