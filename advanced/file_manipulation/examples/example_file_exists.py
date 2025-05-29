"""
Ejemplo: Verificar si un archivo existe

Descripción detallada:
Este ejemplo muestra cómo verificar si un archivo existe usando el módulo os.path.
"""

import os

if __name__ == "__main__":
    archivo = "ejemplo.txt"
    if os.path.exists(archivo):
        print("El archivo existe.")
    else:
        print("El archivo no existe.")
