"""
Ejemplo: If anidado

Descripción detallada:
Este ejemplo muestra cómo usar condicionales anidados para determinar si una persona es adolescente (entre 13 y 19 años inclusive).
"""

if __name__ == "__main__":
    age = 15  # Edad a evaluar
    if age >= 13:
        if age <= 19:
            # Si la edad está entre 13 y 19
            print('Adolescente')
        else:
            print('No es adolescente')
    else:
        print('No es adolescente')
