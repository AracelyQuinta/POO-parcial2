"""
libros.py
Define la clase Libro para representar los libros de la biblioteca.
"""

class Libro:
    def __init__(self, titulo, autor, categoria, ISBN):
        # Tupla inmutable para título y autor
        self.info = (titulo, autor)
        self.categoria = categoria
        self.ISBN = ISBN

    def get_titulo(self):
        """Devuelve el título del libro."""
        return self.info[0]

    def get_autor(self):
        """Devuelve el autor del libro."""
        return self.info[1]

    def get_categoria(self):
        """Devuelve la categoría del libro."""
        return self.categoria

    def get_ISBN(self):
        """Devuelve el ISBN del libro."""
        return self.ISBN

    def set_categoria(self, categoria) :
        self.categoria = categoria

    def set_ISBN(self, ISBN) :
        self.ISBN = ISBN

    def modo_de_presentar_el_libro(self):
        print("SELECCIONE UNA FORMA DE PRESENTACIÓN:")
        print(" 1.- Horizontal")
        print(" 2.- Vertical")
        try:
            resultado_modo = int(input("¿Cómo desea que le muestre la información? (1 o 2): "))
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")
            return

        if resultado_modo == 1:
            encabezado = "| {:<30} | {:<20} | {:<15} | {:<13} |".format("TITULO", "AUTOR", "CATEGORIA", "ISBN")
            contenido = "| {:<30} | {:<20} | {:<15} | {:<13} |".format(self.titulo, self.autor, self.categoria, self.ISBN)
            print(encabezado)
            print(contenido)
        elif resultado_modo == 2:
            print("Información del libro")
            print("*" * 30)
            print(f"Título   : {self.titulo}")
            print(f"Autor    : {self.autor}")
            print(f"Categoría: {self.categoria}")
            print(f"ISBN     : {self.ISBN}")
        else:
            print("Opción no válida. Seleccione 1 o 2.")

    def set_observacion(self, texto):
        self.observacion = texto

    def get_observacion(self):
        return self.observacion

