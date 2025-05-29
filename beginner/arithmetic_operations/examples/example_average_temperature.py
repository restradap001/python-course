"""
Ejemplo: Promedio de temperaturas

Descripción detallada:
Este ejemplo calcula el promedio de temperaturas registradas durante una semana.
"""

if __name__ == "__main__":
    temperaturas = [22, 24, 19, 21, 23, 20, 18]
    promedio = sum(temperaturas) / len(temperaturas)
    print(f"Temperatura promedio: {promedio:.1f}°C")
