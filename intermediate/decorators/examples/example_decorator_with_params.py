"""
Ejemplo: Decorador con parámetros

Descripción detallada:
Este ejemplo muestra cómo crear un decorador que recibe sus propios parámetros.
"""

def repetir(n):
    def decorador(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorador

@repetir(3)
def saludar():
    print("¡Hola!")

if __name__ == "__main__":
    saludar()
