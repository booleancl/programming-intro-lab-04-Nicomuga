estudiantes = [
    'Abel',
    'Aylin',
    'Charlotte',
    'Claudia',
    'Elsy',
    'Javiera',
    'Karen',
    'Maria soledad',
    'Maryelin',
    'Nicolas',
    'Paola',
    'Paola M.',
    'Silvia',
    'Yaritza'
]
user_option = input('Selecciona tu posicion\n')

index = int(user_option) 
estudiante = estudiantes[index - 1]

print(estudiante)
