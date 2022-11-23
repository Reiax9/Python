
dolar_euro = 0.87
libra_euro = 1.16




opcion = input("¿Como quiere cambiar la moneda?\n"
               "A: Euro a libra\n"
               "B: Libra a euro\n"
               "C: Dolar a euro\n"
               "D: Euro a dolar\n")



texto_usuario  = "Introduzca una cantidad de {} a convertir"


if opcion == "A":
    cantidad_escogida = float(input(texto_usuario.format("euros")))
    print("La cantidad en libras es: {}".format(cantidad_escogida * libra_euro)  # Como se deberia de hacer
elif opcion == "B":
    cantidad_escogida = float(input(texto_usuario.format("libras")))
    print("La cantidad en euros es: {}".format(antidad_escogida / libra_euro))
elif opcion == "C":
    print("La cantidad de transaccion es: {}".format(dolar_euro * cantidad_escogida))
elif opcion == "D":
    print("La cantidad de transaccion es: {}".fomrat(euro_dolar * cantidad_escogida))


#libras = input('Introduzca la cantidad: ')

#euro = float(libras) * float(valor)

#print('El cambio al € sería {}'.format(euro))

