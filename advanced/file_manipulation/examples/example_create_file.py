"""
Ejemplo: Crear y escribir en un archivo

Descripción detallada:
Este ejemplo muestra cómo crear un archivo nuevo y escribir una línea de texto en él usando open y write.
"""

if __name__ == "__main__":
    with open("nuevo_archivo.txt", "w") as archivo:
        archivo.write("Hola, este es un archivo nuevo.\n")
    print("Archivo creado y texto escrito.")
