"""
Ejemplo: Intercambio de valores entre variables

Descripción detallada:
Este ejemplo muestra cómo intercambiar los valores de dos variables en Python usando asignación múltiple.
"""

if __name__ == "__main__":
    x = 3  # Valor inicial de x
    y = 7  # Valor inicial de y
    x, y = y, x  # Intercambiamos los valores
    print(x, y)  # Mostramos los valores después del intercambio
