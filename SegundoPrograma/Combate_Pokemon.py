from random import randint
import os

VIDA_INICIAL_PIKACHU= 80
vida_actual_pikachu = VIDA_INICIAL_PIKACHU


VIDA_INICIAL_SQUIRTLE = 90
vida_actual_squirtle = VIDA_INICIAL_SQUIRTLE

TAMANIO_DE_BARRA = 20


while vida_actual_pikachu > 0 and vida_actual_squirtle > 0:

    #Se desenvuelve el combate

    print("Turno de pikachu")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        print("Pikachu ataca con bola boltio")
        vida_actual_squirtle -= 10
    else:
        print("Pikachu ataca con placaje electrico")
        vida_actual_squirtle -= 15

    if vida_actual_squirtle < 0:
        vida_actual_squirtle = 0

    if vida_actual_pikachu < 0:
        vida_actual_pikachu = 0

    barra_de_vida_pikachu = int(vida_actual_pikachu * TAMANIO_DE_BARRA / VIDA_INICIAL_PIKACHU)
    print("pikachu:   [{}{}] ({}/{})".format("*" * barra_de_vida_pikachu,
                                             " " * (TAMANIO_DE_BARRA - barra_de_vida_pikachu),
                                     vida_actual_pikachu, VIDA_INICIAL_PIKACHU))

    barra_de_vida_squirtle = int(vida_actual_squirtle * TAMANIO_DE_BARRA / VIDA_INICIAL_SQUIRTLE)
    print("squirtle:   [{}{}] ({}/{})".format("*" * barra_de_vida_squirtle,
                                              " " * (TAMANIO_DE_BARRA - barra_de_vida_squirtle),
                                      vida_actual_squirtle, VIDA_INICIAL_SQUIRTLE))
    input("Enter para continuar...\n")

    os.system("cls")
    # Turnop de squirtle
    print("Turno Squirtle")

    ataque_squirtle = None

    while ataque_squirtle not in ["A", "B", "C"]:
        ataque_squirtle = input("¿Que ataque deseas realizar? [A] Placaje, [B] Burbuja, [C] Pistola agua")

    if ataque_squirtle == "A":
        print("Squirtle ataca con placaje!")
        vida_actual_pikachu -= 10

    elif ataque_squirtle == "B":
        print("Squirtle ataca con Burbuja")
        vida_actual_pikachu -= 12
    elif ataque_squirtle == "C":
        print("Squirtle ata con Pistola agua")
        vida_actual_pikachu -= 15

    if vida_actual_squirtle < 0:
        vida_actual_squirtle = 0

    if vida_actual_pikachu < 0:
        vida_actual_pikachu = 0

    barra_de_vida_pikachu = int(vida_actual_pikachu * TAMANIO_DE_BARRA / VIDA_INICIAL_PIKACHU)
    print("pikachu:   [{}{}] ({}/{})".format("*" * barra_de_vida_pikachu,
                                             " " * (TAMANIO_DE_BARRA - barra_de_vida_pikachu),
                                             vida_actual_pikachu, VIDA_INICIAL_PIKACHU))

    barra_de_vida_squirtle = int(vida_actual_squirtle * TAMANIO_DE_BARRA / VIDA_INICIAL_SQUIRTLE)
    print("squirtle:   [{}{}] ({}/{})".format("*" * barra_de_vida_squirtle,
                                              " " * (TAMANIO_DE_BARRA - barra_de_vida_squirtle),
                                              vida_actual_squirtle, VIDA_INICIAL_SQUIRTLE))
    input("Enter para continuar...\n")
    os.system("cls")

if vida_actual_pikachu  > vida_actual_squirtle:
    print("Pikachu gana!")
else:
    print("Squirtle gana!")

