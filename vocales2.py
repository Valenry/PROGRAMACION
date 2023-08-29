while True:
    caracter = input("Ingrese un caracter (0 para terminar): ")
    if caracter == '0':
        break
    elif caracter.lower() in 'aeiou':
        print("VOCAL")
    else:
        print("NO VOCAL")
