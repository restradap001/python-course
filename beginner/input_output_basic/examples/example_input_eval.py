"""
Ejemplo: Evaluar expresión ingresada

Descripción:
Solicita una expresión matemática y muestra el resultado usando eval().

Funciones útiles:
- input()
- eval()
- print()
"""

if __name__ == "__main__":
    expr = input("Escribe una expresión matemática: ")
    print(f"Resultado: {eval(expr)}")
