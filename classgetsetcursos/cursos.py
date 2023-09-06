class Cursos:
    def __init__(self, id_curso, fecha_comienzo, titulo, descripcion, objetivos, programa, costo, duracion_meses, foto, estado_curso, categoria):
        self.id_curso = id_curso
        self.fecha_comienzo = fecha_comienzo
        self.titulo = titulo
        self.descripcion = descripcion
        self.objetivos = objetivos
        self.programa = programa
        self.costo = costo
        self.duracion_meses = duracion_meses
        self.foto = foto
        self.estado_curso = estado_curso
        self.categoria = categoria

    def get_id_curso(self):
        return self.id_curso

    def get_fecha_comienzo(self):
        return self.fecha_comienzo

    def get_titulo(self):
        return self.titulo

    def get_descripcion(self):
        return self.descripcion

    def get_objetivos(self):
        return self.objetivos

    def get_programa(self):
        return self.programa

    def get_costo(self):
        return self.costo

    def get_duracion_meses(self):
        return self.duracion_meses

    def get_foto(self):
        return self.foto

    def get_estado_curso(self):
        return self.estado_curso

    def get_categoria(self):
        return self.categoria

    def set_id_curso(self, id_curso):
        self.id_curso = id_curso

    def set_fecha_comienzo(self, fecha_comienzo):
        self.fecha_comienzo = fecha_comienzo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def set_objetivos(self, objetivos):
        self.objetivos = objetivos

    def set_programa(self, programa):
        self.programa = programa

    def set_costo(self, costo):
        self.costo = costo

    def set_duracion_meses(self, duracion_meses):
        self.duracion_meses = duracion_meses

    def set_foto(self, foto):
        self.foto = foto

    def set_estado_curso(self, estado_curso):
        self.estado_curso = estado_curso

    def set_categoria(self, categoria):
        self.categoria = categoria

    def __str__(self):
        return f"Curso: {self.titulo}, Categoría: {self.categoria}, Duración: {self.duracion_meses} meses, Estado: {self.estado_curso}"
