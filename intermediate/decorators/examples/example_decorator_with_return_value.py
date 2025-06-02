"""
Ejemplo: Decorador que valida el valor de retorno

Descripción detallada:
Este ejemplo muestra cómo un decorador puede validar el valor de retorno de una función y lanzar una excepción si no cumple una condición.
"""

def validar_positivo(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        if resultado < 0:
            raise ValueError("El resultado debe ser positivo")
        return resultado
    return wrapper

@validar_positivo
def resta(a, b):
    return a - b

if __name__ == "__main__":
    print(resta(5, 3))
    # print(resta(2, 5))  # Descomenta para ver la excepción
