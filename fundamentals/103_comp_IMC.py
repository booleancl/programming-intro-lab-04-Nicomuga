import numpy as np

name = input('Hola, como te llamas\n')
print('Hola', name,'gusto en conocerte, conozcamos tu IMC')
'''q1 = input('Quieres conocer tu IMC? (Y/N)\n')'''
'''if q1 == 'Y': 

    return weight
else:
    print(a1)'''
weight = float(input('Ingresa tu peso en Kg:\n '))
height = float(input('Ahora dime tu altura en metros (Ejemplo: 1.7): \n'))

IMC = float(weight / height ** 2)

if IMC in np.arange(18.5,24.99):
    print(name, '!!!', 'Estas en tu peso!!') 
elif IMC < 19:
    print(name, 'Cuidado, te encuentras bajo peso, consulta con un profesional de la nutricion')
elif IMC in np.arange(25,29.99):
    print(name, 'Estas ligeramente sobrepeso, pero tranquil@, es solo un poco')
elif IMC in np.arange(30, 34.99):
    print( name, 'cuidado, tienes obesidad grado 1')
elif IMC in np.arange(35, 39.99):
    print(name, 'Cuidado, tu IMC es de:', int(IMC),  'Tienes obesidad grado 2')
elif IMC > 40:
    print(name, 'mucho cuidado. Tu IMC es de', int(IMC) '. Tienes obesidad morbida. Asesorate con un profesional de la nutricion')
else:
    print('no result')
    
print(IMC)