"""
Ejemplo: Mensaje según calificación

Descripción detallada:
Este ejemplo muestra cómo usar if-elif-else para mostrar un mensaje según la calificación de un estudiante.
"""

if __name__ == "__main__":
    calificacion = 7
    if calificacion >= 9:
        print("Excelente")
    elif calificacion >= 7:
        print("Aprobado")
    else:
        print("Reprobado")
