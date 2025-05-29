"""
Ejemplo: Condiciones combinadas para descuento

Descripción detallada:
Este ejemplo utiliza operadores lógicos para determinar si un cliente recibe un descuento especial.
"""

if __name__ == "__main__":
    es_cliente_frecuente = True
    tiene_cupon = False
    if es_cliente_frecuente or tiene_cupon:
        print("Descuento aplicado.")
    else:
        print("No tienes descuento.")
