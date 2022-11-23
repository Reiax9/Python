class Persona:
    nombre = ""
    apellidos = ""
    ntelefono = ""
    nID = ""
    sexo = ""

    def __init__(self, nombrex, apellidos, nID, sexo, ntelefono):  # Despues de self son variables vacías
        self.nombre = nombrex  #Los tres que tienen puesto el self, hace referencia a los de arriba
        self.apellidos = apellidos
        self.nID = nID
        self.sexo = sexo
        self.ntelefono = ntelefono

    def saludar(self):
        saludo = "Hola, mi nombre es {} y el apellido {}\nMi numero de telefono" \
                 " es: {} y soy {} con mi numero de documentacion {}".format(self.nombre, self.apellidos,
                                                                             self.ntelefono, self.sexo, self.nID)
        return saludo


class planilla(Persona):  #Una heredada
    salario = 15000
    moneda = "€"

    def mi_salario(self):
        msj = "mi salario es de: {}{}".format(self.salario, self.moneda)
        return msj



p1 = planilla("Reiax", "Moon", "48249229J", "hombre", "695 01 91 60")
print(p1.saludar())
print(p1.mi_salario())