"""
Ejemplo: Lectura de un archivo línea por línea

Descripción detallada:
Este ejemplo muestra cómo leer un archivo línea por línea usando un ciclo for. El código abre un archivo en modo lectura y muestra cada línea después de eliminar los espacios en blanco, demostrando la lectura secuencial de archivos.
"""

if __name__ == "__main__":
    # Abrimos el archivo en modo lectura ('r')
    with open('example.txt', 'r') as f:
        # Recorremos cada línea del archivo
        for line in f:
            # Mostramos la línea sin saltos de línea extra
            print(line.strip())
