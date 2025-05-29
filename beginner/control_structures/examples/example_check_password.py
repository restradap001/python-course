"""
Ejemplo: Verificación de contraseña

Descripción detallada:
Este ejemplo muestra cómo comparar una contraseña ingresada con la contraseña correcta usando una estructura if.
"""

if __name__ == "__main__":
    contrasena_correcta = "python123"
    contrasena_ingresada = "python123"
    if contrasena_ingresada == contrasena_correcta:
        print("Acceso concedido.")
    else:
        print("Acceso denegado.")
