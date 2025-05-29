"""
Ejemplo: Manejo de división por cero con try-except

Descripción detallada:
Este ejemplo muestra cómo manejar una excepción ZeroDivisionError usando un bloque try-except. El código intenta dividir por cero, captura la excepción y muestra un mensaje indicando que no se puede dividir por cero.
"""

if __name__ == "__main__":
    # Intentamos dividir por cero
    try:
        resultado = 10 / 0
    except ZeroDivisionError:
        # Se captura la excepción y se muestra un mensaje personalizado
        print('No se puede dividir por cero!')
