"""
Ejemplo: Decorador aplicado a métodos de clase

Descripción detallada:
Este ejemplo muestra cómo aplicar un decorador a un método dentro de una clase.
"""

def mi_decorador(func):
    def wrapper(*args, **kwargs):
        print("Método decorado")
        return func(*args, **kwargs)
    return wrapper

class Persona:
    @mi_decorador
    def saludar(self):
        print("Hola, soy una persona.")

if __name__ == "__main__":
    p = Persona()
    p.saludar()
