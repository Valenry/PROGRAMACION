import smtplib
from email.mime.text import MIMEText

class Usuarios:
    def __init__(self, id_usuario, nombre, apellido, dni, direccion, fecha_nacimiento, localidad, codigo_postal, provincia, telefono_celular, email, clave_acceso, estado_usuario):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento
        self.localidad = localidad
        self.codigo_postal = codigo_postal
        self.provincia = provincia
        self.telefono_celular = telefono_celular
        self.email = email
        self.clave_acceso = clave_acceso
        self.estado_usuario = estado_usuario
        self.verificado = False

    # Getters
    def get_id_usuario(self):
        return self.id_usuario

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_dni(self):
        return self.dni

    def get_direccion(self):
        return self.direccion

    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento

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

    def get_clave_acceso(self):
        return self.clave_acceso

    def get_estado_usuario(self):
        return self.estado_usuario

    def get_verificado(self):
        return self.verificado

    # Setters
    def set_id_usuario(self, id_usuario):
        self.id_usuario = id_usuario

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_dni(self, dni):
        self.dni = dni

    def set_direccion(self, direccion):
        self.direccion = direccion

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

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

    def set_clave_acceso(self, clave_acceso):
        self.clave_acceso = clave_acceso

    def set_estado_usuario(self, estado_usuario):
        self.estado_usuario = estado_usuario

    # Método para enviar correo de verificación
    def enviar_correo_verificacion(self):
        try:
            # Configurar el servidor SMTP y el envío de correo
            server = smtplib.SMTP('smtp.example.com', 587)  # Cambiar a tu servidor SMTP
            server.starttls()
            server.login('tu_correo@example.com', 'tu_contraseña')  # Cambiar a tus credenciales

            # Crear y enviar el correo de verificación
            mensaje = MIMEText('Haz clic en este enlace para verificar tu correo.')
            mensaje['Subject'] = 'Verificación de correo electrónico'
            mensaje['From'] = 'tu_correo@example.com'
            mensaje['To'] = self.email

            server.sendmail('tu_correo@example.com', [self.email], mensaje.as_string())

            # Cerrar la conexión con el servidor SMTP
            server.quit()

            return True
        except Exception as e:
            print(f"Error al enviar el correo de verificación: {str(e)}")
            return False

    # Método para verificar si el correo es válido (puedes personalizar esta función)
    def email_valido(self):
        # Aquí puedes implementar una validación más robusta del correo electrónico
        # Para esta demostración, simplemente se considerará válido si contiene un "@" y un "."
        return "@" in self.email and "." in self.email

    def __str__(self):
        return f"Usuario: {self.nombre} {self.apellido}, DNI: {self.dni}, Estado: {self.estado_usuario}, Verificado: {self.verificado}"
