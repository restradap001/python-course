"""
Ejemplo: Decorador básico

Descripción detallada:
Este ejemplo muestra cómo crear y usar un decorador simple que imprime mensajes antes y después de ejecutar una función.
"""

def mi_decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes de la función")
        resultado = func(*args, **kwargs)
        print("Después de la función")
        return resultado
    return wrapper

@mi_decorador
def saludar():
    print("¡Hola!")

if __name__ == "__main__":
    saludar()
