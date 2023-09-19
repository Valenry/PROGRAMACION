class ConfirmacionDeCompra:
    def __init__(self, carrito, medio_pago):
        self.usuario = carrito.get_usuario()
        self.carrito = carrito
        self.fecha_compra = carrito.get_fecha_compra()
        self.monto_total = carrito.get_monto_total()
        self.medio_pago = medio_pago

    def get_usuario(self):
        return self.usuario

    def get_carrito(self):
        return self.carrito

    def get_fecha_compra(self):
        return self.fecha_compra

    def get_monto_total(self):
        return self.monto_total

    def get_medio_pago(self):
        return self.medio_pago

    def set_usuario(self, usuario):
        self.usuario = usuario

    def set_carrito(self, carrito):
        self.carrito = carrito

    def set_fecha_compra(self, fecha_compra):
        self.fecha_compra = fecha_compra

    def set_monto_total(self, monto_total):
        self.monto_total = monto_total

    def set_medio_pago(self, medio_pago):
        self.medio_pago = medio_pago

    def __str__(self):
        return f"Confirmación de Compra\nUsuario: {self.usuario.get_nombre()}\nFecha de Compra: {self.fecha_compra}\nMonto Total: ${self.monto_total}\nMedio de Pago: {self.medio_pago.get_tipo()}"
