"""
Ejemplo: Decorador que modifica el valor de retorno

Descripción detallada:
Este ejemplo muestra cómo un decorador puede modificar el valor de retorno de una función decorada.
"""

def duplicar_resultado(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        return resultado * 2
    return wrapper

@duplicar_resultado
def obtener_numero():
    return 5

if __name__ == "__main__":
    print(obtener_numero())
