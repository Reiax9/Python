def main():
    print("Confirme su contraseña")
    contraseña = input("Escriba su contraseña: ")
    seg_contraseña = input("Escriba e nuevo su contraseña: ")

    if contraseña == seg_contraseña:
        print("Contraseña confirmada. ¡Hasta la vista!")

    elif contraseña != seg_contraseña:

        contador = 0

        while contador < 3:

            if contraseña != seg_contraseña:
                print("La contraseña no coincide. Inténtalo de nuevo.")
                contraseña = input("Escriba su contraseña: ")
                seg_contraseña = input("Escriba de nuevo su contraseña: ")

            elif contraseña == seg_contraseña:
                print("Contraseña confirmada. ¡Hasta la vista!")
                break

            contador += 1

        if contador == 3:
            print("Lo sentimos, has superado la cantidad de intentos.")


if __name__ == "__main__":
    main()
