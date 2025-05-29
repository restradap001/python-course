"""
Ejemplo: Escribir varias líneas en un archivo

Descripción detallada:
Este ejemplo muestra cómo escribir varias líneas de texto en un archivo usando writelines.
"""

if __name__ == "__main__":
    lineas = ["Primera línea\n", "Segunda línea\n", "Tercera línea\n"]
    with open("varias_lineas.txt", "w") as archivo:
        archivo.writelines(lineas)
    print("Líneas escritas en el archivo.")
