# Importa módulos estándar y clases necesarias
import os                      # Para verificar existencia de archivos
import json                    # Para manejar lectura/escritura en formato JSON
from typing import List        # Para indicar listas tipadas
from producto import Producto  # Importa la clase Producto definida externamente

class GestionArchivo:
    """
    Clase encargada de la persistencia de datos del inventario en formato JSON.
    Métodos principales:
    - cargar() -> List[Producto]: Carga productos desde archivo.
    - guardar(lproducto) -> bool: Guarda lista de productos en archivo.
    """

    def __init__(self):
        # Define la ruta del archivo de almacenamiento
        self.ruta = "inventario.txt"

        # Si el archivo no existe, lo crea con una lista vacía en formato JSON
        if not os.path.exists(self.ruta):
            with open(self.ruta, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4)

    def cargar(self) -> List[Producto]:
        """
        Lee el archivo JSON y convierte cada entrada en una instancia de Producto.
        Devuelve una lista de productos. Si hay error, devuelve lista vacía.
        """
        try:
            with open(self.ruta, "r", encoding="utf-8") as f:
                data = json.load(f)  # Carga el contenido como lista de diccionarios
                lproducto = []

                # Convierte cada diccionario en un objeto Producto
                for p in data:
                    lproducto.append(Producto(p["id"], p["nombre"], p["cantidad"], p["precio"]))

                # Alternativa compacta (comentada): comprensión de listas
                # return [Producto(d["id"], d["nombre"], d["cantidad"], d["precio"]) for d in data]

                return lproducto
        except Exception as e:
            # Muestra error en consola si la lectura falla
            print(f"Error leyendo {self.ruta}: {e}")
            return []

    def guardar(self, lproducto: List[Producto]) -> bool:
        """
        Guarda la lista de productos en formato JSON.
        Convierte cada objeto Producto en un diccionario.
        Devuelve True si se guarda correctamente, False si ocurre un error.
        """
        try:
            with open(self.ruta, "w", encoding="utf-8") as f:
                json.dump([
                    {
                        "id": p.get_id(),
                        "nombre": p.get_nombre(),
                        "cantidad": p.get_cantidad(),
                        "precio": p.get_precio(),
                    }
                    for p in lproducto  # Itera sobre la lista de productos
                ], f, indent=4, ensure_ascii=False)  # Formato legible y soporte UTF-8
            return True
        except Exception as e:
            # Muestra error en consola si la escritura falla
            print(f"Error escribiendo {self.ruta}: {e}")
            return False
