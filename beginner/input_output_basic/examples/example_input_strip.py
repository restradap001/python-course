"""
Ejemplo: Limpiar espacios de la entrada

Descripción:
Lee un texto y elimina espacios al inicio y final.

Funciones útiles:
- input()
- str.strip()
- print()
"""

if __name__ == "__main__":
    texto = input("Escribe algo con espacios: ").strip()
    print(f"Texto limpio: '{texto}'")
