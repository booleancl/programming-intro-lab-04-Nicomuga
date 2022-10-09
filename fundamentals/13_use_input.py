# Para hacer programas interativos y obtener datos del usuario tenmos la funcion input(), que recibe como argumento lo que pedira la consola
a1 = 'Nunca lo sabras...'
name = input('Hola, como te llamas\n')
print('Hola', name,'gusto en conocerte, conozcamos tu IMC')
'''q1 = input('Quieres conocer tu IMC? (Y/N)\n')'''
'''if q1 == 'Y': 
    return weight
else:
    print(a1)'''
weight = int(input('Ingresa tu peso en Kg:\n '))
height = int(input('Ahora dime tu altura en centrimetos: \n'))

IMC = weight * height ** 2

if IMC in range(18.5,24.99)
    print(name, '!!!', 'Estas en tu peso!!') 
elif IMC =< 18.5:
    print(name, 'Cuidado, te encuentras bajo peso, consulta con un profesional de la nutricion')
elif IMC i range(25,29.99):
    print(name, 'Estas ligeramente sobrepeso, pero tranquila, es solo un poco')
elif IMC in range(30, 34.99)
    print( name, 'cuidado, tienes obesidad grao 1')
elif IMC in tange(35, 39.99)
    print(name, 'mas cuidado aun. Tienes obesidad gredo 2')
elif IMC > 40
    print(name, 'mucho cuidado. Tienes obesidad morbida. Asesorate con un profesional de la nutricion')
else:
    print('no result')
    
    


