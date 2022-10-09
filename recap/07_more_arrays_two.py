#Crer un arreglo del 1 al 10 e imprimir los elementos pares

numbers = list(range(11))

for number in numbers:
    if number % 2 == 0:
        print(number)

print(type(numbers))

for number in numbers:
    if number % 2 == 1:
        print(number)