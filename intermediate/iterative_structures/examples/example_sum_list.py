"""
Ejemplo: Suma de elementos de una lista con for

Descripción detallada:
Este ejemplo muestra cómo usar un bucle for para sumar todos los elementos de una lista.
"""

if __name__ == "__main__":
    numeros = [2, 4, 6, 8]
    suma = 0
    for n in numeros:
        suma += n
    print(f"La suma es: {suma}")
