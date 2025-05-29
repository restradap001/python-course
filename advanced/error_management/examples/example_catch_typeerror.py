"""
Ejemplo: Capturar TypeError

Descripción detallada:
Este ejemplo muestra cómo capturar un error de tipo (TypeError) al intentar sumar un número y una cadena.
"""

if __name__ == "__main__":
    try:
        resultado = 5 + "cinco"
    except TypeError:
        print("No se puede sumar un número y una cadena.")
