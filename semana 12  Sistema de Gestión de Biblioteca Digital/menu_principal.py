"""
menu_principal.py
Archivo principal para la interacción con el usuario.
Muestra el menú y gestiona las operaciones principales del sistema.
"""

from Biblioteca import Biblioteca
from Reporte import Reporte
from archivo import GuardarT
from usuario import Usuario
from libros import Libro

def mostrar_menu(registro_habilitado):
    """
    Muestra el menú principal del sistema.
    """
    print("\nMENÚ PRINCIPAL DEL SISTEMA")
    print("1. Agregar nuevo libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Mostrar usuarios registrados")
    print("5. Mostrar catálogo de libros")
    print("6. Buscar libros")
    print("7. Listar libros prestados por usuario")
    print("8. Mostrar estado general de libros")
    print("9. Generar reporte")
    print("10. Dar de baja usuario")
    print("0. Salir")

def ejecutar_menu():
    """
    Ejecuta el ciclo principal del menú y gestiona la interacción con el usuario.
    """
    biblioteca = Biblioteca()
    persistencia = GuardarT(biblioteca.usuarios, biblioteca.catalogo)
    persistencia.cargar_libros_desde_txt(Libro)
    persistencia.cargar_usuarios_desde_txt(Usuario)
    reporteador = Reporte(biblioteca.usuarios, biblioteca.catalogo)

    print("\nBienvenido al Sistema de Gestión Bibliotecaria")
    usuario_actual = None

    while True:
        respuesta = input("¿Usted posee un usuario registrado en el sistema? (si/no): ").strip().lower()
        if respuesta == "no":
            print("\nDebe registrar un usuario para continuar.")
            biblioteca.registro_de_usuario()
            persistencia.guardar_usuarios_txt()
            # Autenticación automática con el último usuario registrado
            usuario_actual = list(biblioteca.usuarios.values())[-1]
            print(f"¡Ingreso al sistema como '{usuario_actual.get_nombre()}' (ID: {usuario_actual.get_id()})!")
            break
        elif respuesta == "si":
            nombre = input("Ingrese su nombre de usuario: ").strip()
            id_usuario_actual = input("Ingrese su ID de usuario: ").strip()
            usuario_actual = biblioteca.usuarios.get(id_usuario_actual)
            if usuario_actual and usuario_actual.get_nombre() == nombre:
                print(f"¡Ingreso al sistema como '{nombre}' (ID: {id_usuario_actual})!")
                break
            else:
                print("Ups, ingreso algo mal. No se encuentra registrado.")
                volver = input("¿Desea volver a intentarlo? (sí/no): ").strip().lower()
                if volver == "sí":
                    continue
                else:
                    registrar = input("¿Quisiera registrarse para poder acceder? (sí/no): ").strip().lower()
                    if registrar == "sí":
                        biblioteca.registro_de_usuario()
                        persistencia.guardar_usuarios_txt()
                        usuario_actual = list(biblioteca.usuarios.values())[-1]
                        print(f"¡Ingreso al sistema como '{usuario_actual.get_nombre()}' (ID: {usuario_actual.get_id()})!")
                        break
                    else:
                        print("Saliendo del sistema. Que tenga un buen día.")
                        return
        else:
            print("Respuesta inválida. El sistema se cerrará por seguridad.")
            return

    # Menú principal, usando usuario_actual
    while True:
        mostrar_menu(True)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            while True:
                try:
                    titulo = input("Título del libro: ")
                    autor = input("Autor: ")
                    categoria = input("Categoría: ")
                    ISBN = input("ISBN: ")
                    libro = Libro(titulo, autor, categoria, ISBN)
                    biblioteca.agregar_libro(libro)
                    persistencia.guardar_libros_txt()
                    print("Libro agregado correctamente.")
                except Exception as e:
                    print(f"Error al agregar libro: {e}")

                print("\n¿Desea añadir otro libro?")
                print("1. Si")
                print("2. No, volver al menú")
                print("3. Salir del sistema")
                siguiente = input("Seleccione una opción: ")

                if siguiente == "1":
                    continue
                elif siguiente == "2":
                    break
                elif siguiente == "3":
                    persistencia.guardar_todo_txt()
                    print("Gracias por usar el sistema.")
                    return
                else:
                    print("Opción inválida. Regresando al menú.")
                    break

        elif opcion == "2":
            biblioteca.prestar_libro()
            persistencia.guardar_todo_txt()

        elif opcion == "3":
            biblioteca.devolucion_del_libro()
            persistencia.guardar_todo_txt()

        elif opcion == "4":
            biblioteca.mostrar_usuarios()

        elif opcion == "5":
            biblioteca.mostrar_libros_guardados()

        elif opcion == "6":
            biblioteca.buscar_libros()

        elif opcion == "7":
            biblioteca.listar_libros_prestados()

        elif opcion == "8":
            biblioteca.mostrar_estado_general_de_libros()

        elif opcion == "9":
            reporteador.menu_reportes()

        elif opcion == "10":
            # Solo permite dar de baja al usuario actual
            confirm = input(f"¿Seguro que desea darse de baja como '{usuario_actual.get_nombre()}' (ID: {usuario_actual.get_id()})? (sí/no): ").strip().lower()
            if confirm == "si":
                biblioteca.dar_de_baja_usuario()
                persistencia.guardar_todo_txt()
                print("Usuario dado de baja. Saliendo del sistema.")
                return
            else:
                print("Operación cancelada.")

        elif opcion == "0":
            persistencia.guardar_todo_txt()
            print("Gracias por usar el sistema.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    ejecutar_menu()