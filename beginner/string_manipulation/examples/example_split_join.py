"""
Ejemplo: Separar y unir palabras

Descripción detallada:
Este ejemplo muestra cómo separar una frase en palabras y luego unirlas usando un guion.
"""

if __name__ == "__main__":
    frase = "Python es divertido"
    palabras = frase.split()
    nueva_frase = "-".join(palabras)
    print(nueva_frase)
