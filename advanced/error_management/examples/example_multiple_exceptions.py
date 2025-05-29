"""
Ejemplo: Captura de múltiples excepciones

Descripción detallada:
Este ejemplo muestra cómo manejar varios tipos de excepciones en un solo bloque try-except. El código intenta convertir una cadena a entero, lo que genera un ValueError, y captura tanto ValueError como TypeError, mostrando el mensaje de error.
"""

if __name__ == "__main__":
    # Intentamos convertir una cadena no numérica a entero
    try:
        value = int('abc')
    except (ValueError, TypeError) as e:
        # Se captura la excepción y se muestra el mensaje de error
        print(f'Error: {e}')
