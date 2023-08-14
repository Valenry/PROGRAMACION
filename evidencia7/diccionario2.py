# Diccionario con claves autogeneradas y valores de Nª de Tel.
numeros_telefono = {}
contador = 1

while True:
    telefono = input(f"Ingrese el número de teléfono para Persona{contador} (o 'salir' para finalizar): ")
    
    if telefono.lower() == 'salir':
        break
    
    numeros_telefono[contador] = telefono
    contador += 1

# Mostrarlo 
print("Diccionario de números de teléfono:")
for clave, telefono in numeros_telefono.items():
    print(f"Clave: {clave}, Teléfono: {telefono}")


# Método de prueba eficiente :(
diccionario_prueba = {1: "123-456-7890", 2: "987-654-3210", 3: "555-555-5555"}
print("\nMétodo de prueba eficiente:")
for clave, telefono in diccionario_prueba.items():
    print(f"Clave: {clave}, Teléfono: {telefono}")


# DIO!! NO TOCAR MAS!