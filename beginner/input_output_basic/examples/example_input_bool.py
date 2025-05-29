"""
Ejemplo: Entrada booleana simple

Descripción:
Pregunta al usuario si quiere continuar y responde según la entrada.

Funciones útiles:
- input()
- str.lower()
- print()
"""

if __name__ == "__main__":
    respuesta = input("¿Deseas continuar? (s/n): ").lower()
    if respuesta == "s":
        print("Continuando...")
    else:
        print("Programa finalizado.")
