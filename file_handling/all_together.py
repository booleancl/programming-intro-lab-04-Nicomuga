print('Bienvenido al programa')
user_input = ''

while user_input != 'exit':
    print('########################')
    print('ingresa una opcion \n')
    print('1', 'agregar contenido\n')
    print('2', 'leer contenido\n')
    print('exit', 'Para salir\n')
    print('########################')

    user_input = input()

    if user_input == '1':
        file = open('file_handling/demo_two.txt', 'a')
        user_content = input('Ingresa el contenido\n')
        file.write(user_content + '\n')
        file.close()
    elif user_input == '2':
        file = open('file_handling/demo_two.txt', 'r')
        for line in file:
            print(line)
    else:
        print('opcion incorrecta')
print('Chau Chau')