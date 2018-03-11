'''
Requisitos:
    pip install pillow (PIL - Python Iamge Library)
'''

# Librerias
import numpy as np
from PIL import Image

# Crear la imagen de una cruz
matriz = np.zeros((512,512))
x,y = matriz.shape
n = 200 
xm = int(x/2)
ym = int(y/2)

# Se crea una cruz
matriz[xm-n:xm+n+1,:] = 255
matriz[:,ym-n:ym+n+1] = 100

# Se escribe una imagen
# Esta libreria puede guardar extensiones PNG y JPG (uint8)
img = Image.fromarray(matriz.astype("uint8"))
img.save("huaraches_00%s.png"%contador)

