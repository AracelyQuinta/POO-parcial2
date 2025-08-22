class Producto:
    """
    Representa un producto con atributos básicos:
    - ID único
    - Nombre descriptivo
    - Cantidad en inventario
    - Precio unitario

    Incluye validaciones para evitar valores negativos o inválidos.
    """

    def __init__(self, id, nombre, cantidad, precio):
        # Asigna el ID y nombre directamente
        self.id = id
        self.nombre = nombre

        # Usa los métodos set para aplicar validaciones en cantidad y precio
        self.setcantidad(cantidad)
        self.setprecio(precio)

    # Métodos getter para acceder a los atributos
    def getid(self):
        return self.id

    def getnombre(self):
        return self.nombre

    def getcantidad(self):
        return self._cantidad  # Se accede al atributo protegido

    def getprecio(self):
        return self._precio  # Se accede al atributo protegido

    # Método setter para cantidad con validación
    def setcantidad(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self._cantidad = nueva_cantidad
        else:
            # Si la cantidad es negativa, se corrige a 0 y se informa
            print("La cantidad no puede ser negativa. Se asigna 0.")
            self._cantidad = 0

    # Método setter para precio con validación
    def setprecio(self, nuevo_precio):
        if nuevo_precio > 0:
            self._precio = nuevo_precio
        else:
            # Si el precio es inválido, se asigna 0 y se informa
            print("El precio debe ser mayor a $0. Se asigna $0 por defecto.")
            self._precio = 0

    # Representación en texto del producto, útil para imprimir en consola
    def __str__(self):
        return (
            f"Producto\n"
            f"|   ID   |   Nombre   | Cantidad | Precio |\n"
            f"| {self.getid():^6} | {self.getnombre():^10} | {self.getcantidad():^8} | ${self.getprecio():.2f} |"
        )
