import imageio.v2 as imageio
import numpy as np
import math
#import matplotlib.pyplot as plt


def pregunta_1(image): 
    c_image = [[column[:] for column in row] for row in image] # Esta línea sirve para hacer una copia de la matriz original de la imagen
    heigth, width = len(image), len(image[0])
    for i in range(heigth):
        for j in range(width):
            rgb = [ rgb * 1.6 for rgb in c_image[i][j] ]
            rgb_filtered = [round(color) if color <= 255 else 255 for color in rgb ]
            c_image[i][j] = rgb_filtered
    return c_image

def pregunta_2(image): 
    c_image = [[column[:] for column in row] for row in image] # Esta línea sirve para hacer una copia de la matriz original de la imagen
    heigth, width = len(image), len(image[0])

    print(width, heigth)
    for i in range(heigth):
        for j in range(width):
            c_image[i][j] = image[i] [width - j - 1] # intercambiar pixeles
            c_image[i][j][0] = 0 # asignar 0 al canal Rojo
            c_image[i][j][2] = 0 # asinar 0 al canal Blue
    return c_image

def pregunta_3(image): 
    c_image = [[column[:] for column in row] for row in image] # Esta línea sirve para hacer una copia de la matriz original de la imagen
    heigth, width = len(image), len(image[0])

    for i in range(heigth):
        for j in range(width):
            red, green, blue = c_image[i][j][0], c_image[i][j][1], c_image[i][j][2]
            sepia_red = round(red * 0.393 + green * 0.769 + blue * 0.189)
            sepia_green = round(red * 0.349 + green * 0.686 + blue * 0.168)
            sepia_blue = round(red * 0.272 + green * 0.534 + blue * 0.131)
            c_image[i][j][0] = min(255, sepia_red)
            c_image[i][j][1] = min(255, sepia_green)
            c_image[i][j][2] = min(255, sepia_blue)
    return c_image

def pregunta_4(image): 
    c_image = [[column[:] for column in row] for row in image] # Esta línea sirve para hacer una copia de la matriz original de la imagen
    heigth, width = len(image), len(image[0])
    print(f"{width} x {heigth}")
    center_y, center_x = heigth // 2, width // 2
    print(f"{center_x} x {center_y}")
    for i in range(heigth):
        for j in range(width):
            if i <= heigth - 1 and j <= width - 1:
                if not (j - center_x) **2 + (i - center_y)**2 < (heigth//2)**2:
                    c_image[i][j] = [0, 0, 0]
            
    return c_image

if __name__ == "__main__":
    image_path = "tarea3/images/playa.bmp"
    image = imageio.imread(image_path)
    pregunta_1(image)