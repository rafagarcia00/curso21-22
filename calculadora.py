def sumar(cadena):
    lista = cadena.split(',')
    for elem in lista:
        if not elem.isdigit():
            return "Error: Carácter no numérico"
            
    if len(lista)>2:
        return " Error: Demasiados números."
    elif (lista):
        return True


def mas_de_dos_numeros_da_error():
    sumar("1,2,3")

def dos_numeros_devuelve_true():
    return sumar('1,2')

def caracteres_no_numerico():
        return sumar('a,c')


# -------------------------------
print(mas_de_dos_numeros_da_error())

print(dos_numeros_devuelve_true())

print(caracteres_no_numerico())
