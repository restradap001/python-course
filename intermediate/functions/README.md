# Funciones en Python

## Descripción General
Las funciones permiten agrupar instrucciones bajo un nombre y reutilizarlas. Facilitan la organización, legibilidad y mantenimiento del código.

## Definición y Uso
- Se definen con la palabra clave `def`.
- Pueden recibir argumentos y devolver valores con `return`.

## Ejemplo
```python
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Ana")
```

## Argumentos y Parámetros
- Posicionales y nombrados
- Valores por defecto
- Argumentos variables (`*args`, `**kwargs`)

## Buenas Prácticas
- Usar nombres descriptivos para funciones y parámetros.
- Documentar con docstrings.
- Evitar funciones demasiado largas.
