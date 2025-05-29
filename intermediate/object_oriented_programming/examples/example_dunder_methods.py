"""
Ejemplo: Métodos especiales (__str__)

Descripción detallada:
Este ejemplo muestra cómo definir el método especial __str__ en una clase Punto para personalizar su representación como cadena.
"""

if __name__ == "__main__":
    class Punto:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def __str__(self):
            return f"({self.x}, {self.y})"

    p = Punto(2, 3)
    print(p)
