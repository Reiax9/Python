numero_pequenio = numero_de_usuario[0]
numero_grande = numero_de_usuario[0]


[1, 2, 3, 4, 5, ,6 ,-7 ,8 9, 10]

for numero in numero_de_usuario[1:]: #Filtra la lista
    if numero_pequenio > numero:
        numero_pequenio = numero
    elif numero_grande < numero:
        numero_grande = numero

print("numero grande: {}, Numero pequeño: {}".format(numero_grande, numero_pequenio))