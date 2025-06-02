"""
Ejemplo: Múltiples decoradores

Descripción detallada:
Este ejemplo muestra cómo se pueden aplicar varios decoradores a una misma función.
"""

def decorador1(func):
    def wrapper(*args, **kwargs):
        print("Decorador 1")
        return func(*args, **kwargs)
    return wrapper

def decorador2(func):
    def wrapper(*args, **kwargs):
        print("Decorador 2")
        return func(*args, **kwargs)
    return wrapper

@decorador1
@decorador2
def mostrar():
    print("Función principal")

if __name__ == "__main__":
    mostrar()
