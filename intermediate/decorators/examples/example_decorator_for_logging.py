"""
Ejemplo: Decorador para logging

Descripción detallada:
Este ejemplo muestra cómo crear un decorador que registre (log) las llamadas a una función.
"""

def loggear(func):
    def wrapper(*args, **kwargs):
        print(f"Llamando a {func.__name__} con argumentos {args} y {kwargs}")
        resultado = func(*args, **kwargs)
        print(f"{func.__name__} terminó")
        return resultado
    return wrapper

@loggear
def multiplicar(a, b):
    return a * b

if __name__ == "__main__":
    print(multiplicar(2, 5))
