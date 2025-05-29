# Estructuras de Control en Python

## Descripción General
Las estructuras de control permiten modificar el flujo de ejecución de un programa. En Python, las más comunes son las condicionales (`if`, `elif`, `else`) y los bucles (`for`, `while`).

## Condicionales
Permiten ejecutar bloques de código solo si se cumple una condición.
```python
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

## Bucles
Permiten repetir acciones múltiples veces.
- **for**: Itera sobre una secuencia (lista, string, rango, etc.).
- **while**: Repite mientras una condición sea verdadera.

```python
for i in range(5):
    print(i)

n = 0
while n < 5:
    print(n)
    n += 1
```

## Aplicaciones Comunes
- Validación de datos
- Repetición de tareas
- Procesamiento de listas y colecciones

## Buenas Prácticas
- Usar indentación correcta (4 espacios por nivel).
- Evitar bucles infinitos.
- Utilizar `break` y `continue` para controlar el flujo dentro de los bucles.
