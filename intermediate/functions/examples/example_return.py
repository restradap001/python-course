"""
Ejemplo: Función con valor de retorno

Descripción detallada:
Este ejemplo muestra cómo definir una función que retorna un valor en Python. Se define una función add que suma dos números y retorna el resultado.
"""

if __name__ == "__main__":
    def add(a, b):
        # Retornamos la suma de a y b
        return a + b
    resultado = add(2, 3)  # Llamamos a la función
    print(resultado)  # Mostramos el resultado
