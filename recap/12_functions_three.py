#Las funciones pueden tener parametros por defecto

def say_country(country = 'Chile'):
    print('hola soy de', country)

say_country('Bolivia')
say_country('Peru')
say_country('Colombia')
say_country()