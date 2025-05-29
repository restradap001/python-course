# Colecciones avanzadas

## Descripción General
Además de listas y diccionarios, Python ofrece otras colecciones útiles como conjuntos (`set`), tuplas (`tuple`) y comprensión de listas/diccionarios para manipular datos de forma eficiente.

## Tipos principales
- **Tuplas (`tuple`)**: Secuencias inmutables de elementos.
- **Conjuntos (`set`)**: Colecciones no ordenadas de elementos únicos.
- **Comprensión de listas y diccionarios**: Sintaxis concisa para crear nuevas colecciones a partir de otras.

## Ejemplo
```python
# Tupla
coordenadas = (10, 20)
# Set
frutas = {"manzana", "pera", "manzana"}  # {'manzana', 'pera'}
# Comprensión de listas
cuadrados = [x*x for x in range(5)]
```

## Buenas Prácticas
- Usa tuplas para datos que no deben cambiar.
- Utiliza sets para eliminar duplicados.
- Prefiere comprensiones para crear colecciones de forma clara y eficiente.
