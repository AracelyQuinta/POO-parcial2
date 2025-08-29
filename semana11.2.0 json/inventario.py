from typing import List, Optional
from producto import Producto
from archivo import GestionArchivo

class Inventario:
    """
    Lógica de negocio simple. Delegamos la carga/guardado en ArchivoInventario.
    """
    def __init__(self):
        self.archivo = GestionArchivo()
        self.lproducto: List[Producto] = self.archivo.cargar()

    # Operaciones
    def anadir_producto(self, p: Producto) -> None:
        if any(x.get_id() == p.get_id() for x in self.lproducto):
            print("El ID ya existe. No se añadió el producto.")
            return
        self.lproducto.append(p)
        if self.archivo.guardar(self.lproducto):
            print("Producto añadido y guardado en archivo.")
        else:
            print("No se pudo guardar en archivo. El producto permanece en memoria.")

    def eliminar_producto(self, id_producto: str) -> None:
        original = len(self.lproducto)
        self.lproducto = [p for p in self.lproducto if p.get_id() != id_producto]
        if len(self.lproducto) == original:
            print("Producto no encontrado.")
            return
        if self.archivo.guardar(self.lproducto):
            print("Producto eliminado y guardado en archivo.")
        else:
            print("No se pudo guardar en archivo. Cambios solo en memoria.")

    def actualizar_producto(self, id_producto: str, cantidad: Optional[int] = None, precio: Optional[float] = None) -> None:
        encontrado = False
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
        if self.archivo.guardar(self.lproducto):
            print("Producto actualizado y guardado en archivo.")
        else:
            print("No se pudo guardar en archivo. Cambios solo en memoria.")

    # Consultas: devuelven listas; no imprimen
    def buscar_por_nombre(self, nombre: str) -> List[Producto]:
        return [p for p in self.lproducto if nombre.lower() in p.get_nombre().lower()]

    def obtener_todos(self) -> List[Producto]:
        return list(self.lproducto)

    def recargar(self) -> None:
        self.lproducto = self.archivo.cargar()
        print("Inventario recargado desde archivo.")

    # Presentación: imprime una tabla a partir de una lista
    def imprimir_tabla(self, lproducto: List[Producto]) -> None:
        if not lproducto:
            print("No hay lproducto para mostrar.")
            return
        print(f"{'ID':<8}{'Nombre':<20}{'Cantidad':<12}{'Precio':<10}")
        print("-" * 50)
        for p in lproducto:
            print(f"{p.get_id():<8}{p.get_nombre():<20}{p.get_cantidad():<12}{p.get_precio():<10.2f}")
