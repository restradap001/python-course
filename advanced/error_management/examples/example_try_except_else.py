"""
Ejemplo: Uso de try-except-else

Descripción detallada:
Este ejemplo muestra cómo usar un bloque try-except-else para manejar errores y ejecutar código solo si no ocurre ninguna excepción.
"""

if __name__ == "__main__":
    try:
        numero = int("10")
    except ValueError:
        print("Error de conversión.")
    else:
        print(f"Conversión exitosa: {numero}")
