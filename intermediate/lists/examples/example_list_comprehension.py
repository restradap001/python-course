"""
Ejemplo: Comprensión de listas

Descripción detallada:
Este ejemplo muestra cómo crear una nueva lista con los cuadrados de los números del 1 al 5 usando comprensión de listas.
"""

if __name__ == "__main__":
    cuadrados = [x**2 for x in range(1, 6)]
    print(cuadrados)
