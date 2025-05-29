"""
Ejemplo: Inmutabilidad de tuplas

Descripción:
Demuestra que las tuplas no pueden modificarse.

Funciones útiles:
- tuple
- TypeError
- print()
"""

if __name__ == "__main__":
    t = (1, 2, 3)
    try:
        t[0] = 10
    except TypeError:
        print("No se puede modificar una tupla")
