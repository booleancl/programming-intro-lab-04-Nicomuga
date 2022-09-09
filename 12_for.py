#operadores
#data types
#estructuras de control. Por ejemplo, if 
#El for es una estructura de control que nos permite realizar la misma accion , pero con elementos diferentes cada vez

veggies = ['Broccoli', 'Celery', 'Lettuce', 'Carrots']

for veggie in veggies:
    print('I need to eat more '+ veggie)

fruits = ['Banana', 'apple', 'strawberry', 'orange']

for fruit in fruits:
    print('I love to eat fruits',fruit)

total = 0
for num in range(1,11):
    total = total + num

print(total)