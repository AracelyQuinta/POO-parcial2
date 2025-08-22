# Importa las clases necesarias para manejar archivos, verificar documentos y gestionar el inventario
from manipulacion_de_archivo import Archivo
from verificador_de_documento import verificar_o_crear_excel
from inventario import Inventario
import os  # Para operaciones con el sistema de archivos (como abrir Excel)

# Función principal que ejecuta el menú del sistema
def menu():
    # Define el nombre del archivo Excel y la hoja donde se almacenan los productos
    nombre_archivo = "inventario_de_productos.xlsx"
    hoja = "Inventario"

    # Verifica si el archivo y la hoja existen; si no, los crea con encabezado
    verificar_o_crear_excel(nombre_archivo, hoja)

    # Crea una instancia de la clase Archivo y carga los productos desde Excel
    archivo = Archivo()
    archivo.cargar_desde_excel(nombre_archivo, hoja)

    # Crea una instancia de Inventario y sincroniza los productos en memoria
    inventario1 = Inventario()
    inventario1.productos = archivo.productos

    # Bucle principal del menú
    while True:
        # Muestra las opciones disponibles al usuario
        print("\nMENÚ DE INVENTARIO")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        # Solicita al usuario que seleccione una opción
        opcion = input("Seleccione una opción (1-6): ").strip()

        # Opción 1: Añadir uno o varios productos
        if opcion == "1":
            seguir = "si"
            while seguir == "si":
                inventario1.añadir_producto()  # Añade un producto desde consola
                seguir = input("¿Desea añadir otro producto? (si/no): ").strip().lower()

            # Actualiza los productos en el objeto Archivo y guarda en Excel
            archivo.productos = inventario1.productos
            archivo.guardar_en_excel_xlsx(nombre_archivo)

            # Abre el archivo Excel automáticamente
            os.startfile(nombre_archivo)

        # Opción 2: Eliminar un producto por ID
        elif opcion == "2":
            id_que_debe_eliminarse = input("Ingrese el ID a eliminar: ").strip()
            inventario1.eliminar_producto_en_excel(nombre_archivo, hoja, id_que_debe_eliminarse)

        # Opción 3: Actualizar los datos de un producto por ID
        elif opcion == "3":
            producto_con_id_a_actualizar = input("Ingrese el ID a actualizar: ").strip()
            inventario1.actualizar_producto_por_id(nombre_archivo, hoja, producto_con_id_a_actualizar)

        # Opción 4: Buscar productos por coincidencia en el nombre
        elif opcion == "4":
            nombre_del_producto = input("Ingrese el nombre del producto: ").strip()
            inventario1.buscar_productos_por_nombre(nombre_archivo, hoja, nombre_del_producto)

        # Opción 5: Mostrar todos los productos registrados en el archivo
        elif opcion == "5":
            inventario1.mostrar_todos_los_productos(nombre_archivo, hoja)

        # Opción 6: Salir del sistema
        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        # Si la opción ingresada no es válida
        else:
            print("Opción inválida. Intente nuevamente.")

# Punto de entrada del programa
if __name__ == "__main__":
    menu()
