"""
Reporte.py
Define la clase Reporte para generar reportes de la biblioteca.
"""

class Reporte:
    def __init__(self, usuarios, catalogo):
        """
        Inicializa la clase con las colecciones de usuarios y libros.
        """
        self.usuarios = usuarios
        self.catalogo = catalogo
        self.historial_exportaciones = []

    def cargar_historial_exportaciones(self):
        try:
            with open("historial_exportaciones.txt", "r", encoding="utf-8") as f:
                self.historial_exportaciones = [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            self.historial_exportaciones = []

    def menu_reportes(self):
        """
        Muestra el menú de reportes y gestiona la generación de reportes.
        """
        print("\nMENÚ DE REPORTES")
        print("1. Reporte de libros prestados por usuario")
        print("2. Reporte general del catálogo")
        print("3. Reporte de libros con observaciones")
        print("4. Ver historial de exportaciones")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_usuario = input("Ingrese el ID del usuario: ")
            self.exportar_libros_prestados(id_usuario)
        elif opcion == "2":
            self.exportar_catalogo()
        elif opcion == "3":
            self.exportar_observaciones()
        elif opcion == "4":
            self.ver_historial_exportaciones()
        else:
            print(" Opción inválida.")

    def generar_reporte_libros_prestados(self, id_usuario):
        if id_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return

        usuario = self.usuarios[id_usuario]
        libros = usuario.lista_de_libros_prestados

        if not libros:
            print(f"El usuario '{usuario.get_nombre()}' no tiene libros prestados.")
            return

        print(f"\nREPORTE DE LIBROS PRESTADOS - Usuario: {usuario.get_nombre()} (ID: {id_usuario})")
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

    def generar_reporte_catalogo(self):
        print("\nREPORTE GENERAL DEL CATÁLOGO")
        print("-" * 90)
        print("| {:<30} | {:<20} | {:<15} | {:<13} |".format("TÍTULO", "AUTOR", "CATEGORÍA", "ISBN"))
        print("-" * 90)
        for libro in self.catalogo.values():
            print("| {:<30} | {:<20} | {:<15} | {:<13} |".format(
                libro.get_titulo(),
                libro.get_autor(),
                libro.get_categoria(),
                libro.get_ISBN()
            ))
        print("-" * 90)

    def generar_reporte_observaciones(self):
        print("\nREPORTE DE OBSERVACIONES DE LIBROS")
        print("-" * 100)
        print("| {:<30} | {:<20} | {:<15} | {:<13} | {:<15} |".format("TÍTULO", "AUTOR", "CATEGORÍA", "ISBN",
                                                                      "OBSERVACIÓN"))
        print("-" * 100)
        for libro in self.catalogo.values():
            observacion = libro.get_observacion() if hasattr(libro, "observacion") else ""
            if observacion:
                print("| {:<30} | {:<20} | {:<15} | {:<13} | {:<15} |".format(
                    libro.get_titulo(),
                    libro.get_autor(),
                    libro.get_categoria(),
                    libro.get_ISBN(),
                    observacion
                ))
        print("-" * 100)

    def exportar_libros_prestados_por_todos(self):
        import os
        os.makedirs("reportes", exist_ok=True)

        nombre_archivo = os.path.join("reportes", "reporte_libros_prestados_todos.txt")
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("REPORTE DE TODOS LOS LIBROS PRESTADOS\n")
            archivo.write("-" * 90 + "\n")
            archivo.write(
                "| {:<30} | {:<20} | {:<15} | {:<13} | {:<10} |\n".format("TÍTULO", "AUTOR", "CATEGORÍA", "ISBN",
                                                                          "USUARIO"))
            archivo.write("-" * 90 + "\n")

            for usuario in self.usuarios.values():
                for libro in usuario.lista_de_libros_prestados:
                    archivo.write("| {:<30} | {:<20} | {:<15} | {:<13} | {:<10} |\n".format(
                        libro.get_titulo(),
                        libro.get_autor(),
                        libro.get_categoria(),
                        libro.get_ISBN(),
                        usuario.get_id()
                    ))

            archivo.write("-" * 90 + "\n")

        def registrar_historial(self, tipo, archivo):
            from datetime import datetime
            registro = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {tipo} → {archivo}"
            self.historial_exportaciones.append(registro)

            # Guardar en archivo persistente
            with open("historial_exportaciones.txt", "a", encoding="utf-8") as f:
                f.write(registro + "\n")

    def exportar_catalogo(self):
        nombre_archivo = "reporte_catalogo.txt"
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write("REPORTE GENERAL DEL CATÁLOGO\n")
            f.write("-" * 90 + "\n")
            f.write("| {:<30} | {:<20} | {:<15} | {:<13} |\n".format("TÍTULO", "AUTOR", "CATEGORÍA", "ISBN"))
            f.write("-" * 90 + "\n")
            for libro in self.catalogo.values():
                f.write("| {:<30} | {:<20} | {:<15} | {:<13} |\n".format(
                    libro.get_titulo(), libro.get_autor(), libro.get_categoria(), libro.get_ISBN()
                ))
            f.write("-" * 90 + "\n")

        self.registrar_historial("Catálogo general", nombre_archivo)
        print(f" Reporte generado: {nombre_archivo}")

    def exportar_observaciones(self):
        nombre_archivo = "reporte_observaciones.txt"
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write("REPORTE DE OBSERVACIONES DE LIBROS\n")
            f.write("-" * 100 + "\n")
            f.write("| {:<30} | {:<20} | {:<15} | {:<13} | {:<15} |\n".format("TÍTULO", "AUTOR", "CATEGORÍA", "ISBN",
                                                                              "OBSERVACIÓN"))
            f.write("-" * 100 + "\n")
            for libro in self.catalogo.values():
                observacion = libro.get_observacion() if hasattr(libro, "observacion") else ""
                if observacion:
                    f.write("| {:<30} | {:<20} | {:<15} | {:<13} | {:<15} |\n".format(
                        libro.get_titulo(), libro.get_autor(), libro.get_categoria(), libro.get_ISBN(), observacion
                    ))
            f.write("-" * 100 + "\n")

        self.registrar_historial("Libros con observaciones", nombre_archivo)
        print(f" Reporte generado: {nombre_archivo}")

    def registrar_historial(self, tipo, archivo):
        from datetime import datetime
        registro = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {tipo} → {archivo}"
        self.historial_exportaciones.append(registro)

    def ver_historial_exportaciones(self):
        print("\nHISTORIAL DE EXPORTACIONES")
        if not self.historial_exportaciones:
            print("No hay exportaciones registradas.")
        else:
            for registro in self.historial_exportaciones:
                print(f"- {registro}")

