import time

def tiempo(func):
    def cal_tiempo(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        duracion = fin - inicio
        print(f"Tiempo de ejecución de la función '{func.__name__}': {duracion} segundos")
        return resultado
    return cal_tiempo()

def multiplicacion(*numeros):
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado

#
resultado1 = multiplicacion(2, 3, 4)
print("Resultado 1:", resultado1)

resultado2 = multiplicacion(5, 6, 7, 8)
print("Resultado 2:", resultado2)

resultado3 = multiplicacion(10, 2, 1)
print("Resultado 3:", resultado3)
