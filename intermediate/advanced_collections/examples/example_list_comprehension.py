"""
Ejemplo: Comprensión de listas

Descripción:
Crea una lista de cuadrados usando list comprehension.

Funciones útiles:
- list comprehension
- range()
- print()
"""

if __name__ == "__main__":
    cuadrados = [x*x for x in range(5)]
    print(cuadrados)
