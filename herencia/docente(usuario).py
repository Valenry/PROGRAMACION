class Docente(Usuarios):
    def __init__(self, id_docente, apellido, nombre, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email):
        Usuarios.__init__(self, id_docente, nombre, apellido, dni, direccion, fecha_nacimiento, localidad, codigo_postal, provincia, telefono_celular, email, "", "", "Docente")

    # Getters
    def get_id_docente(self):
        return self.id_usuario  # Heredado de la clase Usuario

    def get_apellido(self):
        return self.apellido  # Heredado de la clase Usuario

    def get_nombre(self):
        return self.nombre  # Heredado de la clase Usuario

    def get_dni(self):
        return self.dni  # Heredado de la clase Usuario

    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento  # Heredado de la clase Usuario

    def get_direccion(self):
        return self.direccion  # Heredado de la clase Usuario

    def get_localidad(self):
        return self.localidad  # Heredado de la clase Usuario

    def get_codigo_postal(self):
        return self.codigo_postal  # Heredado de la clase Usuario

    def get_provincia(self):
        return self.provincia  # Heredado de la clase Usuario

    def get_telefono_celular(self):
        return self.telefono_celular  # Heredado de la clase Usuario

    def get_email(self):
        return self.email  # Heredado de la clase Usuario

    # Setters
    def set_id_docente(self, id_docente):
        self.id_usuario = id_docente  # Heredado de la clase Usuario

    def set_apellido(self, apellido):
        self.apellido = apellido  # Heredado de la clase Usuario

    def set_nombre(self, nombre):
        self.nombre = nombre  # Heredado de la clase Usuario

    def set_dni(self, dni):
        self.dni = dni  # Heredado de la clase Usuario

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento  # Heredado de la clase Usuario

    def set_direccion(self, direccion):
        self.direccion = direccion  # Heredado de la clase Usuario

    def set_localidad(self, localidad):
        self.localidad = localidad  # Heredado de la clase Usuario

    def set_codigo_postal(self, codigo_postal):
        self.codigo_postal = codigo_postal  # Heredado de la clase Usuario

    def set_provincia(self, provincia):
        self.provincia = provincia  # Heredado de la clase Usuario

    def set_telefono_celular(self, telefono_celular):
        self.telefono_celular = telefono_celular  # Heredado de la clase Usuario

    def set_email(self, email):
        self.email = email  # Heredado de la clase Usuario

    def __str__(self):
        return f"Docente: {self.apellido}, {self.nombre}, DNI: {self.dni}"   # Heredado de la clase Usuario
