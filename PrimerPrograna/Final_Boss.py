import random
tittle = "Bienvenido al juego del escape"
print("\n" + tittle + "\n" + '-' * len(tittle) + "\n")

print("Esto se trata una historia japonesa, donde un samurai está recluido en la pagoda. Se logra desatar la cuerda\n"
      "y este sale por la ventana para esconderse en los arbustos. Ve que está lleno de guardias. Hay dos maneras\n"
      "de salir de esta, intenta robar la katana de un guardia, sube la muralla y salta al otro lado o se disfraza\n"
      "de guardia.")

opciones = input("[S]subir, [R]robar o [D]disfrzar")

armas_inventario = True


if opciones == "S":
    print("Estas encima de la muralla, pero ves que al otro lado hay una gran caida, pero los guardias te han visto\n"
          "¿Ahora que harás?")
    opciones = input("[S]saltar, [R]rendirte")
    if opciones == "S": #Saltar la muralla
        print("Saltaste y por tu gran suerte abajo había un gran charco de agua, pero acabaste mal herido\n"
              "por suerte había una agraciada joven limpiando la ropa, esta se ofrece ayudarte...")
        opciones = input("[A] Te dejas ayudar por la joven, [B] Desconfias y huyes por el bosque")
        if opciones == "A": #La decision con la joven
            print("La joven te lleva a su casa y te cura las heridas, pero te tiene que llevar a casa para poder\n"
                  "curarte")
            opciones = input("[S] Aceptas, [N] Declinas la oferta")
            if opciones == "S": #Aceptas la propuesta
                print("Te trato las heridas antes de marchar para no morirte desangrado.\n"
                      "La joven resultaba que era la hija del shogun, ya cuando te descubrio el padre, era demasiado\n"
                      "tarde para escapar. Por no decir que mancillaste el honor de su familia al tocar a su hija.\n"
                      "Te senteciaron a seppuku, al cual aceptaste y moristes con honor. Fin")
            elif opciones == "N":
                print("Declinas la oferta, entonces la joven marcha del lugar para volver a su casa. Intentas volver\n"
                      "solo, pero las heridas eran graves. a mitad del camino, encontrastes unos salvajes que estaban\n"
                      "en guardia. Al verte no dudaron en dispararte. Fin")
        elif opciones == "B":
            print("Huyes despavorido de la joven al darte cuenta que tiene un emblema de una familia de la realeza,\n"
                  "pero tus heridas ni siquiera estaban tratadas, así que moristes desangrado a mitad del bosque. Fin")
    elif opciones == "R":
        print("Los guardias te vuelven a capturar y te meten en la pagoda otra vez, pero esta vez te cortan las\n"
              "piernas para que no vuelvas a escapar. Fin")
elif opciones == "R": #Aquí decide robar
    print("Estas en los arbustos, y te vas acercando poco a poco a un guardia. Le coges del cuello y lo asfixias sin\n"
          "que nadie se de cuenta. Ha pesar de tu honor de samurai, estas pensando en robar las armas\n\n"
          "¿Coges la katana y wakizaki a pesar de perder tu honor?")
    opciones = input("[S] Sí, [N] No")

    armas_inventario = False

    if opciones == "S":
        print("Coges las armas, a pesar de perder tu honor")
    elif opciones == "N":
        print("No coges las armas para poder seguir con tu honor")
    else:
        print("Tienes que poner resultado en pantalla")
        exit()
    print("Después de asegurarte que el guardia esta muerto, te diriges por las tiendas de campañas intentando pasar\n"
          "desapercibido. Ves que delante hay dos hombres patrullando y entras en la tienda que tienes en la derecha\n"
          "con intención de que no te vean, pero tienes la mala suerte que había uno durmiendo adentro y lo\n"
          "despiertas con el ruido al entrar\n\nEl guardia te mira a los ojos durante unos segundos antes de abrir\n"
          "la boca para advertir a sus nakamas...")
    opciones = input("[A] Atacar al guardia, [B] Hui de la tienda por la puerta de atras")
    if opciones == "A" == armas_inventario == True:
        print("Matas al guardia antes de que salga un hilo de voz, ves que por la parte de atras puedes salir,\n"
              "pero antes de nada, coges las monedas que tenia encima de la mesa y ves un mapa del castillo...\n"
              "ves donde tendrías la ruta de escape. Sales de la tienda y vas directo donde te marca el mapa\n"
              "sales del castillo y te escapas. Fin")
    elif opciones == "A" == armas_inventario == False:
        print("Saltas encima del guardia e intentas asfixiarlo con las manos, pero el guardia te golpe en la sien\n"
              "propinando un golpe fatal. Fin")
    elif opciones == "B":
        print("Huyes")
elif opciones == "D":
    print("Sales disparado de los arbustos hasta una tienda,")

