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
    print("9. Generar reportes")
    print("10. Guardar datos manualmente")
    print("11. Dar de baja usuario")
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
    registro_habilitado = False

    while True:
        respuesta = input("¿Usted posee un usuario registrado en el sistema? (sí/no): ").strip().lower()
        if respuesta == "no":
            print("\nDebe registrar un usuario para continuar.")
            biblioteca.registro_de_usuario()
            persistencia.guardar_usuarios_txt()
            print("Usuario registrado correctamente. Accediendo al sistema...")
            registro_habilitado = True
            break
        elif respuesta == "sí":
            nombre = input("Ingrese su nombre de usuario: ").strip()
            id_usuario = input("Ingrese su ID de usuario: ").strip()
            usuario_encontrado = any(
                u.get_nombre() == nombre and u.get_id() == id_usuario
                for u in biblioteca.usuarios.values()
            )
            if usuario_encontrado:
                print("Usuario encontrado. Accediendo al sistema...")
                registro_habilitado = True
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
                        print("Usuario registrado correctamente. Accediendo al sistema...")
                        registro_habilitado = True
                        break
                    else:
                        print("Saliendo del sistema. Que tenga un buen día.")
                        return
        else:
            print("Respuesta inválida. El sistema se cerrará por seguridad.")
            return

    while True:
        mostrar_menu(registro_habilitado)
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
                print("1. Sí")
                print("2. No, volver al menú")
                print("3. Salir del sistema")
                siguiente = input("Seleccione una opción: ")

                if siguiente == "1":
                    continue
                elif siguiente == "2":
                    break
                elif siguiente == "3":
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
            biblioteca.dar_de_baja_usuario()
            persistencia.guardar_todo_txt()

        elif opcion == "0":
            persistencia.guardar_todo_txt()  # Guarda todo antes de salir
            print("Gracias por usar el sistema.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    ejecutar_menu()