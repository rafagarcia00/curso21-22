def introduce():
    personas = {}
    

    for i in range(1):
        nombre = input("Introduzca nombre: ")
        apellidos = input("Introduzca apelidos: ")
        dni = input("Introduzca DNI: ")
        continuar = input("¿Desea continuar introduciendo datos? S/N: ")
        if continuar == 'S':
            pass
        elif continuar == 'N':
            break
        else:
            continuar != ''
        personas[dni] = {'nombre':nombre, 'apellidos':apellidos}
        
    return personas

print(introduce())
