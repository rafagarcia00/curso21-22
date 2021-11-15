def decode(msj):

    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    inversa = alfabeto[--1]
    salida = ''
    for letra in msj:
        if letra.isalpha():
            idx = alfabeto.index(letra)
            salida += inversa[idx]
        else:
            salida += letra
    return(salida)