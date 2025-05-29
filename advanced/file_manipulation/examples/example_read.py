"""
Ejemplo: Lectura completa de un archivo

Descripción detallada:
Este ejemplo muestra cómo leer todo el contenido de un archivo de una sola vez. El código abre un archivo en modo lectura y muestra su contenido, ilustrando la lectura básica de archivos en Python.
"""

if __name__ == "__main__":
    # Abrimos el archivo en modo lectura ('r')
    with open('example.txt', 'r') as f:
        # Leemos y mostramos todo el contenido del archivo
        print(f.read())
