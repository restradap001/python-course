"""
Ejemplo: Decorador con argumentos en la función decorada

Descripción detallada:
Este ejemplo muestra cómo un decorador puede aplicarse a funciones que reciben argumentos.
"""

def mi_decorador(func):
    def wrapper(*args, **kwargs):
        print(f"Llamando a {func.__name__} con argumentos {args} y {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@mi_decorador
def sumar(a, b):
    print(f"Resultado: {a + b}")

if __name__ == "__main__":
    sumar(3, 4)
