"""
Ejemplo: Modificar el valor de una clave en un diccionario

Descripción detallada:
Este ejemplo muestra cómo modificar el valor asociado a una clave en un diccionario de Python.
"""

if __name__ == "__main__":
    car = {'brand': 'Toyota', 'model': 'Corolla', 'year': 2020}  # Diccionario original
    car['year'] = 2022  # Modificamos el valor de la clave 'year'
    print(car)  # Mostramos el diccionario actualizado
