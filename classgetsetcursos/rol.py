class Rol:
    def __init__(self, id_rol, nombre_rol, descripcion_rol):
        self.id_rol = id_rol
        self.nombre_rol = nombre_rol
        self.descripcion_rol = descripcion_rol

   
    def get_id_rol(self):
        return self.id_rol

    def get_nombre_rol(self):
        return self.nombre_rol

    def get_descripcion_rol(self):
        return self.descripcion_rol

    
    def set_id_rol(self, id_rol):
        self.id_rol = id_rol

    def set_nombre_rol(self, nombre_rol):
        self.nombre_rol = nombre_rol

    def set_descripcion_rol(self, descripcion_rol):
        self.descripcion_rol = descripcion_rol

    def __str__(self):
        return f"Rol: {self.nombre_rol}, Descripción: {self.descripcion_rol}"
