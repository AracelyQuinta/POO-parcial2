"""
usuario.py
Define la clase Usuario para representar los usuarios de la biblioteca.
"""

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id = id_usuario
        self.lista_de_libros_prestados = []

    def get_nombre(self):
        """Devuelve el nombre del usuario."""
        return self.nombre

    def get_id(self):
        """Devuelve el ID del usuario."""
        return self.id

    def lista_de_libros(self):
        return self.lista_de_libros_prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.ID})"




