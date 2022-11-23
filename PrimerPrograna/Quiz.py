titulo = 'Bienvenido al test sobre quesos'
print('\n' + titulo + '\n' + '-' * len(titulo) + '\n')

puntuacion = 0

opcion = input('Pregunta 1: Que haces cuando ves una tabla de queso?\n'
               'A - Salgo corriendo\n'
               'B - Pruebo uno de los quesos o incluso varios\n'
               'C - No pueso evitar devorarla\n')

if opcion == 'A':
    puntuacion += 0  # Es un pequeño aajo para no tener que repetir puntuacion
elif opcion == 'B':
    puntuacion = puntuacion + 5
elif opcion == 'C':
    puntuacion = puntuacion + 10
else:
    print('Las opciones posibles son A, B y C')
    exit()

opcion = input('Pregunta 2: ¿Como te gusta la hamburgesa?\n'
               'A - Sin queso\n'
               'B - Con queso\n'
               'C - Pan y queso\n')


if opcion == 'A':
    puntuacion += 0  # Es un pequeño aajo para no tener que repetir puntuacion
elif opcion == 'B':
    puntuacion = puntuacion + 5
elif opcion == 'C':
    puntuacion = puntuacion + 10
else:
    print('Las opciones posibles son A, B y C')
    exit()


opcion = input('Pregunta 3: ¿Eres intolerante a la lactosa?\n'
               'A - Si\n'
               'B - A veces\n'
               'C - No\n')


if opcion == 'A':
    puntuacion += 0  # Es un pequeño aajo para no tener que repetir puntuacion
elif opcion == 'B':
    puntuacion = puntuacion + 5
elif opcion == 'C':
    puntuacion = puntuacion + 10
else:
    print('Las opciones posibles son A, B y C')
    exit()


if puntuacion >= 25:
    print('Felicididades, eres un fanatico del queso')
elif puntuacion >= 15:
    print('Te gusta el queso, muy bien')
else:
    print('Oooh no te gusta el queso :C')


print(puntuacion)