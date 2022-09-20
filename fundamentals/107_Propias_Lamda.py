#Para saber si es un numero par o impar es mas facil definir una funcion lamda. Las funciones lamda no tienen un nombre, sino que son expresada en una sola linea se. En el ejemplo, la funcion lamda esta contenia para ser utilizada en la variable remainder. 
#En especifico esta funcion nos permite diferenciar entre numeros pares e impares. De ser un numero pa, la funcion devuelve 0, de ser impar la funcion devuelve un 1.
# lamda se le puede aplicar a cualquier variables
num = 9

remainder = lambda num: num % 2

print(remainder(num))

#otro ejemplo seria 
product = lambda x, y : x * y

print(product(2, 3))

#Otro ejemplo que no entiendo del todo, pero se puede ocupar 
def testfunc(num):
    return lambda x : x * num

result1 = testfunc(10)
result2 = testfunc(1000)

print(result1(9))
print(result2(9))