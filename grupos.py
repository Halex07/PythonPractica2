nombre = input("Ingrese su nombre: ")
sexo = input("¿Cuál es su sexo M/F ")
if sexo == "F":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"
print("Su grupo de trabajo es " + grupo)