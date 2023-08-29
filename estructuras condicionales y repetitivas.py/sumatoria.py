suma = 0
numero = int(input("Ingrese un número (-1 para terminar): "))
while numero != -1:
    suma += numero
    numero = int(input("Ingrese un número (-1 para terminar): "))
print(f"La sumatoria es: {suma}")
