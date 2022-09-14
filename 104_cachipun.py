import random

options = ["piedra", "tijera", "papel"]

print("Hola,juguemos cachipun")

print ("Ingresa su opción")
print (1, "piedra")
print (2, "tijera")
print (3, "papel")

user_input = int(input("jugador1\n"))
user_option = options[user_input - 1]

computer_option = random.choice(options)

print('Mi mano', user_option)
print("Mano computador:", computer_option)

if (mano1_eleccion == mano_computador):
    print("Empatan jugadores")

elif (mano1_eleccion == "piedra" and mano_computador == "tijera") or(mano1_eleccion == "tijera" and mano_computador == "papel") or (mano1_eleccion == "papel" and mano_computador == "piedra"):
    print("Felicitaciones! ganaste la partida")
    
else:
    print("Lo siento! el computador ha ganado")
