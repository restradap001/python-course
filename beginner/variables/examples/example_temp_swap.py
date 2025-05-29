"""
Ejemplo: Intercambio temporal de variables

Descripción detallada:
Este ejemplo muestra cómo intercambiar el valor de dos variables usando una variable temporal.
"""

if __name__ == "__main__":
    a = 5
    b = 10
    temp = a
    a = b
    b = temp
    print(f"a = {a}, b = {b}")
