import random

# Crear diccionario
numeros_telefono = {}
contador = 1

while contador <= 5:  # Puedes cambiar este valor para tener más claves
    telefono = f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
    numeros_telefono[f"Persona{contador}"] = telefono
    contador += 1

# Mostrar el diccionario 
print("Diccionario de números de teléfono:")
for clave, telefono in numeros_telefono.items():
    print(f"Clave: {clave}, Teléfono: {telefono}")

