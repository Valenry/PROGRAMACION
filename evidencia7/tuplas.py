# Tres tuplas
tupla1 = ("Luna llena", "7 de enero", "Domingo")
tupla2 = ("Cuarto menguante", "15 de enero", "Lunes")
tupla3 = ("Luna nueva", "21 de enero", "Lunes")

# Crear una lista que las contenga
lista_tuplas = [tupla1, tupla2, tupla3]

# Mostrar la lista de tuplas
print("Lista de tuplas:")
for tupla in lista_tuplas:
    print(f"Fase: {tupla[0]}, Fecha: {tupla[1]}, Día: {tupla[2]}")
