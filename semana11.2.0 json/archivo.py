import os
import json
from typing import List
from producto import Producto

class GestionArchivo:
    """
    Manejo de persistencia en JSON (diccionario).
    - cargar() -> List[Producto]
    - guardar(lproducto) -> bool
    """
    def __init__(self):
        self.ruta = "inventario.txt"
        if not os.path.exists(self.ruta):
            with open(self.ruta, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4)

    def cargar(self) -> List[Producto]:
        try:
            with open(self.ruta, "r", encoding="utf-8") as f:
                data = json.load(f)
                lproducto = []
                for p in data:
                    lproducto.append(Producto(p["id"], p["nombre"], p["cantidad"], p["precio"]))

                #return [Producto(d["id"], d["nombre"], d["cantidad"], d["precio"]) for d in data]
                return lproducto
        except Exception as e:
            print(f"Error leyendo {self.ruta}: {e}")
            return []

    def guardar(self, lproducto: List[Producto]) -> bool:
        try:
            with open(self.ruta, "w", encoding="utf-8") as f:
                json.dump([
                    {
                        "id": p.get_id(),
                        "nombre": p.get_nombre(),
                        "cantidad": p.get_cantidad(),
                        "precio": p.get_precio(),
                    }
                    for p in lproducto
                ], f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error escribiendo {self.ruta}: {e}")
            return False
