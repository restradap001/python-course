"""
Ejemplo: Validación simple de correo electrónico

Descripción detallada:
Este ejemplo muestra cómo verificar si una cadena contiene el carácter '@' para validar un correo electrónico de manera básica.
"""

if __name__ == "__main__":
    correo = "usuario@ejemplo.com"
    if "@" in correo:
        print("Correo válido.")
    else:
        print("Correo inválido.")
