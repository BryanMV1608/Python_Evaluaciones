import datetime

class Persona:
    def __init__(self):
        self.nombre = None
        self.edad = None
        self.nacionalidad = "Peruana."

    def solicitar_datos(self):
        self.nombre = input("Ingrese el nombre de la pesona: ")
        while True:
            try:
                self.edad = int(input("Ingrese la edad de la persona: "))
                break
            except ValueError:
                print("Error: La edad de la pesona debe ser un número entero.")

    def cumpleanios(self):
        self.edad += 1

    def fecha_registro(self):
        now = datetime.datetime.now()
        fecha = now.strftime("%Y-%m-%d %H:%M")
        return fecha

##Instancia de la clase Persona
persona = Persona()

persona.solicitar_datos()

##Se incrementa la edad de la pesona dos veces
persona.cumpleanios()
persona.cumpleanios()

##Se muestra la edad actualizada
print("la edad actualizada de la persona es: {}.".format(persona.edad))

##Se muestra la fecha de registro
fecha = persona.fecha_registro()
print("La fecha de registro de la persona fue: {}".format(fecha))


