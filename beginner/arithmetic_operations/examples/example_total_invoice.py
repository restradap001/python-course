"""
Ejemplo: Cálculo del total de una factura

Descripción detallada:
Este ejemplo muestra cómo sumar los precios de varios productos y calcular el total de una factura, incluyendo el IVA.
"""

if __name__ == "__main__":
    # Lista de precios de productos
    precios = [12.5, 8.99, 3.75]
    subtotal = sum(precios)
    iva = subtotal * 0.16
    total = subtotal + iva
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"IVA: ${iva:.2f}")
    print(f"Total a pagar: ${total:.2f}")
