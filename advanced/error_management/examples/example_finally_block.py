"""
Ejemplo: Uso del bloque finally en manejo de excepciones

Descripción detallada:
Este ejemplo muestra cómo utilizar el bloque finally en el manejo de excepciones. El código intenta realizar una división por cero, captura la excepción y luego ejecuta el bloque finally para mostrar 'Finalizado', demostrando que finally siempre se ejecuta.
"""

if __name__ == "__main__":
    # Intentamos realizar una división por cero
    try:
        x = 1 / 0
    except ZeroDivisionError:
        # Se captura la excepción y se muestra un mensaje de error
        print('¡Error!')
    finally:
        # Este bloque se ejecuta siempre
        print('Finalizado')
