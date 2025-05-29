"""
Ejemplo: Escritura en un archivo

Descripción detallada:
Este ejemplo muestra cómo escribir texto en un archivo en Python. El código abre un archivo en modo escritura y escribe una línea de texto, ilustrando operaciones básicas de salida a archivos.
"""

if __name__ == "__main__":
    # Abrimos el archivo en modo escritura ('w')
    with open('example.txt', 'w') as f:
        # Escribimos una línea de texto en el archivo
        f.write('¡Hola, archivo!\n')
