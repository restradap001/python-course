"""
Ejemplo: Modificar una lista

Descripción detallada:
Este ejemplo muestra cómo modificar elementos de una lista asignando un nuevo valor a un índice específico. El código cambia la segunda fruta de la lista y muestra la lista actualizada, ilustrando que las listas son mutables en Python.
"""

if __name__ == "__main__":
    # Creamos una lista de frutas
    frutas = ['apple', 'banana', 'cherry']
    # Modificamos el segundo elemento
    frutas[1] = 'orange'
    # Imprimimos la lista actualizada
    print(frutas)
