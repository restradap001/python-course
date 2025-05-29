"""
Ejemplo: Métodos de clase

Descripción detallada:
Este ejemplo muestra cómo definir un método de clase en Producto para llevar la cuenta de instancias creadas.
"""

if __name__ == "__main__":
    class Producto:
        contador = 0
        def __init__(self, nombre):
            self.nombre = nombre
            Producto.contador += 1
        @classmethod
        def total_productos(cls):
            return cls.contador

    p1 = Producto("A")
    p2 = Producto("B")
    print(f"Total productos: {Producto.total_productos()}")
