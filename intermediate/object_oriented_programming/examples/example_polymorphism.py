"""
Ejemplo: Polimorfismo con clases

Descripción detallada:
Este ejemplo muestra cómo dos clases pueden compartir el mismo método (hablar) y cómo una función puede invocar ese método sin importar el tipo de objeto.
"""

if __name__ == "__main__":
    class Ave:
        def hablar(self):
            print("Pío")
    class Loro(Ave):
        def hablar(self):
            print("Hola")

    def hacer_hablar(ave):
        ave.hablar()

    hacer_hablar(Ave())
    hacer_hablar(Loro())
