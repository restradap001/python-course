# Manejo de Errores en Python

## Descripción General
El manejo de errores permite que los programas gestionen situaciones inesperadas sin detenerse abruptamente. Python utiliza excepciones para señalar errores y permite capturarlos y gestionarlos con bloques `try`, `except`, `else` y `finally`.

## Estructura Básica
```python
try:
    # Código que puede causar un error
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero.")
else:
    print("No hubo errores.")
finally:
    print("Este bloque siempre se ejecuta.")
```

## Excepciones Comunes
- `ZeroDivisionError`: División por cero
- `ValueError`: Valor incorrecto
- `TypeError`: Tipo de dato incorrecto
- `FileNotFoundError`: Archivo no encontrado

## Buenas Prácticas
- Capturar solo las excepciones necesarias.
- Usar mensajes de error claros.
- Utilizar excepciones personalizadas cuando sea necesario.
