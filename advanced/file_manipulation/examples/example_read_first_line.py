"""
Ejemplo: Leer la primera línea de un archivo

Descripción detallada:
Este ejemplo muestra cómo leer solo la primera línea de un archivo de texto usando readline.
"""

if __name__ == "__main__":
    with open("ejemplo.txt", "r") as archivo:
        primera_linea = archivo.readline()
    print(f"Primera línea: {primera_linea}")
