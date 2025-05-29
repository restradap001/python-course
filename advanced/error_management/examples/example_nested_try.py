"""
Ejemplo: Bloques try anidados

Descripción detallada:
Este ejemplo muestra cómo usar bloques try-except anidados para manejar diferentes tipos de errores.
"""

if __name__ == "__main__":
    try:
        try:
            x = int("abc")
        except ValueError:
            print("Error de valor interno.")
        y = 10 / 0
    except ZeroDivisionError:
        print("Error de división externa.")
