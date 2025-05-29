"""
Ejemplo: Comprensión anidada

Descripción:
Crea una matriz identidad usando comprensión de listas anidada.

Funciones útiles:
- list comprehension
- range()
- print()
"""

if __name__ == "__main__":
    identidad = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
    print(identidad)
