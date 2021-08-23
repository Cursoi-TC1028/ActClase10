# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        ["5", "6", "s"],
        ["introducir valor 1: ", "introducir valor 2: ", 
        "introducir clave  (s, r, m, d): ","resultado: 11"],
        "Verifica los vlores de entrada"

    ),    
    (
        ["5", "6", "m"],
        ["introducir valor 1: ", "introducir valor 2: ", 
        "introducir clave  (s, r, m, d): ","resultado: 30"],
        "Verifica los vlores de entrada"

    ),

    (
        ["5", "6", "d"],
        ["introducir valor 1: ", "introducir valor 2: ", 
        "introducir clave  (s, r, m, d): ","resultado: 0.8333333333333334"],
        "Verifica los vlores de entrada"

    ),
]
