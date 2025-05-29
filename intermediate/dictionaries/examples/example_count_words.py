"""
Ejemplo: Contar palabras en una frase

Descripción detallada:
Este ejemplo muestra cómo usar un diccionario para contar cuántas veces aparece cada palabra en una frase.
"""

if __name__ == "__main__":
    frase = "hola mundo hola python"
    palabras = frase.split()
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    print(conteo)
