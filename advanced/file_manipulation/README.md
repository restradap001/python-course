# Manipulación de Archivos en Python

## Descripción General
La manipulación de archivos permite leer, escribir y modificar archivos en disco. Python ofrece funciones integradas para trabajar con archivos de texto y binarios.

## Operaciones Básicas
- **Abrir archivo**: `open('archivo.txt', 'r')`
- **Leer archivo**: `read()`, `readline()`, `readlines()`
- **Escribir archivo**: `write()`, `writelines()`
- **Cerrar archivo**: `close()` (o usar `with` para cerrar automáticamente)

## Ejemplo
```python
with open('datos.txt', 'w') as f:
    f.write('Hola mundo\n')

with open('datos.txt', 'r') as f:
    contenido = f.read()
    print(contenido)
```

## Buenas Prácticas
- Usar `with` para abrir archivos y asegurar su cierre.
- Manejar excepciones al trabajar con archivos.
- Verificar la existencia del archivo antes de leerlo.
