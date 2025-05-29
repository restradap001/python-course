
# Programación Orientada a Objetos (POO)

## Descripción General
La Programación Orientada a Objetos (POO) es un paradigma que organiza el código en torno a objetos, los cuales agrupan datos y comportamientos relacionados. Es fundamental para escribir programas robustos, reutilizables y fáciles de mantener en Python.

## Características principales
- Permite definir **clases** (plantillas) y crear **objetos** (instancias).
- Los objetos pueden tener **atributos** (datos) y **métodos** (funciones asociadas).
- Soporta **encapsulamiento** (protección de datos internos), **herencia** (reutilización de código) y **polimorfismo** (métodos con el mismo nombre en diferentes clases).
- El uso de `self` permite acceder a los atributos y métodos de cada objeto.

## Operaciones comunes
- Definir una clase: `class Persona: ...`
- Crear un objeto: `p = Persona()`
- Acceder a atributos: `p.nombre`
- Llamar métodos: `p.hablar()`
- Heredar de otra clase: `class Estudiante(Persona): ...`

## Ejemplo
```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

persona1 = Persona("Ana", 30)
persona1.saludar()
# Salida: Hola, soy Ana y tengo 30 años.
```

## Buenas Prácticas
- Usa nombres descriptivos para clases, atributos y métodos.
- Encapsula los datos sensibles usando atributos privados o protegidos.
- Aprovecha la herencia para evitar duplicar código.
- Utiliza el polimorfismo para escribir código flexible y reutilizable.
- Documenta tus clases y métodos con docstrings.

## ¿Cómo usar este módulo?
1. Explora los ejemplos en la carpeta `examples/` para ver implementaciones prácticas.
2. Resuelve los ejercicios en la carpeta `exercises/` para afianzar los conceptos.

## Recursos adicionales
- [Documentación oficial de Python: POO](https://docs.python.org/es/3/tutorial/classes.html)
- [Tutorial de POO en Python (en español)](https://www.programiz.com/python-programming/object-oriented-programming)

¡Explora, experimenta y domina la Programación Orientada a Objetos en Python!
