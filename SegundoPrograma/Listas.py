"""listaString = ["hola", "hola2", "holaaaaaaaaaa"]

def cadena(listaString):
    cont = 0
    max = len(listaString[0])
    for i in listaString:
        num = len(i)
        if num > max:
            max = num
            cont_max = cont
        cont += 1

    return listaString[cont_max]


if __name__ == "__main__":
    cadena(listaString)

print(cadena(listaString))"""

"""Crea una función que sume una lista de números, no se vale usar la función sum()
Ejemplo:
suma([1, 2, 3, 4, 5])

> 15"""

"""numerossumar = [1, 2, 3, 4, 5]

def sumar(numerossumar):

    val = 0

    for i in numerossumar:
        val += i

    return val


if __name__ == "__main__":
    sumar(numerossumar)
print(sumar(numerossumar))"""

"""Crea una función que te de True como resultado si el número pasado como argumento es impar
Ejemplo:
es_impar(3)
> True
es_impar(24)"""

"""def chelidon(num):
    resultado = False

    if num % 2 == 1:
        resultado = True

    return resultado


if __name__ == "__main__":
    print(chelidon())
"""

"""Crea una función que pregunte al usuario si esta seguro o no,
y devuelva los valores "True" o "False" dependiendo de si el usuario está seguro.
"""

"""def seguro(result):
    resultado = False

    if result == "S":
        resultado = True

    return resultado


result = input("Estas seguro que no te quieres morir: [S/N]")
print(seguro(result))
"""

"""Crea una función que convierta toda una string en mayusculas, no vale usar el método upper()"""

"""strmayus = "Hola... como andamos wey"


def mayus(strmayus):

    resultado = ""
    for i in strmayus:

        if "a" <= i <= "z":
            strnum = ord(i)
            strnum -= 32
            numstr = chr(strnum)
            resultado += numstr
        else:
            resultado += i
    return resultado

print(mayus(strmayus))"""

"""Crea una función que reciba como argumento un número del 1 al 100 a adivinar
y que le pregunte al usuario que adivine el número. El código se ejecutará hasta que el usuario adivine."""


import random
import os


def azar(x, y):
    num_random = random.randint(x, y)
    num_user = int(input("A ver si adivinas un número del 1 al 100: "))

    while num_user != num_random:
        num_user = int(input("Intentalo de nuevo. Adivina el número del 1 al 100: "))

        if num_user != num_random:
            print("Oooooh! Vuelve a intentarlo")

        os.system("cls")
        if num_user > 100 or num_user < 1:
            print("Pon un número del 1 al 100")

    print("Muy bien, lo lograste!")


if __name__ == "__main__":
    (azar(0, 5))
