import pprint
frase = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
def cuenta_palabras(frase):
    palabras = frase.split(' ')
    dic_palabras = {}
    for p in palabras:
        if p in dic_palabras:
            dic_palabras[p] +=1
        else:
            dic_palabras[p] =1

    return dic_palabras

pprint.pprint(cuenta_palabras(frase))