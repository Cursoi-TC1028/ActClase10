# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case the test fails
# To test another case, add another tuple

input_values = [
        # Test case 1
        (
            ["25", "5","6","45","2","3"],
            ["proceso 1:","Introduce las horas: ", "Introduce las minutos: ", "Introduce las segundos: ", "proceso 2:",
              "Introduce las horas: ", "Introduce las minutos: ", "Introduce las segundos: ",
              "proceso 1: 90306","proceso 2: 162123"],
            "Revisa tu código",
        ),
        # Test case 2
        (
           ["12", "25","6","85","6","45"],
            ["proceso 1:","Introduce las horas: ", "Introduce las minutos: ", "Introduce las segundos: ", "proceso 2:",
              "Introduce las horas: ", "Introduce las minutos: ", "Introduce las segundos: ",
              "proceso 1: 44706","proceso 2: 306405"],
            "Revisa tu código",
        ),
        # Test case 3
        (
            ["75", "85","94","52","32","1"],
            ["proceso 1:","Introduce las horas: ", "Introduce las minutos: ", "Introduce las segundos: ", "proceso 2:",
              "Introduce las horas: ", "Introduce las minutos: ", "Introduce las segundos: ",
              "proceso 1: 275194","proceso 2: 189121"],
            "Revisa tu código",
        )
    ]
