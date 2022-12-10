# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 22:11:00 2021

@author: Jordy Andres
"""

#Librería opencv
import cv2
path1 = '.\\Img_video\\'

#Arreglo vacío
img_array = []
x=2878
#For para leer imagenes desde un directorio
while(x<=2878+1305):
    path = path1+'IMG_%04d.jpg' % x
    img = cv2.imread(path)
    img_array.append(img)
    print(x)
    x+=1
#Tamaño de la última imagen alto y ancho

video = cv2.VideoWriter('Videofinal2.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (1920,1080))

#For para guardar frames en un video
for i in range(len(img_array)):
    video.write(img_array[i])
    print(i)

video.release() 