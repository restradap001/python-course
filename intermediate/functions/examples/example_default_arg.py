"""
Ejemplo: Función con argumento por defecto

Descripción detallada:
Este ejemplo muestra cómo definir una función con un argumento que tiene un valor por defecto en Python. La función power eleva un número base a un exponente, que por defecto es 2.
"""

if __name__ == "__main__":
    def power(base, exponent=2):
        # Retornamos base elevado a exponent
        return base ** exponent
    print(power(3))      # 3^2 = 9
    print(power(2, 3))   # 2^3 = 8
