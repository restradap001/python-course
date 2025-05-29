"""
Ejemplo: Función para imprimir números del 1 al n

Descripción detallada:
Este ejemplo muestra cómo definir una función que imprime los números del 1 al n usando un bucle for.
"""

if __name__ == "__main__":
    def imprimir_numeros(n):
        for i in range(1, n+1):
            print(i)
    imprimir_numeros(5)
