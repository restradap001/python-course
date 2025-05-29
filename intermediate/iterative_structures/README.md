# Estructuras Iterativas en Python

## Descripción General
Las estructuras iterativas permiten repetir un bloque de código varias veces. En Python, los bucles más usados son `for` y `while`.

## Bucle for
Itera sobre secuencias (listas, strings, rangos, etc.).
```python
for i in range(5):
    print(i)
```

## Bucle while
Repite mientras una condición sea verdadera.
```python
n = 0
while n < 5:
    print(n)
    n += 1
```

## Control de bucles
- `break`: Sale del bucle
- `continue`: Salta a la siguiente iteración

## Buenas Prácticas
- Evitar bucles infinitos.
- Usar bucles para procesar listas y colecciones.
