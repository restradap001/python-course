"""
Ejemplo: Cálculo de precio con descuento

Descripción detallada:
Este ejemplo muestra cómo calcular el precio final de un producto aplicando un descuento porcentual.
"""

if __name__ == "__main__":
    precio = 150.0
    descuento = 0.2  # 20%
    precio_final = precio * (1 - descuento)
    print(f"Precio final con descuento: ${precio_final:.2f}")
