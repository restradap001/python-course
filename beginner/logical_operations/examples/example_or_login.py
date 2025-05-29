"""
Ejemplo: Acceso con usuario o correo

Descripción detallada:
Este ejemplo utiliza el operador lógico or para permitir el acceso si el usuario ingresa su nombre de usuario o su correo electrónico correctamente.
"""

if __name__ == "__main__":
    usuario = "juan"
    correo = "juan@mail.com"
    entrada = "juan"
    if entrada == usuario or entrada == correo:
        print("Acceso correcto.")
    else:
        print("Acceso incorrecto.")
