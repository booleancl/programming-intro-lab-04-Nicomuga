# Crear una funcion que imprima los numeros divisibles por 3 hasta el numero n 

def divisibles_by_three(n):
    for num in list(range(n+1)):
        if num % 3 == 0:
            print(num)

divisibles_by_three(50)

#Crear una funcion que sume todos los numeros hasta el numero n

def sum_up_to(n):
    return sum(range(n+1))

print(sum_up_to(20))


# Crear una función que calcule el volumen de una esfera de radio r

def ball_volume(r):
    return (4/3) * 3.1416 *r**3 
    

print(ball_volume(15))

# Crear una función que entregue el volumen de un cilindro de radio r y altura h

def cylinder_volume(r,h):
    return 3.14 * r**2 * h

print(cylinder_volume(10,5))