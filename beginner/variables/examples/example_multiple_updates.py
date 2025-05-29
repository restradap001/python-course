"""
Ejemplo: Actualización múltiple de variables

Descripción detallada:
Este ejemplo muestra cómo actualizar varias variables en una sola línea de código.
"""

if __name__ == "__main__":
    x, y = 1, 2
    x, y = y, x + y
    print(f"x = {x}, y = {y}")
