"""
Ejemplo: Recomendación según temperatura

Descripción detallada:
Este ejemplo utiliza una estructura condicional para recomendar ropa según la temperatura.
"""

if __name__ == "__main__":
    temperatura = 12
    if temperatura < 10:
        print("Lleva abrigo.")
    elif temperatura < 20:
        print("Lleva una chaqueta ligera.")
    else:
        print("Ropa ligera es suficiente.")
