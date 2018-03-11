'''
Aprender lo que es el slicing.
'''

# Librerias
import numpy as np

# Slicing sirve para obtener varios elementos de la matriz ea la vez
lista = list(range(6,21))

# Slicing en numpy
matriz = np.zeros((10,10))
x,y = matriz.shape

val = 0
for i in range(x):
    for j in range(y):
        val+=1
        matriz[i,j] = val
print(matriz)

# Cuadrante superior izquierdo
# print(matriz[0:5,0:5])
matriz[:5,:5] = 1
print(matriz[:5,:5])

# Cuadrante superior derecho
matriz[:5,5:] = 2
print(matriz[:5,5:])

# Cuadrante inferior izquierdo
matriz[5:,:5] = 3
print(matriz[5:,:5])

# Cuadramte inferior derecho
matriz[5:,5:] = 4
print(matriz[5:,5:])

# Ejercicio de la cruz con puro slicing
matriz = np.zeros((11,11))
x,y = matriz.shape
xm = int(x/2)
ym = int(y/2)
n = 0
grosor = 2*n + 1


matriz[:,ym-n:ym+n+1] = 1
matriz[xm-n:xm+n+1,:] = 1

print(matriz)

