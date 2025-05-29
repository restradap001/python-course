"""
Ejemplo: Definición de una clase y creación de un objeto

Descripción detallada:
Este ejemplo muestra cómo definir una clase simple llamada Persona con atributos nombre y edad, y cómo crear un objeto de esa clase e imprimir sus atributos.
"""

if __name__ == "__main__":
    class Persona:
        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad
    persona1 = Persona("Ana", 30)
    print(f"Nombre: {persona1.nombre}")
    print(f"Edad: {persona1.edad}")
