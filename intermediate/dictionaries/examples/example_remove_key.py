"""
Ejemplo: Eliminar una clave de un diccionario

Descripción detallada:
Este ejemplo muestra cómo eliminar una clave y su valor de un diccionario usando del.
"""

if __name__ == "__main__":
    datos = {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"}
    del datos["ciudad"]
    print(datos)
