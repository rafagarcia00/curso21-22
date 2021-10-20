cadena = "hola caracola"
salida = ''
    # print(cadena[i].upper())

    # ------------------------------------------------------
salida= ''
inversa = ''

for x in cadena:
        if x== ' ' :
            break
        salida += x.upper()
        inversa = x.upper() + inversa
print(salida)
print('-------------------------')

print(inversa)