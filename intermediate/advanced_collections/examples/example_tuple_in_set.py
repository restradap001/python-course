"""
Ejemplo: Tuplas como elementos de un set

Descripción:
Demuestra que las tuplas pueden ser elementos de un set, pero las listas no.

Funciones útiles:
- set
- tuple
- print()
"""

if __name__ == "__main__":
    s = set()
    s.add((1, 2))
    print(s)
