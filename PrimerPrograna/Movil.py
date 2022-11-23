escoge_movil = "Escoge un movil"

tittle = "\n" + escoge_movil + "\n" + "-" * len(escoge_movil) + "\n"

print(tittle)

movil = input("¿Que marca de movil quieres tener?\n"
              "¿iOS o Andorid?\n")

dinero = input('¿Tienes dinero?')

if movil == "Android":
    if dinero == 'No':
        print("Compra un android chino de 100€")
    elif dinero == 'Sí':
        camara_movil = input('Te importa la cámara del movil')
        if camara_movil == 'Sí':
            print('Comprate un Google Pixel Supercamara')
        elif camara_movil == "No":
            print('Comprate un Android calidad-precio')
        else:
            print("Mal")
            exit()
    else:
        print("Mal")
        exit()
elif movil == "iOS":
    if dinero == "Sí":
        print("Comprate un iphone ultra pro max")
    elif dinero == "No":
        print("Comprate un iphone de segunda mano")
    else:
        print("Mal")
        exit()
else:
    print("Mal")
    exit()