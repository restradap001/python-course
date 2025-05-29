"""
Ejemplo: Combinación de operadores lógicos y de comparación

Descripción detallada:
Este ejemplo muestra cómo combinar operadores lógicos y de comparación para evaluar condiciones complejas. Se verifica si un número es mayor que 10 y par.
"""

if __name__ == "__main__":
    num = 12  # Número a evaluar
    resultado = num > 10 and num % 2 == 0  # ¿Mayor que 10 y par?
    print(f"num > 10 y par: {resultado}")
