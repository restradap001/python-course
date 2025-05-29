"""
Ejemplo: Sentencia if-else

Descripción detallada:
Este ejemplo muestra cómo usar una estructura if-else para determinar si un número es par o impar. Se evalúa el residuo de x al dividirlo entre 2.
"""

if __name__ == "__main__":
    x = 4  # Número a evaluar
    if x % 2 == 0:
        # Si el residuo es 0, el número es par
        print('x es par')
    else:
        # Si no, el número es impar
        print('x es impar')
