
frase = "hola, me quiero suicidar"
vocales = ["a", "e", "i","o", "u"]
vocales_encontradas = 0

for letra in frase:
    if letra in vocales: #Si hay vocal en la frase, hará los siguientes pasos. Si no la hay, revisará la siguiente letra
        print("He encontrado una '{}'".format(letra))
        vocales_encontradas += 1

print("vocales encontradas: {}".format(vocales_encontradas))



"""""
numbers = [1, 2, 3, 5, 6, 7, 8]

for n in numbers:
    if n == 4:
        break
else:
    print("No se encontro el 4")
"""