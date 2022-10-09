#completar la siguiente funcion para que se imprima cualquier tabla de multiplicacion hasta el 12
multiplicador = list(range(1,13))

def multiplication_table(number = 1):
    print('###################################################')
    for multiplicador in range(13):
        print(number, 'x', multiplicador, '=' , number * multiplicador)

multiplication_table(2)
multiplication_table(7)