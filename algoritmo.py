cantidad = int(input("Ingrese la cantidad de números: "))
mayores = 0
menores = 0
iguales = 0

for _ in range(cantidad):
    numero = int(input("Ingrese un número: "))
    if numero > 0:
        mayores += 1
    elif numero < 0:
        menores += 1
    else:
        iguales += 1

print(f"Mayores a 0: {mayores}")
print(f"Menores a 0: {menores}")
print(f"Iguales a 0: {iguales}")
