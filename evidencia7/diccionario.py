# Crear el diccionario de nombres  Flia con DNI
nucleo_familiar = {
    "10101010": "Liam",
    "10101011": "Facundo",
    "10101001": "Valentina"
}

# Agregar datos de Flia Ampliada
familia_ampliada = {
    "1010": "Abuela",
    "1001": "Abuelo",
    "101010": "Tío",
    "101011": "Tía",
    "101012": "Padre",
    "101020": "Madre"
}

# Combinar ambos diccionarios
diccionario_completo = {**nucleo_familiar, **familia_ampliada}


# Mostrar el diccionario de nombres con DNI
print("Diccionario de nombres con DNI:")
for dni, nombre in nucleo_familiar.items():
    print(f"DNI: {dni}, Nombre: {nombre}")

# Mostrar el diccionario completo
print("\nDiccionario completo:")
for clave, valor in diccionario_completo.items():
    print(f"DNI: {clave}, Nombre: {valor}")


