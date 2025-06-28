#-----------------------------------------------------------------------
# 5. Escribir una función que reciba una lista de string y retorne 
# únicamente aquellos elementos que tengan los mismos carácteres. e.g. 
# entrada: ["amor", "roma", "perro"], salida ["amor", "roma"].
#-----------------------------------------------------------------------


def same_characters(list_of_str):
    try:
        if not isinstance(list_of_str, list):
            raise TypeError("The input must be a list.")
        
        if len(list_of_str) == 0:
            raise ValueError("The list is empty.")

        groups = {}

        for i in list_of_str:
            if not isinstance(i, str):
                raise ValueError(f"The element '{i}' is not a valid string.")
            
            cleaned_word = i.strip().lower()
            order = ''.join(sorted(cleaned_word))

            if order in groups:
                groups[order].append(cleaned_word)
            else:
                groups[order] = [cleaned_word]

        result = []
        for j in groups.values():
            if len(j) > 1:
                result.extend(j)

        return result

    except (TypeError, ValueError) as error:
        print(f"Error in function: {error}")
        return None

# Main program
print("Welcome! This program will find words that have the same characters (anagrams) from a list you provide.")

try:
    user_input = input("Enter a list of words separated by commas: ")
    list_of_str = [word.strip() for word in user_input.split(",")]

    result_list = same_characters(list_of_str)

    if result_list is not None:
        print("The resulting list of anagrams is:", result_list)
    else:
        print("The operation could not be completed due to an error.")

except Exception as e:
    print(f"Unexpected error: {e}")
