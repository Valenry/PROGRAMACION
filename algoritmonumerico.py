suma = 0
contador = 0
numero = float(input("Ingrese un número (0 para terminar): "))
while numero != 0:
    suma += numero
    contador += 1
    numero = float(input("Ingrese un número (0 para terminar): "))

if contador > 0:
    media = suma / contador
    print(f"La suma es: {suma}")
    print(f"La media es: {media}")
else:
    print("No se ingresaron números.")
