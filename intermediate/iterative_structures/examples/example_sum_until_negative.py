"""
Ejemplo: Sumar hasta número negativo con while

Descripción detallada:
Este ejemplo muestra cómo usar un bucle while para sumar números de una lista hasta encontrar un número negativo.
"""

if __name__ == "__main__":
    numeros = [3, 5, 7, -1, 4]
    suma = 0
    i = 0
    while i < len(numeros) and numeros[i] >= 0:
        suma += numeros[i]
        i += 1
    print(f"Suma hasta negativo: {suma}")
