def ingresar_datos():
    while True:
        try:
            dato1 = float(input("Ingresar el dato N°01: "))
            dato2 = float(input("Ingresar el dato N°02: "))
            break
        except ValueError:
            print("¡Cuidado!, el dato ingresado no es válido.")
    return dato1, dato2

def dividir(dato1, dato2):
    while True:
        try:
            division = dato1 / dato2
            print("La división de los datos ingresados es: {}.".format(division))
            break
        except ZeroDivisionError:
            print("Los datos ingresados dieron error.")
            dato2 = float(input("Ingrese un segundo número distinto de cero:"))

def evaluar_suma(dato1, dato2):
    while True:
        try:
            suma = dato1 + dato2
            print("El resultado de la suma es: {}.".format(suma))
            if suma < 0:
                raise ValueError("Error: Suma incorrecta.")
            break
        except ValueError as error:
            print(error)
            dato1, dato2 = ingresar_datos()

dato1, dato2 =ingresar_datos()
dividir(dato1,dato2)
evaluar_suma(dato1,dato2)


