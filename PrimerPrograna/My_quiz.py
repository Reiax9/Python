test_juego = '¿Cuanto te gusta los videojuegos?'

Titulo = '\n' + test_juego + '\n' + '-' * len(test_juego) + '\n'

print(Titulo)

puntuacion = 0

opcion = input("¿Pregunta numero 1: ¿Cuantas horas al dia juegas\n"
               "A - 20 horas al dia\n"
               "B - 5 horas al dia\n"
               "C - Diractamente no juego\n")

if opcion == "A":
    puntuacion += 10
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 0
else:
    print('Solo se puede las opciones que ves en pantalla')
    exit()

opcion = input("¿Pregunta numero 2: ¿Cuantos juegos te compras al año?\n"
               "A - 5 juegos al año\n"
               "B - 10 juegos al año\n"
               "C - Los pirateo\n")

if opcion == "A":
    puntuacion += 5
elif opcion == "B":
    puntuacion += 10
elif opcion == "C":
    puntuacion += 0
else:
    print('Solo se puede las opciones que ves en pantalla')
    exit()

opcion = input("¿Pregunta numero 3: Te gusta los videojuegos?\n"
               "A - Sí\n"
               "B - No\n")

if opcion == "A":
    puntuacion += 5
elif opcion == "B":
    puntuacion += 0
else:
    print('Solo se puede las opciones que ves en pantalla')
    exit()


if puntuacion >= 25:
    print("Felicidades loco, eres un fanatico")
elif puntuacion >= 15:
    print("Muy bien, veo que te gusta jugar")
else:
    print("Fuera de aquí")

print(puntuacion)