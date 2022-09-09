import time
# Es perfectamente posible llamar una funcion dentro de otra. Lo hiximos cuando calculamos el volumen de un cilindro
#pero tambien es perfectamente posible que una funcion se llame a si misma.
#Esta es una tecnica muy poderosa para ciertos problemas.

# funcion conteo regresivo
# funcion que se llama a si misma
def countdown(number):
    if number <= 0:
        print("KABUUUM")
    else: 
        print(number)
        time.sleep(0.5)
        countdown(number - 1)

countdown(5)

def super_sum(number):
    if number <= 0:
        return number
    else:
        return number + super_sum(number - 1)
       

print (super_sum(10))


# Otra forma es crear una lista con un rango de caracteres para luego hacer iterar la lista. En est caso de 1 a 10, se escribe 11 porque el rango va de 1 a 11, ero no incluye el 11

Total = 0
for list_elem in range(1,11):
    Total = Total + list_elem

print(Total)


# Recursion infinita, sin condicion de salida. Para nada util, pero entretenida.
def infinite():
    infinite()

infinite()