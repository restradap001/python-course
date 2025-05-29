"""
Ejemplo: Operaciones con sets

Descripción:
Realiza unión, intersección y diferencia entre sets.

Funciones útiles:
- set.union()
- set.intersection()
- set.difference()
- print()
"""

if __name__ == "__main__":
    a = {1, 2, 3}
    b = {2, 3, 4}
    print(a.union(b))
    print(a.intersection(b))
    print(a.difference(b))
