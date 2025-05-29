"""
Ejemplo: Manejo de entrada inválida (ValueError)

Descripción detallada:
Este ejemplo muestra cómo manejar una entrada inválida del usuario usando un bloque try-except. El código intenta convertir una cadena a entero, captura el ValueError si la entrada no es válida y muestra un mensaje de error.
"""

if __name__ == "__main__":
    # Intentamos convertir una cadena no numérica a entero
    try:
        num = int('abc')
    except ValueError:
        # Se captura la excepción y se muestra un mensaje personalizado
        print('¡Entrada no válida!')
