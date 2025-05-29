"""
Ejemplo: Crear diccionario a partir de listas

Descripción detallada:
Este ejemplo muestra cómo crear un diccionario combinando dos listas, una de claves y otra de valores.
"""

if __name__ == "__main__":
    claves = ["a", "b", "c"]
    valores = [1, 2, 3]
    diccionario = dict(zip(claves, valores))
    print(diccionario)
