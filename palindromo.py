def limpiar(cadena):
    aux=cadena.lower()
    aux = aux.replace(' ', '')
    aux = aux.replace('.', '')
    aux = aux.replace(',', '')
    aux = aux.replace(';', '')
    aux = aux.replace(':', '')
    aux = aux.replace('á', 'a')
    aux = aux.replace('é', 'e')
    aux = aux.replace('í', 'i')
    aux = aux.replace('ò', 'o')
    aux = aux.replace('ù', 'u')
    return aux

print(limpiar('No subas , abusón'))



def palindromo(s):
    s =limpiar(cadena)
    return s == s[::-1]    