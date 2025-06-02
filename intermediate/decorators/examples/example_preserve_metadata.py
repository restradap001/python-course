"""
Ejemplo: Decorador que preserva metadatos de la función original

Descripción detallada:
Este ejemplo muestra cómo usar functools.wraps para mantener el nombre y docstring de la función decorada.
"""

import functools

def mi_decorador(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorando...")
        return func(*args, **kwargs)
    return wrapper

@mi_decorador
def sumar(a, b):
    """Suma dos números."""
    return a + b

if __name__ == "__main__":
    print(sumar(2, 3))
    print(sumar.__name__)
    print(sumar.__doc__)
