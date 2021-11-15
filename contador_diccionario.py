import pprint
import collections

frase = """"
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

conteo = {}
 
for palabra in frase.upper().split():
     conteo.setdefault(palabra, 0)
     conteo[palabra] = conteo[palabra] + 1

conteoEnOrden = collections.Counter(conteo)

pprint.pprint(conteoEnOrden.most_common())