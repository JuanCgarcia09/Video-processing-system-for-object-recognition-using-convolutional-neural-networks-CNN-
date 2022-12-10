# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 22:51:27 2021

@author: Jordy Andres
"""

import cv2

import numpy as np
from keras.preprocessing import image
from keras.models import load_model


classifier = load_model('Red_128_128.h5')

cont=3200
cont2=0
flag=1
inia=393
inii=1
path = '.\\Frames\\'
path2 = '.\\Img_video\\'
while(cont<=3300):
    imagen = cv2.imread(path+'IMG_%04d.jpg' % cont)
    cont2=0
    while(cont2<=2):
        inia=393
        inii=1
        while(flag):
            if(cont2==0):
                alto=250
                ancho=600
                cuadrito=imagen[inia:inia+alto,inii:inii+ancho]
                inii+=30
            if(cont2==1):
                alto=125
                ancho=300
                cuadrito=imagen[inia:inia+alto,inii:inii+ancho]
                inii+=30
            if(cont2==2):
                alto=62
                ancho=150
                cuadrito=imagen[inia:inia+alto,inii:inii+ancho]
                inii+=30
            if(cont2==3):
                alto=55
                ancho=50
                cuadrito=imagen[inia:inia+alto,inii:inii+ancho]
                inii+=30
            test_image = image.img_to_array(cv2.resize(cuadrito, dsize=(128, 128)))
            test_image = np.expand_dims(test_image, axis = 0)
            result = classifier.predict(test_image)
            if result[0][0] == 1:
                prediction = 'Carron´t'
            else:
                prediction = 'Carro'
                inii+=ancho
                start_point = (inii, inia)
                end_point = (inii+ancho, inia+alto)
                color = (255, 0, 0)
                thickness = 2
                imageout = cv2.rectangle(imagen, start_point, end_point, color, thickness)   
            if(inii+ancho>1920):
                inii=0
                if(inia+alto>784):
                    flag=0
                else:
                    inia+=alto
        cont2+=1
        flag=1
    cv2.imwrite(path2 + 'IMG_%04d.jpg' % cont, imageout)
    cont+=1