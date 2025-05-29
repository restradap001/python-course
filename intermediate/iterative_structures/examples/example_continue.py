"""
Ejemplo: Uso de continue en un bucle

Descripción detallada:
Este ejemplo muestra cómo utilizar la instrucción continue dentro de un bucle for en Python. El código imprime los números del 1 al 5, excepto el 3, ya que cuando i es igual a 3 se salta esa iteración.
"""

if __name__ == "__main__":
    # Iteramos del 1 al 5
    for i in range(1, 6):
        if i == 3:
            continue  # Salta la iteración cuando i es 3
        print(i)  # Imprime el valor de i si no es 3
