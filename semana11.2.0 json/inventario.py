# Importa tipos necesarios y clases externas
from typing import List, Optional           # Para listas tipadas y parámetros opcionales
from producto import Producto              # Clase que representa un producto
from archivo import GestionArchivo         # Clase que maneja la persistencia en archivo

class Inventario:
    """
    Clase que encapsula la lógica de negocio del sistema de inventario.
    Delegamos la persistencia (cargar/guardar) en la clase GestionArchivo.
    """

    def __init__(self):
        # Inicializa el gestor de archivo y carga los productos existentes
        self.archivo = GestionArchivo()
        self.lproducto: List[Producto] = self.archivo.cargar()

    # -------------------------------
    # Operaciones sobre el inventario
    # -------------------------------

    def anadir_producto(self, p: Producto) -> None:
        # Verifica si el ID ya existe para evitar duplicados
        if any(x.get_id() == p.get_id() for x in self.lproducto):
            print("El ID ya existe. No se añadió el producto.")
            return

        # Añade el producto a la lista
        self.lproducto.append(p)

        # Intenta guardar en archivo
        if self.archivo.guardar(self.lproducto):
            print("Producto añadido y guardado en archivo.")
        else:
            print("No se pudo guardar en archivo. El producto permanece en memoria.")

    def eliminar_producto(self, id_producto: str) -> None:
        # Guarda el tamaño original para verificar si hubo eliminación
        original = len(self.lproducto)

        # Filtra la lista excluyendo el producto con el ID dado
        self.lproducto = [p for p in self.lproducto if p.get_id() != id_producto]

        # Si no se eliminó nada, el producto no existía
        if len(self.lproducto) == original:
            print("Producto no encontrado.")
            return

        # Intenta guardar los cambios
        if self.archivo.guardar(self.lproducto):
            print("Producto eliminado y guardado en archivo.")
        else:
            print("No se pudo guardar en archivo. Cambios solo en memoria.")

    def actualizar_producto(self, id_producto: str, cantidad: Optional[int] = None, precio: Optional[float] = None) -> None:
        # Bandera para verificar si se encontró el producto
        encontrado = False

        # Busca el producto por ID y actualiza los campos si se proporcionan
        for p in self.lproducto:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                encontrado = True
                break

        if not encontrado:
            print("Producto no encontrado.")
            return

        # Guarda los cambios en archivo
        if self.archivo.guardar(self.lproducto):
            print("Producto actualizado y guardado en archivo.")
        else:
            print("No se pudo guardar en archivo. Cambios solo en memoria.")

    # -------------------------------
    # Consultas (no imprimen, devuelven listas)
    # -------------------------------

    def buscar_por_nombre(self, nombre: str) -> List[Producto]:
        # Devuelve productos cuyo nombre contenga la cadena buscada (insensible a mayúsculas)
        return [p for p in self.lproducto if nombre.lower() in p.get_nombre().lower()]

    def obtener_todos(self) -> List[Producto]:
        # Devuelve una copia de la lista completa de productos
        return list(self.lproducto)

    def recargar(self) -> None:
        # Recarga el inventario desde el archivo
        self.lproducto = self.archivo.cargar()
        print("Inventario recargado desde archivo.")

    # -------------------------------
    # Presentación (impresión en consola)
    # -------------------------------

    def imprimir_tabla(self, lproducto: List[Producto]) -> None:
        # Verifica si hay productos para mostrar
        if not lproducto:
            print("No hay lproducto para mostrar.")
            return

        # Imprime encabezados con formato alineado
        print(f"{'ID':<8}{'Nombre':<20}{'Cantidad':<12}{'Precio':<10}")
        print("-" * 50)

        # Imprime cada producto con formato tabular
        for p in lproducto:
            print(f"{p.get_id():<8}{p.get_nombre():<20}{p.get_cantidad():<12}{p.get_precio():<10.2f}")
