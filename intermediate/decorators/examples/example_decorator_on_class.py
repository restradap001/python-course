"""
Ejemplo: Decorador de clase

Descripción detallada:
Este ejemplo muestra cómo crear un decorador que modifica el comportamiento de una clase completa.
"""

def agregar_metodo(cls):
    cls.nuevo_metodo = lambda self: print("Método agregado por decorador")
    return cls

@agregar_metodo
class MiClase:
    pass

if __name__ == "__main__":
    obj = MiClase()
    obj.nuevo_metodo()
