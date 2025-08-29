# Importa las clases necesarias desde otros módulos
from producto import Producto         # Clase que representa un producto individual
from inventario import Inventario     # Clase que gestiona la colección de productos

# Función principal que ejecuta el menú interactivo
def menu() -> None:
    inventario = Inventario()        # Crea una instancia del inventario

    while True:                      # Bucle infinito hasta que el usuario decida salir
        # Muestra el menú de opciones
        print("Sistema de Gestión de Inventarios")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Recargar desde archivo")
        print("7. Salir")
        opcion = input("Seleccione una opción: ").strip()  # Captura la opción del usuario

        # Opción 1: Añadir producto al inventario
        if opcion == "1":
            try:
                # Solicita los datos del producto
                idp = input("ID: ").strip()
                nombre = input("Nombre: ").strip()
                cantidad = int(input("Cantidad (entero): ").strip())
                precio = float(input("Precio (decimal): ").strip())
                # Crea el producto y lo añade al inventario
                inventario.anadir_producto(Producto(idp, nombre, cantidad, precio))
            except ValueError:
                # Maneja errores de conversión numérica
                print("Entrada inválida: cantidad debe ser entero y precio decimal.")
            input("\nEnter para continuar...")  # Pausa antes de volver al menú

        # Opción 2: Eliminar producto por ID
        elif opcion == "2":
            idp = input("ID a eliminar: ").strip()
            inventario.eliminar_producto(idp)
            input("\nEnter para continuar...")

        # Opción 3: Actualizar cantidad y/o precio de un producto
        elif opcion == "3":
            idp = input("ID a actualizar: ").strip()
            txt_cant = input("Nueva cantidad (vacío para no cambiar): ").strip()
            txt_prec = input("Nuevo precio (vacío para no cambiar): ").strip()
            try:
                # Convierte los valores si se proporcionan
                cantidad = int(txt_cant) if txt_cant else None
                precio = float(txt_prec) if txt_prec else None
                inventario.actualizar_producto(idp, cantidad, precio)
            except ValueError:
                print("Entrada inválida: cantidad debe ser entero y precio decimal.")
            input("\nEnter para continuar...")

        # Opción 4: Buscar productos por nombre (coincidencia parcial)
        elif opcion == "4":
            nombre = input("Buscar por nombre (coincidencia parcial): ").strip()
            resultados = inventario.buscar_por_nombre(nombre)
            inventario.imprimir_tabla(resultados)
            input("\nEnter para continuar...")

        # Opción 5: Mostrar todos los productos registrados
        elif opcion == "5":
            productos = inventario.obtener_todos()
            inventario.imprimir_tabla(productos)
            input("\nEnter para continuar...")

        # Opción 6: Recargar inventario desde archivo externo
        elif opcion == "6":
            inventario.recargar()
            input("\nEnter para continuar...")

        # Opción 7: Salir del programa
        elif opcion == "7":
            print("Saliendo...")
            break

        # Manejo de opción inválida
        else:
            print("Opción no válida.")
            input("\nEnter para continuar...")

# Punto de entrada del programa
if __name__ == "__main__":
    menu()

