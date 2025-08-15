from inventario import Inventario  # Importa la clase Inventario definida previamente
import os

inventario1 = Inventario()  # Crea una instancia del inventario
archivo = "inventario_de_productos.xlsx"  # Nombre del archivo Excel donde se guardan los datos
hoja = "Inventario"  # Nombre de la hoja dentro del archivo

# Bucle principal del menú
while True:
    # Muestra las opciones disponibles
    print("\nMENÚ DE INVENTARIO")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")

    opcion = input("Seleccione una opción (1-6): ").strip()  # Solicita la opción al usuario

    if opcion == "1":
        # Permite añadir varios productos seguidos
        seguir = "si"
        for _ in range(100):  # Límite arbitrario para evitar bucles infinitos
            if seguir == "si":
                inventario1.añadir_producto()  # Añade un producto desde consola
                seguir = input("¿Desea añadir otro producto? (si/no): ").strip().lower()
            else:
                break
        inventario1.guardar_en_excel_xlsx(archivo)  # Guarda todos los productos en Excel
        os.startfile(archivo)  # Abre el archivo Excel automáticamente

    elif opcion == "2":
        # Elimina un producto por ID
        id_que_debe_eliminarse = input("Ingrese el ID a eliminar: ").strip()
        inventario1.eliminar_producto_en_excel(archivo, hoja, id_que_debe_eliminarse)
        os.startfile(archivo)  # Abre el archivo para mostrar el resultado

    elif opcion == "3":
        # Actualiza los datos de un producto por ID
        producto_con_id_a_actualizar = input("Ingrese el ID a actualizar: ").strip()
        inventario1.actualizar_producto_por_id(archivo, hoja, producto_con_id_a_actualizar)
        os.startfile(archivo)  # Abre el archivo para mostrar los cambios

    elif opcion == "4":
        # Busca productos por coincidencia en el nombre
        nombre_del_producto = input("Ingrese el nombre del producto: ").strip()
        inventario1.buscar_productos_por_nombre(archivo, hoja, nombre_del_producto)

    elif opcion == "5":
        # Muestra todos los productos registrados en el archivo Excel
        inventario1.mostrar_todos_los_productos(archivo, hoja)

    elif opcion == "6":
        # Sale del sistema
        print("Saliendo del sistema...")
        break

    else:
        # Si la opción no es válida
        print("Opción inválida. Intente nuevamente.")
