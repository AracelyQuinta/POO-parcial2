"""
archivo.py
Módulo para la persistencia de datos de la biblioteca digital.
Incluye funciones para guardar y cargar usuarios y libros desde archivos de texto.
"""

class GuardarT:
    def __init__(self, usuarios, catalogo):
        """
        Inicializa la clase con las colecciones de usuarios y libros.
        """
        self.usuarios = usuarios
        self.catalogo = catalogo

    def guardar_usuarios_txt(self):
        """
        Guarda los usuarios en un archivo de texto.
        Formato: ID;NOMBRE;LIBROS_PRESTADOS
        """
        with open("datos_guardados/usuarios.txt", "w", encoding="utf-8") as archivo:
            for usuario in self.usuarios.values():
                libros = ",".join([libro.ISBN for libro in usuario.lista_de_libros_prestados]) if hasattr(usuario, "lista_de_libros_prestados") else "Ninguno"
                archivo.write(f"{usuario.get_id()};{usuario.get_nombre()};{libros}\n")

    def guardar_libros_txt(self):
        """
        Guarda los libros en un archivo de texto.
        Formato: ISBN;TITULO;AUTOR;CATEGORIA
        """
        with open("datos_guardados/libros.txt", "w", encoding="utf-8") as archivo:
            for libro in self.catalogo.values():
                archivo.write(f"{libro.get_ISBN()};{libro.get_titulo()};{libro.get_autor()};{libro.get_categoria()}\n")

    def guardar_todo_txt(self):
        self.guardar_usuarios_txt()
        self.guardar_libros_txt()

    def cargar_libros_desde_txt(self, clase_libro):
        try:
            with open("datos_guardados/libros.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(";")
                    if len(datos) == 4:
                        libro = clase_libro(*datos)
                        self.catalogo.append(libro)
        except FileNotFoundError:
            pass  # No mostrar mensaje

    def cargar_usuarios_desde_txt(self, clase_usuario):
        try:
            with open("datos_guardados/usuarios.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    # Ignorar encabezados y líneas que no contienen datos
                    if linea.startswith("|"):
                        datos = linea.strip().split("|")
                        # El formato es: | ID | NOMBRE | LIBROS PRESTADOS |
                        if len(datos) >= 2 and datos[0] != "ID":
                            id_usuario = datos[0]
                            nombre = datos[1]
                            usuario = clase_usuario(nombre, id_usuario)
                            self.usuarios[id_usuario] = usuario
        except FileNotFoundError:
            pass  # No mostrar mensaje



