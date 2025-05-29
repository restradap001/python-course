"""
Ejemplo: Atributos de clase vs atributos de instancia

Descripción detallada:
Este ejemplo muestra la diferencia entre un atributo de clase (especie) y un atributo de instancia (nombre) en la clase Mascota.
"""

if __name__ == "__main__":
    class Mascota:
        especie = "Perro"  # atributo de clase
        def __init__(self, nombre):
            self.nombre = nombre  # atributo de instancia
    m1 = Mascota("Fido")
    print(f"Nombre: {m1.nombre}")
    print(f"Especie: {m1.especie}")
