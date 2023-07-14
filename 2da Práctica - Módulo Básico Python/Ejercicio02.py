class Persona:
    def __init__(self, nombre, edad, saldo, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self._saldo = saldo
        self.nacionalidad ="Peruana."

    def transferencia(self, persona2, monto):
        if self._saldo >= monto:
            self._saldo -= monto
            persona2._saldo += monto
            print("Se ha realizado la transferencia. Saldo actual: {}".format(self._saldo))
        else:
            print("Saldo insuficiente en su cuenta. No se ha realizado la transferencia.")

    def mostrar_saldo(self):
        print("Su saldo actual es: {}".format(self._saldo))

##Instancia de dos personas
personan1 = Persona("",0,500, "Peruana")
personan2 = Persona("",0,1200, "Peruana")

##Se muestra saldo de ambas personas
personan1.mostrar_saldo()
personan2.mostrar_saldo()

##Se realiza transferencia de personan1 a personan2
monto_transferencia = 600
personan1.transferencia(personan2, monto_transferencia)

##Se muestran saldos actualizados
personan1.mostrar_saldo()
personan2.mostrar_saldo()