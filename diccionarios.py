# diccionario = {
#     'nombre' : 'Fernando',
#     'apellido1' : 'López',
#     'notas' : [1,2,3,4,5] 


# }

# diccionario['apellido2'] = 'García'

# print(type(diccionario))
# print(diccionario['nombre'])
# print(diccionario['apellido1'])
# print(diccionario['apellido2'])
# print(f"Nombre completo: {diccionario['nombre']} {diccionario['apellido1']}")


vscode = {
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Archivo actual",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        }
    ]
}
vscode['configurations'] = 'hola'
print(type(vscode))
print(vscode['configurations'])