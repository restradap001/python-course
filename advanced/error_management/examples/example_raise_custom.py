"""
Ejemplo: Lanzar excepción personalizada

Descripción detallada:
Este ejemplo muestra cómo lanzar una excepción personalizada usando raise.
"""

if __name__ == "__main__":
    edad = -5
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
