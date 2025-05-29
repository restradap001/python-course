"""
Ejemplo: Acceso permitido con condiciones lógicas

Descripción detallada:
Este ejemplo muestra cómo usar operadores lógicos para permitir el acceso solo si el usuario es mayor de edad y tiene invitación.
"""

if __name__ == "__main__":
    edad = 20
    tiene_invitacion = True
    if edad >= 18 and tiene_invitacion:
        print("Acceso permitido.")
    else:
        print("Acceso denegado.")
