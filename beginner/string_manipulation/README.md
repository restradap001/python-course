# Manipulación de Cadenas en Python

## Descripción General
Las cadenas de texto (strings) son uno de los tipos de datos más utilizados. Python ofrece múltiples métodos para manipular, analizar y transformar cadenas.

## Operaciones Comunes
- **Concatenación**: Unir cadenas con `+` o `join()`
- **Slicing**: Extraer subcadenas usando índices
- **Cambio de mayúsculas/minúsculas**: `upper()`, `lower()`, `capitalize()`
- **Reemplazo**: `replace()`
- **Búsqueda**: `find()`, `in`, `count()`
- **Eliminación de espacios**: `strip()`, `lstrip()`, `rstrip()`

## Ejemplo
```python
texto = "  Hola Mundo  "
print(texto.strip().upper())  # 'HOLA MUNDO'
```

## Buenas Prácticas
- Usar f-strings para formatear cadenas.
- Validar y limpiar entradas de usuario.
