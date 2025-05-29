"""
Ejemplo: Métodos estáticos en una clase

Descripción detallada:
Este ejemplo muestra cómo definir y utilizar un método estático en una clase Matematica para calcular el cuadrado de un número.
"""

if __name__ == "__main__":
    class Matematica:
        @staticmethod
        def cuadrado(x):
            return x * x

    print(f"Cuadrado de 6: {Matematica.cuadrado(6)}")
