"""
Ejemplo: Agregar contenido a un archivo (append)

Descripción detallada:
Este ejemplo muestra cómo agregar una línea al final de un archivo existente usando el modo append ('a'). El código abre el archivo y escribe una nueva línea sin borrar el contenido anterior.
"""

if __name__ == "__main__":
    # Abrimos el archivo en modo append ('a')
    with open('example.txt', 'a') as f:
        # Agregamos una nueva línea al final del archivo
        f.write('Línea agregada\n')
