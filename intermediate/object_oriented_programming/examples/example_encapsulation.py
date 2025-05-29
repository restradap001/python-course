"""
Ejemplo: Encapsulamiento de atributos

Descripción detallada:
Este ejemplo muestra cómo definir un atributo privado en una clase CuentaBancaria y cómo acceder a él mediante un método público.
"""

if __name__ == "__main__":
    class CuentaBancaria:
        def __init__(self, saldo):
            self.__saldo = saldo  # atributo privado
        def mostrar_saldo(self):
            print(f"Saldo: {self.__saldo}")

    cuenta = CuentaBancaria(1000)
    cuenta.mostrar_saldo()
