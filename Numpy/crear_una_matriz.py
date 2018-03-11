'''
Ejercicios de matrices

Instalar numpy:
    pip install numpy
'''

# Librerias
import numpy as np

# Definir una matriz
# Matriz llena de ceros
# np.zeros((filas,columnas,...,n))
matriz = np.zeros((2,5))

# Llenar la matriz de unos
unos = np.ones((2,5))
# print(unos)

# Dimensiones de la matriz
x,y = matriz.shape   # Se da el valor de la dimension para x y y
# print(x,y)

# LLenar la matriz con valores
for i in range(x):
    for j in range(y):
        val = i+j
        # la siguiente linea accede al elemento i,j de la matriz
        # y le adigna un valor
        matriz[i,j] = val

# print(matriz)

# Ejercicio 1 llenar un matriz diagonal
print("Ejercicio Diagonal")
diagonal = np.zeros((5,5))
x,y= diagonal.shape

for i in range(x):
    # Llena la matriz en la diagonal con 1s
    diagonal[i,i] = 1

# print(diagonal)

# Ejercicio 2 contar las casillas de una matriz
matriz = np.zeros((5,5))
x,y = matriz.shape

val = 0
for i in range(x):
    for j in range(y):
        val +=1
        matriz[i,j] = val

print(matriz)

## Slicing

# Ejercicio 3. Llenar una matriz triangular por abajo
triangular = np.zeros((5,5))
x,y = triangular.shape

for i in range(x):
    for j in range(y):
        if j <= i:
            triangular[i,j] = 1

print("\nMatriz triangular inferior\n")
print(triangular)

# Ejericio 4. LLenar una matriz triangular por arriba
triangular = np.zeros((5,5))
x,y = triangular.shape

for i in range(x):
    for j in range(y):
        if i <= j:
            triangular[i,j] = 1

print("\nMatriz triangular superior")
print(triangular)

# Ejercicio. Hacer una forma de cruz con una matriz
cruz = np.zeros((8,8))
x,y = cruz.shape

# Encuentra la posicion de la mitad de la matriz, poara cada dimension
ym = int(y/2)
xm = int(x/2)

# Recorre la matriz horizontalmente, sobre la linea de en medio
for i in range(x):
    cruz[i,ym] = 1
    cruz[i,ym-1] = 1

# Recorre la matriz verticalmente, sobre la linea de en medio
for j in range(y):
    cruz[xm,j] = 1
    cruz[xm-1,j] = 1

print(cruz)

