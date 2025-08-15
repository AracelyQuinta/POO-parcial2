'''
Clase Producto:
Atributos: ID (único), nombre, cantidad y precio.
Métodos: Constructor, getters y setters para cada atributo.
'''
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self._cantidad = cantidad
        self._precio=precio

    def getid (self):
        return self.id

    def getnombre(self):
        return self.nombre

    def getcantidad(self):
        return self._cantidad


    def getprecio(self):
        return self._precio

    def setcantidad(self, nueva_cantidad):
        if nueva_cantidad > 0:
            self._cantidad = nueva_cantidad
        else:
            print("No hay producto en stock")
            self._cantidad = 0

    def setprecio(self, nuevo_precio):
        if nuevo_precio > 0:
            self._precio = nuevo_precio
        else:
            print("Ningun producto tiene el valor de $0.00")
            self._precio = 0


    def __str__(self):
        return(
            f"Producto\n"
            f"|    ID    |    Nombre    |    Cantidad    |    Precio    |\n"
            f"| {self.getid()} | {self.getnombre()} | {self.getcantidad()} | {self.getprecio()} |"
        )
'''
producto_nuevo= Producto(7789,"jabones",20,0.40)
print(producto_nuevo)
'''
