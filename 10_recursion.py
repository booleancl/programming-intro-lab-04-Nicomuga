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

        