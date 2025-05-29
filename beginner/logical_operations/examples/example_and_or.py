"""
Ejemplo: Uso combinado de and y or

Descripción detallada:
Este ejemplo muestra cómo combinar los operadores and y or para validar el acceso a un sistema.
"""

if __name__ == "__main__":
    usuario = "admin"
    clave = "1234"
    activo = True
    if (usuario == "admin" and clave == "1234") or activo:
        print("Acceso al sistema.")
    else:
        print("Acceso denegado.")
