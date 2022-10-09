# Podemos crear o definir nuestras propias funciones
# lo hacmos con la palabra especial "def" y el cuerpo 
# La funcion debe ir correctamente identada
import time as t

def chuchuwa(inst):
    print("chuchuwa chuchuwa chuchuwa wa wa")
    t.sleep(3.5)
    print("chuchuwa chuchuwa chuchuwa wa wa")
    t.sleep(3.5)
    print("atencion")
    t.sleep(1.5)
    print("compania")
    t.sleep(1.5)
    print(inst)
    t.sleep(1.)
    print("Y!!!!")


print(chuchuwa)
print(type(chuchuwa))

#Las funciones son otro tipo de variables

# El llamado de la funcion

chuchuwa("Mano hacia el frente")
t.sleep(2)
chuchuwa("Hombro hacia atras")
t.sleep(2)
chuchuwa("Lengua afuera")
t.sleep(2)



# Si la funcion no tiene un valor de retorno, la variable definida como result, nos entregara none, que es para representar nada
result=chuchuwa("Lengua afuera")
print(result)


# En funcion chuchuwa(inst) el argumento 'inst' es un parametro requerido y por lo tanto no puede lazarse la funcion sin tener un parametro