class Clases:
    def __init__(self, id_clase, fecha, titulo, contenido, url_drive, id_curso):
        self.id_clase = id_clase
        self.fecha = fecha
        self.titulo = titulo
        self.contenido = contenido
        self.url_drive = url_drive
        self.id_curso = id_curso

    def get_id_clase(self):
        return self.id_clase

    def get_fecha(self):
        return self.fecha

    def get_titulo(self):
        return self.titulo

    def get_contenido(self):
        return self.contenido

    def get_url_drive(self):
        return self.url_drive

    def get_id_curso(self):
        return self.id_curso

    def set_id_clase(self, id_clase):
        self.id_clase = id_clase

    def set_fecha(self, fecha):
        self.fecha = fecha

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_contenido(self, contenido):
        self.contenido = contenido

    def set_url_drive(self, url_drive):
        self.url_drive = url_drive

    def set_id_curso(self, id_curso):
        self.id_curso = id_curso

    def __str__(self):
        return f"Clase: {self.titulo}, Fecha: {self.fecha}, Curso: {self.id_curso}"
