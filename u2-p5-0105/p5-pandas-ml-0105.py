import numpy as np
import pandas as pd

# Iker Montoya NC 0105

# Datos Matriz
datos_alumno = [
    [100, 80, 10],
    [90, 70, 7],
    [120, 100, 14],
    [80, 50, 2],
]

# Poner nombre de las columnas
# y almacenar la tabla en la variable df (DataFrame)
print("datos a partir de una matrix 4x3---")
df = pd.DataFrame(datos_alumno, columns=["ci", "marcas", "paquete"])
print(df)

# Datos a partir de un diccionario
print("---datos apartir de un diccionario----")
alumno_diccionario = {
    "nombre": ["Iker", "pedro", "joel", "nicole", "dilan", "jesse"],
    "califa": [60, 90, 100, 80, 70, 85],
    "edad": [64, 15, 16, 16, 18, 14]
}

estudiantes = pd.DataFrame(alumno_diccionario)
print(estudiantes)

print("Iker Montoya NC 0105")