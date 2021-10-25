# funcion que imprime un numero y me da el doble

def doble(numero):
    if type(numero) in [int,float,complex] :
        return numero * 2
    # if type(numero) == int:
    #     return numero * 2
    # if type(numero) == complex:
    #     return numero *2
    else:
        return 'No se ha introducido un número'

print(doble(3))
print(doble('jojoj'))
print(doble(2.87887))
print(doble(2+8j))
print(doble([1,2,3]))