"""

Hay 3 modos para leer un archivo con la funcion open()

'r' para leer 
'a' para agregar al final (append)
'w' para escribir sobre el contenido
"""
file = open('file_handling\sample.txt', 'r', encoding='utf-8')
#La funcion open entrega un 'objeto'. Entenderemos por objetocomo algo que tiene datos y metodos. Los metodos son para manipular datos

print(file)

#Para leer el contenido del objeto file, tenemos el metodo del objeto
#read(). Las funciones que le pertenecen a un objeto las llamaremos metodos
print(file.read())


file = open('file_handling\sample.txt', 'r', encoding='utf-8')

#Podemos leer el archivo utilizando for

for linea in file: 
    print(linea)

file.close()