# Listas en Python

## Descripción General
Las listas son colecciones ordenadas y mutables de elementos. Permiten almacenar cualquier tipo de dato y modificar su contenido.

## Operaciones Comunes
- Crear: `lista = [1, 2, 3]`
- Acceder: `lista[0]`
- Modificar: `lista[1] = 5`
- Agregar: `lista.append(4)`
- Eliminar: `lista.remove(2)`
- Slicing: `lista[1:3]`
- Iterar: `for x in lista: ...`

## Ejemplo
```python
frutas = ["manzana", "pera", "naranja"]
frutas.append("plátano")
for fruta in frutas:
    print(fruta)
```

## Buenas Prácticas
- Usar nombres descriptivos para las listas.
- No mezclar tipos de datos en una misma lista si no es necesario.
