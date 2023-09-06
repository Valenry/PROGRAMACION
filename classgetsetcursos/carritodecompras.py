class CarritoDeCompras:
    class TarjetaDeCredito:
        def __init__(self, numero, nombre, fecha_vencimiento, es_debito=False):
            self.numero = numero
            self.nombre = nombre
            self.fecha_vencimiento = fecha_vencimiento
            self.es_debito = es_debito

    class TransferenciaBancaria: #consultar al profe si esto esta bien una class dentro de otra...(sacado ejemplo de internet)
        def __init__(self, banco, numero_cuenta):
            self.banco = banco
            self.numero_cuenta = numero_cuenta

    def __init__(self, usuario):
        self.usuario = usuario
        self.cursos_agregados = []
        self.medio_de_pago = None
        self.fecha_compra = None
        self.monto_total = 0.0

    # GETS
    def get_usuario(self):
        return self.usuario

    def get_cursos_agregados(self):
        return self.cursos_agregados

    def get_medio_de_pago(self):
        return self.medio_de_pago

    def get_fecha_compra(self):
        return self.fecha_compra

    def get_monto_total(self):
        return self.monto_total

    #  SETS
    def set_usuario(self, usuario):
        self.usuario = usuario

    def set_medio_de_pago(self, medio_de_pago):
        self.medio_de_pago = medio_de_pago

    def set_fecha_compra(self, fecha_compra):
        self.fecha_compra = fecha_compra

    def agregar_curso(self, curso):
        self.cursos_agregados.append(curso)
        self.monto_total += curso.get_costo()

    def eliminar_curso(self, curso):
        if curso in self.cursos_agregados:
            self.cursos_agregados.remove(curso)
            self.monto_total -= curso.get_costo()

    def mostrar_cursos(self): # CONSULTAR SI ASI SE AGREGA DE UNA CLASS SOLO LO QUE NECESITAMOS!!???
        for curso in self.cursos_agregados:
            print(f"Foto: {curso.get_foto()}")
            print(f"Título del Curso: {curso.get_titulo()}")
            print(f"Duración: {curso.get_duracion_meses()} meses")
            print(f"Costo: ${curso.get_costo()}")
            print("------------------------")

    def __str__(self):
        return f"Carrito de Compras de {self.usuario}: {len(self.cursos_agregados)} cursos, Monto Total: ${self.monto_total}"
