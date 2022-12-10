# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 15:44:06 2021

@author: Jordy Andres
"""

import cv2

path = '.\\Frames\\'

path2 = '.\\Carros\\'

path3 = '.\\Nocarros\\'

cont = 0
#Para carros
"""
while(cont<=720):
    image = cv2.imread(path+'IMG_%04d.jpg' % cont)
    imageout = image[450:550+150,200:600+200]
    cv2.imwrite(path2 + 'IMG_%04d.jpg' % cont, imageout)
    cont += 1
    image = cv2.imread(path+'IMG_%04d.jpg' % cont)
    imageout = image[550:550+200,1120:1200+280]
    cv2.imwrite(path2 + 'IMG_%04d.jpg' % cont, imageout)
    cont += 1
    image = cv2.imread(path+'IMG_%04d.jpg' % cont)
    imageout = image[505:450+110,50:50+50]
    cv2.imwrite(path2 + 'IMG_%04d.jpg' % cont, imageout)
    cont += 1
    image = cv2.imread(path+'IMG_%04d.jpg' % cont)
    imageout = image[505:450+110,100:100+50]
    cv2.imwrite(path2 + 'IMG_%04d.jpg' % cont, imageout)
    cont += 1
    image = cv2.imread(path+'IMG_%04d.jpg' % cont)
    imageout = image[515:515+70,1800:1700+250]
    cv2.imwrite(path2 + 'IMG_%04d.jpg' % cont, imageout)
    cont += 1
"""
#Para carrosn't
"""
while(cont<=720):
    image = cv2.imread(path+'IMG_%04d.jpg' % cont)
    imageout = image[555:450+160,50:50+50]
    cv2.imwrite(path3 + 'IMG_%04d.jpg' % cont, imageout)
    cont += 1
    image = cv2.imread(path+'IMG_%04d.jpg' % cont)
    imageout = image[450:550+150,750:550+600]
    cv2.imwrite(path3 + 'IMG_%04d.jpg' % cont, imageout)
    cont += 1
    image = cv2.imread(path+'IMG_%04d.jpg' % cont)
    imageout = image[550+50:550+200+50,1120+80+280:1200+280+80+280]
    cv2.imwrite(path3 + 'IMG_%04d.jpg' % cont, imageout)
    cont += 1
    image = cv2.imread(path+'IMG_%04d.jpg' % cont)
    imageout = image[515-100:515+70-100,1800:1700+250]
    cv2.imwrite(path3 + 'IMG_%04d.jpg' % cont, imageout)
    cont += 1
    image = cv2.imread(path+'IMG_%04d.jpg' % cont)
    imageout = image[450+100:550+130,200-200:600+200-600]
    cv2.imwrite(path3 + 'IMG_%04d.jpg' % cont, imageout)
    cont += 1
    #6
    image = cv2.imread(path+'IMG_%04d.jpg' % cont)
    imageout = image[450:550+150,600+200:800+200]
    cv2.imwrite(path3 + 'IMG_%04d.jpg' % cont, imageout)
    cont += 1
    image = cv2.imread(path+'IMG_%04d.jpg' % cont)
    imageout = image[450:550+150,600+200+100:800+200+100]
    cv2.imwrite(path3 + 'IMG_%04d.jpg' % cont, imageout)
    cont += 1
    image = cv2.imread(path+'IMG_%04d.jpg' % cont)
    imageout = image[450-200:550+150-200,200:600+200]
    cv2.imwrite(path3 + 'IMG_%04d.jpg' % cont, imageout)
    cont += 1
    image = cv2.imread(path+'IMG_%04d.jpg' % cont)
    imageout = image[515-50:515+70-50,1800:1700+250]
    cv2.imwrite(path3 + 'IMG_%04d.jpg' % cont, imageout)
    cont += 1
    image = cv2.imread(path+'IMG_%04d.jpg' % cont)
    imageout = image[500+100:500+200,1480+100:12480+280-50-100]
    cv2.imwrite(path3 + 'IMG_%04d.jpg' % cont, imageout)
    cont += 1
"""
image = cv2.imread(path+'IMG_2000.jpg')
print('image.shape =',image.shape)
#Camioneta azul

#imageout = image[450:550+150,200:600+200]

#Camioneta gris

#imageout = image[550:550+200,1120:1200+280]

#Camioneta blanca

#imageout = image[505:450+110,50:50+50]

#Carro blanco

#imageout = image[505:450+110,100:100+50]

#Camioneto blanco mediano

#imageout = image[515:515+70,1800:1700+250]

#Algo1

#imageout = image[555:450+160,50:50+50]

#Algo2

#imageout = image[450:550+150,750:550+600]

#Algo3

#imageout = image[550+50:550+200+50,1120+80+280:1200+280+80+280]

#Algo4

#imageout = image[515-100:515+70-100,1800:1700+250]

#Algo5

#imageout = image[450+100:550+130,200-200:600+200-600]

#Algo5

#imageout = image[515+80:515+70+80,1800:1700+250]

#Algo6

#imageout = image[450:550+150,600+200:800+200]

#Algo7

#imageout = image[450:550+150,600+200+100:800+200+100]

#Algo8

#imageout = image[450-200:550+150-200,200:600+200]

#Algo9

#imageout = image[515-50:515+70-50,1800:1700+250]

#Algo10

#imageout = image[500+100:500+200,1480+100:12480+280-50-100]

#Área 

imageout=image[393:784,1:1920]

print('imageout.shape =',imageout.shape)

cv2.imshow('imagen_recortada',imageout)