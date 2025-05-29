"""
Ejemplo: Recorrer un diccionario

Descripción detallada:
Este ejemplo muestra cómo iterar sobre los pares clave-valor de un diccionario en Python usando un ciclo for.
"""

if __name__ == "__main__":
    car = {'brand': 'Toyota', 'model': 'Corolla', 'year': 2020}  # Diccionario de ejemplo
    # Recorremos el diccionario e imprimimos cada clave y valor
    for key, value in car.items():
        print(f"{key}: {value}")
