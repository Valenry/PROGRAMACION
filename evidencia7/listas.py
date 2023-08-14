# Lista de nombres de la flia
nombres_familia = ["Juan", "José", "María M", "María", "Mario", "Ana", "Patricia", "Paula", "Valentina", "Facundo", "Liam", "Lidia", "Valentín"]

# Lista de T de febrero 2024
temperaturas_febrero = [23, 23, 23, 23, 23, 22, 22, 22, 22, 22, 21, 22, 22, 22, 23, 23, 23, 22, 22, 22, 21, 22, 22, 22, 22, 22, 22, 22, 22]

# Lista de ciudades visitadas
ciudades_visitadas = ["Miami", "Caba", "San Juan", "San Luis", "Gral Pico", "México DF"]

# Lista de eventos importantes
eventos_importantes = [
    {"evento": "Nacimiento", "fecha": "21/05/1982"},
    {"evento": "Casamiento", "fecha": "15/05/2001"},
    {"evento": "Nacimiento Facundo", "fecha": "27/12/2000"},
    {"evento": "Nacimiento Liam", "fecha": "27/09/2011"},
    {"evento": "Divorcio", "fecha": "06/06/2010"},
    {"evento": "Fallecimiento madre", "fecha": "19/07/2021"},
    {"evento": "Operación", "fecha": "01/04/2022"},
    {"evento": "Graduación escuela", "fecha": "01/12/1999"},
    {"evento": "Graduación terciario", "fecha": "05/05/2006"}
]

# Ordenar alfabéticamente lista de nombres de flia
nombres_familia.sort()

# Ordenar ascendentemente  lista de T
temperaturas_febrero.sort()

# Agregar las Ts del mes siguiente a la lista de T
temperaturas_marzo = [22, 21, 21, 22, 22, 22, 22, 22, 22, 22, 21, 21, 21, 21, 21]
temperaturas_febrero.extend(temperaturas_marzo)

# Quitar de la lista de nombres de familia a abuelos
nombres_familia.remove("Lidia")
nombres_familia.remove("Valentín")

# Quitar de la lista de ciudades la ciudad menos linda que hayas visitado
ciudades_visitadas.remove("Gral Pico")

# Mostrar todas 

print("Lista de nombres de familia ordenada alfabéticamente:", nombres_familia)
print("Lista de temperaturas ordenada ascendentemente:", temperaturas_febrero)
print("Lista de ciudades visitadas:", ciudades_visitadas)
print("Lista de eventos importantes:")
for evento in eventos_importantes:
    print(f"{evento['evento']}: {evento['fecha']}")
