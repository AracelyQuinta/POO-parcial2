
from inventario import Inventario
import os
inventario1 = Inventario()
archivo = "inventario_de_productos.xlsx"
hoja = "Inventario"

while True:
    print("\nMENÚ DE INVENTARIO")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")

    opcion = input("Seleccione una opción (1-6): ").strip()

    if opcion == "1":
        seguir = "si"
        for _ in range(100):
            if seguir == "si":
                inventario1.añadir_producto()
                seguir = input("¿Desea añadir otro producto? (si/no): ").strip().lower()
            else:
                break
        inventario1.guardar_en_excel_xlsx(archivo)
        os.startfile(archivo)

    elif opcion == "2":
        id_que_debe_eliminarse = input("Ingrese el ID a eliminar: ").strip()
        inventario1.eliminar_producto_en_excel(archivo, hoja, id_que_debe_eliminarse)
        os.startfile(archivo)

    elif opcion == "3":
        producto_con_id_a_actualizar = input("Ingrese el ID a actualizar: ").strip()
        inventario1.actualizar_producto_por_id(archivo, hoja, producto_con_id_a_actualizar)
        os.startfile(archivo)

    elif opcion == "4":
        nombre_del_producto = input("Ingrese el nombre del producto: ").strip()
        inventario1.buscar_productos_por_nombre(archivo, hoja, nombre_del_producto)

    elif opcion == "5":
        inventario1.mostrar_todos_los_productos(archivo, hoja)

    elif opcion == "6":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida. Intente nuevamente.")
