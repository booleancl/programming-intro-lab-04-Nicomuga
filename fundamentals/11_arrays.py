# array = son estructuras de datos fundamental
#Que permite agrupar valores 

first_array = ['sacar la basura', 'pinarse', 'dormir', 'sacar la ropa']

# En python el primer elemento de un arreglo tiene poscion(index) 0
print(first_array[0])
print(first_array[1])
print(first_array[2])
print(first_array[3])
#print(first_array[4])

# we can get an array large whit the function len
print(len(first_array))

# Podemos agregar elemetos al arreglo con la funcion append al final del array
first_array.append('comer')
first_array.append('dormir')

first_array.insert(0, 'levantarse')
print(first_array)

#ademas podemos agregar elemento al arreglo. 