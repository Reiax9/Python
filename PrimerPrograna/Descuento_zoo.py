
edad = int(input('Digame su edad: '))
tipo_de_carnet = input('Digame su tipo de carnet (E para estudiantes / P Pensinista / F Familia numerosa / N nada')

if (edad < 35 and edad > 25 and tipo_de_carnet == 'E') or /
    edad < 10 or /
    (edad < 65 and tipo_de_carnet == 'P') or /
    (tipo_de_carnet == 'F'):
    print('Se te aplica el descuento')
else:
    print('no se te aplica el descuento')
