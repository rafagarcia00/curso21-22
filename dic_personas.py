def introduce():
    personas = {}
    

    for i in range(1):
        nombre = input("introduzca nombre: ")
        apellidos = input("introduzca apelidos: ")
        dni = input("introduzca DNI: ")
        personas[dni] = {'nombre':nombre, 'apellidos':apellidos}

    return personas

print(introduce())
