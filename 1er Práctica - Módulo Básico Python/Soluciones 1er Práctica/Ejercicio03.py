nombre = input("¿Cuál es su nombre?: ")
apellidos = input("¿Cuál es su apellido?: ")
edad = input("Digite su edad: ")
dni = input("Digite su DNI: ")

dict_1 = {"Nombre": nombre, "Apellidos": apellidos, "Edad": edad, "DNI": dni}

print(dict_1)


########

dict_1["Profesion"] = "Contador"

print(dict_1)

#########

del dict_1["DNI"]
print("los datos actualizados del diccionario son: {}".format(dict_1))




