#Similar alos arreglos, los diccionarios nos permiten estructurar informacion. Con la diferencia de que los elementos estan ordenados por llave y no por indice. Ejemplo

my_car = {
    'brand' : 'Mazda',
    'model' : '5',
    'year' : 2022,
    'options' : ['5 puerta', 'Aire acondicionado', 'Frenos ABS'],
    'available' : True
}

print(my_car['brand'])
print(my_car['year'])
print(my_car['options'])
print(my_car['available'])
print(my_car['model'])

# Si queremos un arreglo o lista con todas las llaves tenemos el metodo .key()
print(my_car.keys())


# Si queremos todos los valores, tenemos el metodo .values()
print(my_car.values())


# Podemos tambien actualizar valores de una determinada llave
my_car['model'] = '9'

print(my_car['model'])


# Tambien podemos agregar llaves y valores
my_car['color'] = 'silver'

print(my_car)