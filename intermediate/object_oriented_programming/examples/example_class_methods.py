"""
Ejemplo: Métodos de instancia en una clase

Descripción detallada:
Este ejemplo muestra cómo definir un método de instancia en una clase Calculadora que suma dos números. Se crea un objeto y se utiliza el método.
"""

if __name__ == "__main__":
    class Calculadora:
        def suma(self, a, b):
            return a + b
    calc = Calculadora()
    print(f"Suma: {calc.suma(3, 5)}")
