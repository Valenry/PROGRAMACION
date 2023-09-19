class MediosDeContacto:
    def __init__(self, id_medio_contacto, fecha, email, telefono, direccion, nombre):
        self.id_medio_contacto = id_medio_contacto
        self.fecha = fecha
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.nombre = nombre

    def get_id_medio_contacto(self):
        return self.id_medio_contacto

    def get_fecha(self):
        return self.fecha

    def get_email(self):
        return self.email

    def get_telefono(self):
        return self.telefono

    def get_direccion(self):
        return self.direccion

    def get_nombre(self):
        return self.nombre

    def set_id_medio_contacto(self, id_medio_contacto):
        self.id_medio_contacto = id_medio_contacto

    def set_fecha(self, fecha):
        self.fecha = fecha

    def set_email(self, email):
        self.email = email

    def set_telefono(self, telefono):
        self.telefono = telefono

    def set_direccion(self, direccion):
        self.direccion = direccion

    def set_nombre(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"ID: {self.id_medio_contacto}, Fecha: {self.fecha}, Email: {self.email}, Teléfono: {self.telefono}, Dirección: {self.direccion}, Nombre: {self.nombre}"


class TiposDeMedioDeContacto(MediosDeContacto):
    def __init__(self, id_medio_contacto, fecha, email, telefono, direccion, nombre, tipo_medio_contacto):
        self.tipo_medio_contacto = tipo_medio_contacto
        # Llamamos explícitamente al constructor de la clase base
        MediosDeContacto.__init__(self, id_medio_contacto, fecha, email, telefono, direccion, nombre)

    def obtener_tipo_medio_contacto(self):
        return self.tipo_medio_contacto

    def set_tipo_medio_contacto(self, tipo_medio_contacto):
        self.tipo_medio_contacto = tipo_medio_contacto

    def __str__(self):
        return f"{MediosDeContacto.__str__(self)}, Tipo de Medio de Contacto: {self.tipo_medio_contacto}"

# Ejemplo de uso:
whatsapp_contact = TiposDeMedioDeContacto(1, "2023-08-14", "ejemplo@xxx.com", "123456789", "Chile 342", "Liam", "WhatsApp")
print(whatsapp_contact)
