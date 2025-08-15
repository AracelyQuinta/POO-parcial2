class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"        class Producto:
            def __init__(self, id, nombre, cantidad, precio):
                self.id = id
                self.nombre = nombre
                self.cantidad = cantidad
                self.precio = precio
        
            def get_id(self):
                return self.id
        
            def get_nombre(self):
                return self.nombre
        
            def set_nombre(self, nombre):
                self.nombre = nombre
        
            def get_cantidad(self):
                return self.cantidad
        
            def set_cantidad(self, cantidad):
                self.cantidad = cantidad
        
            def get_precio(self):
                return self.precio
        
            def set_precio(self, precio):
                self.precio = precio
        
            def __str__(self):
                return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"