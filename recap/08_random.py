import random
import time

fruits = ['manzana', 'pera', 'frutillas', 'pina']

print('\ntu fruta es:\n')
print('redoble de tambores....')
    
for i in range(1,4):        
    print('.')
    time.sleep(0.5)

print(random.choice(fruits))