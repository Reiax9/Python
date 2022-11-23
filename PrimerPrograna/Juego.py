print('Intenta adivinar el numero del 1 al 10')
numeros_azar = 1, 2, 3, 4, 5, 6, 8, 9, 10
numero_ganador = 7
numero_escoger= input('¿Cual es el numero que que estoy pensando? ')

if numero_escoger == '7':
    print('¡Felicidadeeeees, has acertado!')
if numero_escoger != '7':
    print('Oooooh fallaste...')




# Como lño ha hecho nate

import random

numero_ganador = random.randint(1,10)
numero_elegido = int(input('Elige un numero: '))

if numero_elegido == numero_ganador:
    print('Has ganado!')

if numero_elegido > 10:
    print('Te has pasado un poco, era uno entre diez')
if numero_elegido < 1:
    print('Te has quedado corto')

print('El numero ganador era: {}'.format(numero_ganador))