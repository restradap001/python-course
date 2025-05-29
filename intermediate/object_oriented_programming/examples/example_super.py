"""
Ejemplo: Uso de super() en herencia

Descripción detallada:
Este ejemplo muestra cómo usar super() para llamar al constructor de la clase base Vehiculo desde la clase derivada Auto.
"""

if __name__ == "__main__":
    class Vehiculo:
        def __init__(self, marca):
            self.marca = marca

    class Auto(Vehiculo):
        def __init__(self, marca, modelo):
            super().__init__(marca)
            self.modelo = modelo

    a = Auto("Toyota", "Corolla")
    print(f"Marca: {a.marca}")
    print(f"Modelo: {a.modelo}")
