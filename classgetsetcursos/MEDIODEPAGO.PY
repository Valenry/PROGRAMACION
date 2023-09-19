class MedioDePago:
    def __init__(self, tipo):
        self.tipo = tipo

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return f"Medio de Pago: {self.tipo}"

# Método de prueba
def prueba_medio_de_pago():
    # Crear un medio de pago
    medio_pago = MedioDePago("Tarjeta de Crédito")

    # Mostrar el tipo de medio de pago
    print(medio_pago.get_tipo())

# Ejecutar el método de prueba
prueba_medio_de_pago()
