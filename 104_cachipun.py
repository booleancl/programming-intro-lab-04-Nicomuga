import random

opciones = ["piedra", "tijera", "papel"]

print("Hola,juguemos cachipun")

print ("Ingresa su opción")
print (1, "piedra")
print (2, "tijera")
print (3, "papel")

mano1 = int(input("jugador1\n"))
mano1_eleccion = opciones[mano1 - 1]

mano_computador = random.choice(opciones)

print('Mi mano', mano1_eleccion)
print("Mano computador:", mano_computador)

if (mano1_eleccion == mano_computador):
    print("Empatan jugadores")

elif (mano1_eleccion == "piedra" and mano_computador == "tijera") or(mano1_eleccion == "tijera" and mano_computador == "papel") or (mano1_eleccion == "papel" and mano_computador == "piedra"):
    print("Felicitaciones! ganaste la partida")
    
else:
    print("Lo siento! el computador ha ganado")
