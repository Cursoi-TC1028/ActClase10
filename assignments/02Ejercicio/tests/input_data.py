# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        ["5","2","a"],
        ["Ingresa el ancho: ", "Ingresa el largo: ","Quiere calcular el área o el perímetro del rectángulo:",
        "(a para área y p para perímetro)","op: ","area: 10.0"],
        "Debe mostrar:\nscore incorrecto"
    ),
    (
        ["5","2","p"],
        ["Ingresa el ancho: ", "Ingresa el largo: ","Quiere calcular el área o el perímetro del rectángulo:",
        "(a para área y p para perímetro)","op: ","perimetro: 14.0"],
        "Debe mostrar:\nscore incorrecto"
    )    
]
