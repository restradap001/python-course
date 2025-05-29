"""
Ejemplo: Herencia entre clases

Descripción detallada:
Este ejemplo muestra cómo una clase Perro puede heredar de una clase Animal y redefinir el método hablar.
"""

if __name__ == "__main__":
    class Animal:
        def hablar(self):
            print("El animal hace un sonido")

    class Perro(Animal):
        def hablar(self):
            print("Guau!")

    p = Perro()
    p.hablar()
