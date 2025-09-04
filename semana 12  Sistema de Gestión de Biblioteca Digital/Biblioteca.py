from libros import Libro
from usuario import Usuario

class Biblioteca:
    def __init__(self):
        # Diccionario de libros: ISBN -> Libro
        self.catalogo = {}
        # Diccionario de usuarios: ID -> Usuario
        self.usuarios = {}
        # Conjunto para asegurar IDs únicos
        self.ids_registrados = set()
        # Contador para generar nuevos IDs
        self.contador_id = 1

    def agregar_libro(self, libro):
        """
        Añade un libro al catálogo si el ISBN no existe.
        """
        ISBN = libro.ISBN
        if ISBN in self.catalogo:
            # El libro ya existe, no se añade
            pass
        else:
            # Añadir libro al catálogo
            self.catalogo[ISBN] = libro

    def mostrar_libros_guardados(self):
        """
        Muestra todos los libros almacenados en el catálogo.
        """
        if self.catalogo:
            # Imprimir información de cada libro
            for libro in self.catalogo.values():
                print(f"{libro.get_titulo()} - {libro.get_autor()} - {libro.get_categoria()} - {libro.get_ISBN()}")
        else:
            print("No hay libros en el catálogo.")

    def registro_de_usuario(self):
        """
        Registra un nuevo usuario con un ID único.
        """
        nombre = input("Ingrese el nombre del usuario: ")
        while True:
            nuevo_id = f"user{self.contador_id}"
            if nuevo_id not in self.ids_registrados:
                break
            self.contador_id += 1
        self.ids_registrados.add(nuevo_id)
        nuevo_usuario = Usuario(nombre, nuevo_id)
        self.usuarios[nuevo_id] = nuevo_usuario
        print(f"Usuario '{nombre}' registrado exitosamente con ID '{nuevo_id}'.")

    def prestar_libro(self):
        """
        Permite a un usuario pedir prestado uno o más libros.
        """
        nombre_usuario = input("Ingrese su nombre: ")
        id_usuario = input("Ingrese su ID de usuario: ")
        if id_usuario not in self.usuarios or self.usuarios[id_usuario].get_nombre() != nombre_usuario:
            print("Usuario no encontrado. Verifique sus datos.")
            return
        usuario = self.usuarios[id_usuario]
        while True:
            # Mostrar libros que ya posee
            print(f"Libros que ya posee: {', '.join([libro.get_titulo() for libro in usuario.lista_de_libros_prestados]) if usuario.lista_de_libros_prestados else 'Ninguno'}")
            # Buscar libro por título, autor, categoría o ISBN
            print("\n¿De qué forma desea buscar el libro?")
            print("1. Por el nombre del libro")
            print("2. Por el autor del libro")
            print("3. Por la categoría del libro")
            print("4. Por el ISBN del libro")

            try:
                opcion = int(input("Seleccione una opción: "))
            except ValueError:
                print("Opción inválida.")
                continue

            libro_encontrado = None

            if opcion == 1:
                titulo = input("Ingrese el título del libro: ")
                for libro in self.catalogo.values():
                    if libro.get_titulo().lower() == titulo.lower():
                        libro_encontrado = libro
                        break
            elif opcion == 2:
                autor = input("Ingrese el autor del libro: ")
                for libro in self.catalogo.values():
                    if libro.get_autor().lower() == autor.lower():
                        libro_encontrado = libro
                        break
            elif opcion == 3:
                categoria = input("Ingrese la categoría del libro: ")
                for libro in self.catalogo.values():
                    if libro.get_categoria().lower() == categoria.lower():
                        libro_encontrado = libro
                        break
            elif opcion == 4:
                isbn = input("Ingrese el ISBN del libro: ")
                libro_encontrado = self.catalogo.get(isbn)
            else:
                print("Opción inválida.")
                continue

            if not libro_encontrado:
                print("No tenemos ese libro.")
            else:
                # Verificar si el libro ya fue prestado
                if libro_encontrado in usuario.lista_de_libros_prestados:
                    print("Ya tienes este libro prestado.")
                else:
                    usuario.lista_de_libros_prestados.append(libro_encontrado)
                    print(f"Libro '{libro_encontrado.get_titulo()}' prestado a '{usuario.get_nombre()}'.")

            otro = input("\n¿Desea pedir prestado otro libro? (sí/no): ").strip().lower()
            if otro != "sí":
                break

    def devolucion_del_libro(self):
        id_usuario = input("Ingrese el ID del usuario: ")
        if id_usuario not in self.usuarios:
            print(" Usuario no registrado.")
            return

        usuario = self.usuarios[id_usuario]
        libros_prestados = usuario.lista_de_libros_prestados

        if not libros_prestados:
            print(" El usuario no tiene libros prestados.")
            return

        print("\n Libros prestados por el usuario:")
        print("-" * 90)
        print("| {:<3} | {:<30} | {:<20} | {:<15} | {:<13} |".format("N°", "TÍTULO", "AUTOR", "CATEGORÍA", "ISBN"))
        print("-" * 90)
        for i, libro in enumerate(libros_prestados, start=1):
            print("| {:<3} | {:<30} | {:<20} | {:<15} | {:<13} |".format(
                i,
                libro.get_titulo(),
                libro.get_autor(),
                libro.get_categoria(),
                libro.get_ISBN()
            ))
        print("-" * 90)

        try:
            opcion = int(input("Ingrese el número del libro que desea devolver: "))
            if 1 <= opcion <= len(libros_prestados):
                libro_devuelto = libros_prestados.pop(opcion - 1)
                observacion = input("Ingrese una observación sobre el estado del libro (opcional): ")
                libro_devuelto.set_observacion(observacion)

                print("\n Libro devuelto correctamente. Detalles:")
                print("-" * 90)
                print("| {:<30} | {:<20} | {:<15} | {:<13} |".format("TÍTULO", "AUTOR", "CATEGORÍA", "ISBN"))
                print("-" * 90)
                print("| {:<30} | {:<20} | {:<15} | {:<13} |".format(
                    libro_devuelto.get_titulo(),
                    libro_devuelto.get_autor(),
                    libro_devuelto.get_categoria(),
                    libro_devuelto.get_ISBN()
                ))
                print("-" * 90)
                if observacion:
                    print(f"Observación registrada: {observacion}")
            else:
                print("Opción inválida.")
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")

    def buscar_libros(self):
        print("\n¿Cómo desea buscar el libro?")
        print("1. Por título")
        print("2. Por autor")
        print("3. Por categoría")
        opcion = input("Ingrese el número de su preferencia: ")

        criterio = input("Ingrese el texto a buscar: ").lower()
        resultados = []

        for libro in self.catalogo.values():
            if opcion == "1" and criterio in libro.get_titulo().lower():
                resultados.append(libro)
            elif opcion == "2" and criterio in libro.get_autor().lower():
                resultados.append(libro)
            elif opcion == "3" and criterio in libro.get_categoria().lower():
                resultados.append(libro)

        if resultados:
            print("\n Libros encontrados:")
            print("-" * 90)
            print("| {:<30} | {:<20} | {:<15} | {:<13} |".format("TÍTULO", "AUTOR", "CATEGORÍA", "ISBN"))
            print("-" * 90)
            for libro in resultados:
                print("| {:<30} | {:<20} | {:<15} | {:<13} |".format(
                    libro.get_titulo(),
                    libro.get_autor(),
                    libro.get_categoria(),
                    libro.get_ISBN()
                ))
            print("-" * 90)
        else:
            print(" No se encontraron libros que coincidan con el criterio.")

    def listar_libros_prestados(self):
        id_usuario = input("Ingrese el ID del usuario: ")
        if id_usuario not in self.usuarios:
            print(" Usuario no registrado.")
            return

        usuario = self.usuarios[id_usuario]
        libros = usuario.lista_de_libros_prestados

        if not libros:
            print(f" El usuario '{usuario.get_nombre()}' no tiene libros prestados.")
            return

        print(f"\nLibros prestados a '{usuario.get_nombre()}':")
        print("-" * 90)
        print("| {:<30} | {:<20} | {:<15} | {:<13} |".format("TÍTULO", "AUTOR", "CATEGORÍA", "ISBN"))
        print("-" * 90)
        for libro in libros:
            print("| {:<30} | {:<20} | {:<15} | {:<13} |".format(
                libro.get_titulo(),
                libro.get_autor(),
                libro.get_categoria(),
                libro.get_ISBN()
            ))
        print("-" * 90)

    def mostrar_estado_general_de_libros(self):
        print("\n ESTADO GENERAL DE LOS LIBROS EN LA BIBLIOTECA")

        # Libros prestados
        libros_prestados = {}
        for usuario in self.usuarios.values():
            for libro in usuario.lista_de_libros_prestados:
                libros_prestados[libro.get_ISBN()] = usuario

        # Mostrar libros disponibles
        print("\n LIBROS DISPONIBLES PARA PRÉSTAMO:")
        disponibles = [libro for ISBN, libro in self.catalogo.items() if ISBN not in libros_prestados]
        if disponibles:
            print("-" * 90)
            print("| {:<30} | {:<20} | {:<15} | {:<13} |".format("TÍTULO", "AUTOR", "CATEGORÍA", "ISBN"))
            print("-" * 90)
            for libro in disponibles:
                print("| {:<30} | {:<20} | {:<15} | {:<13} |".format(
                    libro.get_titulo(), libro.get_autor(), libro.get_categoria(), libro.get_ISBN()
                ))
            print("-" * 90)
        else:
            print(" No hay libros disponibles actualmente.")

        # Mostrar libros prestados
        print("\n LIBROS ACTUALMENTE PRESTADOS:")
        if libros_prestados:
            print("-" * 110)
            print("| {:<30} | {:<20} | {:<15} | {:<13} | {:<25} |".format("TÍTULO", "AUTOR", "CATEGORÍA", "ISBN",
                                                                          "USUARIO"))
            print("-" * 110)
            for ISBN, usuario in libros_prestados.items():
                libro = self.catalogo[ISBN]
                nombre_usuario = usuario.get_nombre()
                print("| {:<30} | {:<20} | {:<15} | {:<13} | {:<25} |".format(
                    libro.get_titulo(), libro.get_autor(), libro.get_categoria(), ISBN,
                    f"{nombre_usuario} ({usuario.get_id()})"
                ))
            print("-" * 110)
        else:
            print(" No hay libros prestados actualmente.")
