"""
Ejemplo: Leer todo el contenido de un archivo

Descripción detallada:
Este ejemplo muestra cómo leer todo el contenido de un archivo de texto usando read.
"""

if __name__ == "__main__":
    with open("ejemplo.txt", "r") as archivo:
        contenido = archivo.read()
    print(contenido)
