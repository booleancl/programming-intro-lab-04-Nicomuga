#Las funciones pueden hacer cosas y tambien pueden retornar valores

def circle_area(radius):
    area = 3.1415*radius**2
    return area

# En este caso la funcion entrega o devuelve el valor de area

result = circle_area(4)
result1 = circle_area(5)
result2 = circle_area(6)
result3 = circle_area(7)

print(result)
print(result1)
print(result2)
print(result3)

print(circle_area(7))

def circle_volume(radius,height):
    volume=3.1415*radius**2*height
    return volume

result4=circle_volume(4,10)

print(circle_volume(4,10))
print(result4)

def circle_volume(radius,height):
    volume=circle_area(radius)*height
    return volume

res=circle_volume(4,10)
print(res)