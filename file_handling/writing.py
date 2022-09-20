# Podemos escribir un archivo con el modo 'a'

file = open('file_handling\demo.txt', 'a')

file.write('Hola inmundo')

file.close()

#Precaucion, el modo w borra el contenido anterior
file = open('file_handling\demo.txt', 'w')

file.write('Oooops, se borro el contenido anterior')

file.close()
