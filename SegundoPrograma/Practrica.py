"""""
usuario = None

while usuario != "salir":
    usuario = input("pon cualquier cosa que no sea salir")
    if usuario == "quiero salir":
        print("pues escribe salir")
        # Si se pone pass, no haría falta el elif de abajo
    elif usuario == "salir":
        print("felicidades, saliste del bucle")
    else:
        print("espero que te guste el bucle")
"""""

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))