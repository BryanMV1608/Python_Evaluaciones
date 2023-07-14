import random
import math

def archv(archivo):
    try:
        with open(archivo, "x") as file:
            print("El archivo {} creado con éxito.".format(archivo))
    except FileExistsError:
        print("El archivo {} ya existe.".format(archivo))

def lista(archivo):
    try:
        tamano = int(input("Indique el tamaño de lista a generar: "))

        with open(archivo, "w") as file:
            list1 = random.sample (range(1,100), tamano)
            file.write("El tamaño de la lista es: {}".format(tamano))
            file.write("\nLista de número: \n")
            for numero in list1:
                file.write("{}\n".format(numero))

        print("Se creó la lista en el archivo.")
    except ValueError:
        print("El tamaño de la lista a generar debe ser un numero entero.")

def raiz_cuadrada(archivo):
    try:
        with open(archivo, "a") as file:
            file.write("\nLas Raíces cuadradas de los números son: \n")

            with open(archivo, "r") as file:
                contenido = file.readlines()
                num1 = [float(numero) for numero in contenido[2:]]

                for numero in num1:
                    raiz_sqrt = math.sqrt(numero)
                    file.write("{}\n".format(raiz_sqrt))

        print("Las raíces cuadradas calculadas se encuentran en el archivo.")
    except ValueError:
        print("Error en el cálculo de la raíz cuadrada.")
