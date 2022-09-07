# Tenemos expresiones que se pueden evaluar en terminos booleanos o dicotomicos
#ejemplo
print(10 > 9)

#Esto nos permita hacer ejecuciones condicionales, por ejemplo

def is_adult(age):
    if age >= 18:
        return True
    else:
        return False

#Estas siguientes instrucciones las podriamos leer como: "si(if el resultado de is_adult ejecutada con la variacion Gby_age es verdadero, entonces el programa imprime "Quieres una cerveza?". De otro modo (else), imprime "cantemos chuchuwa?""

gaby_age = 45
Paolas_age = 30

if is_adult(gaby_age):
    print("quieres una cerveza?")
else:
    print("Cantemos chuchuwa?")

if is_adult(Paolas_age):
    print("quieres una cerveza?")
else:
    print("Cantemos chuchuwa?")




if gaby_age > Paolas_age:
    diff = Paolas_age - gaby_age
    if diff < 5:
        print("Paola es menos que gaby por menos de 5 nos")
    elif diff < 10:
        print("Paola es menor que gaby por menos de 10 ")
    else:
        print ("Paola s mayor que gaby por mas de 10")
    #print("Gaby es mayor que Paola")
elif gaby_age == Paolas_age:
    print("Paola y Gaby tienen la misma edad")
elif gaby_age > Paolas_age + 10:
    print("Gaby es mayor que Paola por 11 o mas anos")
else:
    print("Paola es mayor que Gaby")
