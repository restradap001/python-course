"""
Ejemplo: Actualización de inventario

Descripción detallada:
Este ejemplo muestra cómo actualizar la cantidad de un producto en un inventario representado por un diccionario.
"""

if __name__ == "__main__":
    inventario = {"manzanas": 10, "naranjas": 5}
    inventario["manzanas"] += 5
    print(f"Inventario actualizado: {inventario}")
