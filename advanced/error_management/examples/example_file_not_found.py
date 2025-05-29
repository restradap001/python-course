"""
Ejemplo: Excepción de archivo no encontrado (FileNotFoundError)

Descripción detallada:
Este ejemplo muestra cómo manejar la excepción FileNotFoundError al intentar abrir un archivo que no existe. El código intenta abrir un archivo, captura la excepción y muestra un mensaje personalizado.
"""

if __name__ == "__main__":
    # Intentamos abrir un archivo que no existe
    try:
        with open('not_found.txt') as f:
            print(f.read())
    except FileNotFoundError:
        # Se captura la excepción y se muestra un mensaje personalizado
        print('Archivo no encontrado.')
