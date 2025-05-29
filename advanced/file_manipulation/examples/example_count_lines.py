"""
Ejemplo: Contar líneas en un archivo

Descripción detallada:
Este ejemplo muestra cómo contar el número de líneas en un archivo. El código abre un archivo, recorre cada línea y las cuenta, luego muestra el total de líneas encontradas.
"""

if __name__ == "__main__":
    # Abrimos el archivo en modo lectura ('r')
    with open('example.txt', 'r') as f:
        # Contamos las líneas usando una expresión generadora
        count = sum(1 for _ in f)
    # Mostramos el total de líneas
    print(count)
