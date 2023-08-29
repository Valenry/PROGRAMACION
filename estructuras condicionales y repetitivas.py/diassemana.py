dia = input("Ingrese un día de la semana: ")
if dia.lower() == "lunes":
    print("¡A trabajar!")
elif dia.lower() == "viernes":
    print("¡Finde, alla vamos!")
elif dia.lower() == "sabado" or dia.lower() == "domingo":
    print("¡Es finde!")
else:
    print(" Día laboral")
