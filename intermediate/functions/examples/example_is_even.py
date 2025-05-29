"""
Ejemplo: Función para verificar si un número es par

Descripción detallada:
Este ejemplo muestra cómo definir una función que verifica si un número es par y retorna True o False.
"""

if __name__ == "__main__":
    def is_even(n):
        # Retorna True si n es par, False si es impar
        return n % 2 == 0
    print(is_even(4))  # True
    print(is_even(5))  # False
