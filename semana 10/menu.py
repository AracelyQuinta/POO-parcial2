
from manipulacion_de_archivo import Archivo
from verificador_de_documento import verificar_o_crear_excel
from inventario import Inventario  # Importa la clase Inventario definida previamente
import os

def menu():
    archivo = Archivo()
    archivo.cargar_desde_excel(nombre_archivo, hoja)

    inventario1 = Inventario()
    inventario1.productos = archivo.productos

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
            archivo.productos = inventario1.productos  # Actualiza productos en el objeto Archivo
            archivo.guardar_en_excel_xlsx(nombre_archivo)  # Guarda en el archivo Excel
            os.startfile(nombre_archivo)  # Abre el archivo Excel
        elif opcion == "2":
            # Elimina un producto por ID
            id_que_debe_eliminarse = input("Ingrese el ID a eliminar: ").strip()
            inventario1.eliminar_producto_en_excel(nombre_archivo, hoja, id_que_debe_eliminarse)

        elif opcion == "3":
            # Actualiza los datos de un producto por ID
            producto_con_id_a_actualizar = input("Ingrese el ID a actualizar: ").strip()
            inventario1.actualizar_producto_por_id(nombre_archivo, hoja, producto_con_id_a_actualizar)
        elif opcion == "4":
            # Busca productos por coincidencia en el nombre
            nombre_del_producto = input("Ingrese el nombre del producto: ").strip()
            inventario1.buscar_productos_por_nombre(nombre_archivo, hoja, nombre_del_producto)

        elif opcion == "5":
            print("Abriendo el archivo Excel...")
            if os.path.exists(nombre_archivo):
                os.startfile(nombre_archivo)
            else:
                print(f"No se encontró el archivo '{nombre_archivo}'.")

        elif opcion == "6":
            # Sale del sistema
            print("Saliendo del sistema...")
            break
        else:
            # Si la opción no es válida
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    nombre_archivo = "inventario_de_productos.xlsx"  # Nombre del archivo Excel donde se guardan los datos
    hoja = "Inventario"
    verificar_o_crear_excel(nombre_archivo, hoja)
    menu()