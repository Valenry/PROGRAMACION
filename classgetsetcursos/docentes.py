class Docentes:
    def __init__(self, id_docente, apellido, nombre, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email):
        self.id_docente = id_docente
        self.apellido = apellido
        self.nombre = nombre
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.localidad = localidad
        self.codigo_postal = codigo_postal
        self.provincia = provincia
        self.telefono_celular = telefono_celular
        self.email = email

    def get_id_docente(self):
        return self.id_docente

    def get_apellido(self):
        return self.apellido

    def get_nombre(self):
        return self.nombre

    def get_dni(self):
        return self.dni

    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def get_direccion(self):
        return self.direccion

    def get_localidad(self):
        return self.localidad

    def get_codigo_postal(self):
        return self.codigo_postal

    def get_provincia(self):
        return self.provincia

    def get_telefono_celular(self):
        return self.telefono_celular

    def get_email(self):
        return self.email

    def set_id_docente(self, id_docente):
        self.id_docente = id_docente

    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_dni(self, dni):
        self.dni = dni

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    def set_direccion(self, direccion):
        self.direccion = direccion

    def set_localidad(self, localidad):
        self.localidad = localidad

    def set_codigo_postal(self, codigo_postal):
        self.codigo_postal = codigo_postal

    def set_provincia(self, provincia):
        self.provincia = provincia

    def set_telefono_celular(self, telefono_celular):
        self.telefono_celular = telefono_celular

    def set_email(self, email):
        self.email = email

    def __str__(self):
        return f"Docente: {self.apellido}, {self.nombre}, DNI: {self.dni}"
