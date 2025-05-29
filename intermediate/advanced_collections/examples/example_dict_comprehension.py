"""
Ejemplo: Comprensión de diccionarios

Descripción:
Crea un diccionario con números y sus cuadrados usando dict comprehension.

Funciones útiles:
- dict comprehension
- range()
- print()
"""

if __name__ == "__main__":
    cuadrados = {x: x*x for x in range(5)}
    print(cuadrados)
