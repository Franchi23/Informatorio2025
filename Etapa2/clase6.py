dicionario = {1: 'a', 2:'b',3:'c'}

print ("Diccionarios - Imprimir las claves")
print("-" * 50)
for valor in dicionario.keys():     # Solo imprime las claves
    print(valor)


print ('\n',"Diccionarios - Imprimir los Valores")
print("-" * 50)

for valor in dicionario.values():     # Solo imprime los valores
    print(valor)

print ('\n',"Diccionarios - Imprimir las Claves y sus Valores")
print("-" * 50) 
for clave,valor in dicionario.items():     # Solo imprime las claves y los valores
    print(f'Clave: {clave} Valor: {valor}')
