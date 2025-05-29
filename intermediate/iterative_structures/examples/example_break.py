"""
Ejemplo: Uso de break en un bucle

Descripción detallada:
Este ejemplo muestra cómo utilizar la instrucción break dentro de un bucle for en Python. El código imprime los números del 1 al 5, pero el bucle se interrumpe cuando i es igual a 4.
"""

if __name__ == "__main__":
    # Iteramos del 1 al 5
    for i in range(1, 6):
        if i == 4:
            break  # Sale del bucle cuando i es 4
        print(i)  # Imprime el valor de i mientras sea menor que 4
