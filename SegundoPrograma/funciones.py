import numbers


def number():
    numbers = int(input("Pon un número para exponer: "))
    my_number = numbers ** 2
    return(my_number)

def main():
    print("numero a exponer {}".format(number()))
    print("El segundo numero {}".format(number()))


if __name__ == "__main__":
    main()


"""""
def duplica(num):
    x = num * 2
    return x

print(duplica(4))
"""""

"""""
def medir_largos(iterable, *args):
    
    def sumar(numero1, numero2):
        return numero1 + numero2

    print("suma total", sumar(3, 5))
    
    if args:
        largos = [len(iterable)]
        for a in args:
            largos.append(len(a))
        return largos
    return len(iterable)


def main():
    print(medir_largos("heeeey"))
    print(medir_largos("heeeey", "como estas", "viejo sabroso"))


if __name__ == "__main__":
    main()
