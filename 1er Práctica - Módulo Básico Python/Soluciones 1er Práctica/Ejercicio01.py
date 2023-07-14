name_1 = input("¿Cuál es su nombre?: ")
age_1 = int(input("¿Cuál es su edad?: "))

name_2 = input("¿Cuál es su nombre?: ")
age_2 = int(input("¿Cuál es su edad?: "))

list_1 = [name_1, age_1, name_2, age_2]       ##Se agrega en una lista los resultados solicitados (Nombre y Edad).

suma_1 = list_1[1] + list_1[3]                ##Se realiza la suma de las edades según la posición en la lista_1

print("La suma de las edades ingresadas al sistema es: {}".format(suma_1))

print("Los tipos de valores ingresados al sistema son: {} y {}".format(type(name_1),type(age_1)))

