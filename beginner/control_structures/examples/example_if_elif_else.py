"""
Ejemplo: Bloque if-elif-else

Descripción detallada:
Este ejemplo muestra cómo usar una estructura condicional if-elif-else para clasificar una calificación numérica en letras. Se evalúa el valor de score y se imprime la calificación correspondiente.
"""

if __name__ == "__main__":
    score = 92  # Calificación numérica
    if score >= 90:
        # Si la calificación es 90 o más
        print('Calificación: A')
    elif score >= 80:
        # Si la calificación es 80 o más pero menor que 90
        print('Calificación: B')
    else:
        # Para cualquier otro caso
        print('Calificación: C o menor')
