# Diccionarios en Python

## Descripción General
Los diccionarios son estructuras de datos que almacenan pares clave-valor. Permiten acceder, modificar y eliminar elementos de forma eficiente usando la clave.

## Características
- Las claves deben ser únicas e inmutables (strings, números, tuplas).
- Los valores pueden ser de cualquier tipo.

## Operaciones Comunes
- Crear: `d = {"nombre": "Ana", "edad": 30}`
- Acceder: `d["nombre"]`
- Modificar: `d["edad"] = 31`
- Agregar: `d["ciudad"] = "Madrid"`
- Eliminar: `del d["nombre"]`
- Iterar: `for clave, valor in d.items(): ...`

## Ejemplo
```python
persona = {"nombre": "Ana", "edad": 30}
persona["profesion"] = "Ingeniera"
for clave, valor in persona.items():
    print(clave, valor)
```

## Buenas Prácticas
- Usar claves descriptivas.
- Validar la existencia de una clave antes de acceder (`in`).
