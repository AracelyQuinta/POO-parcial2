# producto.py
class Producto:
    def __init__(self, id_producto: str, nombre: str, cantidad: int, precio: float):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self) -> str:
        return self.id_producto

    def get_nombre(self) -> str:
        return self.nombre

    def get_cantidad(self) -> int:
        return self.cantidad

    def get_precio(self) -> float:
        return self.precio

    # Setters
    def set_nombre(self, nombre: str) -> None:
        self.nombre = nombre

    def set_cantidad(self, cantidad: int) -> None:
        self.cantidad = cantidad

    def set_precio(self, precio: float) -> None:
        self.precio = precio
