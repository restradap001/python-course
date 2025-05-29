# Tipos de Datos en Python

## Descripción General
Los tipos de datos definen la naturaleza de los valores que puede manejar un programa. Python es un lenguaje de tipado dinámico, lo que significa que no necesitas declarar el tipo de una variable explícitamente.

## Tipos de Datos Básicos
- **int**: Números enteros (por ejemplo, 5, -3, 0)
- **float**: Números decimales (por ejemplo, 3.14, -0.001)
- **str**: Cadenas de texto (por ejemplo, "Hola", 'Python')
- **bool**: Booleanos (True o False)
- **NoneType**: Representa la ausencia de valor (None)

## Conversión de Tipos
Puedes convertir entre tipos usando funciones como `int()`, `float()`, `str()`, `bool()`.

## Ejemplo
```python
x = 5
print(type(x))  # <class 'int'>
y = float(x)
print(type(y))  # <class 'float'>
```

## Buenas Prácticas
- Usar el tipo de dato adecuado para cada situación.
- Validar y convertir datos de entrada cuando sea necesario.
