# Una funciòn es un grupo de sentencias con un nombre que realizan una computciòn.
# Primero uno define una computacion y lluego uno llama o ejecuta esa funcion

#python viene con muchas funciones listas para usar, solo hay que llamarlas o ejecutarlas
print() #para imprimir una variable

#la mayoria de las funciones entregan un valor, es decir, nos devuelven el resultado. Ejemplo: 


str_num = '32' #Esta es una variable string, porque se encuentra encerrado entre comillla. Si no las tuviera seria una variable int
real_num=int(str_num) #Esta funcion transforma a entero
print(type(real_num), type(str_num))

float_num=3.9999
int_num=int(float_num)
print(int_num)


#esto no se puede relizar
#str_prueba = 'treinta y dos'
#real_prueba=int(str_prueba)
#print(real_prueba)

print(float("32")) #Esta funcion entrea un float
print(str(3.1415)) #Esta funcion entega un string

#e pueden anidar funciones como en el ejemplo
print(float("32")) 
print(str(3.1415)) 
