# Crear una funcion que imprima los numeros divisibles por 3 hasta el numero n 

def divisibles_by_three(n):
    if n % 3 == 0:
        for num in range(n+1):
            print(num)

divisibles_by_three(50)

#Crear una funcion que sume todos los numeros hasta el numero n

def sum_up_to(n):
    for num in range(n+1):
        return num + num

print(sum_up_to(20))
