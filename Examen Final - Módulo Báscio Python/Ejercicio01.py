import random

def num_aleator():
    lista1 = []
    for i in range(10):
        numero = random.randint(1,100)
        lista1.append(numero)
    print("los datos de la lista creada son: {}".format(lista1))
    return lista1

def num_norepet(lista1):
    num1 = list(set(lista1))
    print("los número no repetidos de la lista creada son: {}".format(num1))
    return num1

def num_orden(num1):
    num_descendente = sorted(num1, reverse=True)
    num_ascendente = sorted(num1)
    print("los números no repetidos ordenados de mayor a menor son: {}".format(num_descendente))
    print("los números no repetidos ordenados de menor a mayor son: {}".format(num_ascendente))
    return num_descendente, num_ascendente

def num_mayor(num1):
    mayor = max(num1)
    print("El mayor número de la lista de números no repetidos es: {}".format(mayor))
    return mayor

list_random = num_aleator()
num_unico = num_norepet(list_random)
num_dscdt, num_ascdt = num_orden(num_unico)
num_max = num_mayor(num_unico)
