# -*- coding: utf-8 -*-


# Convolutional Neural Network

# Installing Theano
# pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# Installing Tensorflow
# pip install tensorflow

# Installing Keras
# pip install --upgrade keras

# Part 1 - Building the CNN

# Importing the Keras libraries and packages


from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Dropout


# Initialising the CNN
classifier = Sequential()

# Step 1 - Convolution
#classifier.add(Conv2D(#Filtros, (xMascara, Ymascara), input_shape = (xImagen, YImagen, RGB), activation = 'relu'))
classifier.add(Conv2D(128, (5, 5), input_shape = (128,128, 3), activation = 'relu'))

# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))
classifier.add(Dropout(0.2))

# Adding a second convolutional layer
classifier.add(Conv2D(64, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))
classifier.add(Dropout(0.2))


# Adding a second convolutional layer
classifier.add(Conv2D(64, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))
classifier.add(Dropout(0.2))

# Step 3 - Flattening
classifier.add(Flatten())


# Step 4 - Full connection

classifier.add(Dense(units = 512, activation = 'relu'))
classifier.add(Dense(units = 512, activation = 'relu'))
classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))

# Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])


# Part 2 - Fitting the CNN to the images

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)



training_set = train_datagen.flow_from_directory('C:/Users/Jordy Andres/Desktop/Juan/8vo/Deep Learning/Lab_Final/Entrenamiento',target_size = (128, 128), batch_size = 32, class_mode = 'binary')

test_set = test_datagen.flow_from_directory('C:/Users/Jordy Andres/Desktop/Juan/8vo/Deep Learning/Lab_Final/Prueba', target_size = (128,128), batch_size = 32,  class_mode = 'binary')


classifier.fit_generator(training_set, steps_per_epoch = 92, epochs = 4,  validation_steps = 6)


import numpy as np
from keras.preprocessing import image
from keras.models import load_model
classifier = load_model('Red_128_128.h5')
test_image = image.img_to_array(image.load_img('C:/Users/Jordy Andres/Desktop/Juan/8vo/Deep Learning/Lab_Final/Prueba/Test2/img4.JPG', target_size = (128, 128)))

import matplotlib.pyplot as plt
plt.imshow(test_image/255)
test_image = np.expand_dims(test_image, axis = 0)



result = classifier.predict(test_image)
print(result)
xx=training_set.class_indices
print(xx)
if result[0][0] == 1:
    prediction = 'Carron´t'
    print(prediction)
else:
    prediction = 'Carro'
    print(prediction)
    
    
#classifier.save("Red_Cat&Dog_100_100.h5")

#  Guarda la Red   
#classifier.save("Red_256_256.h5")  
    
#Cuadritos
#Dim1 600x250
#Dim2 300x125
#Dim3 150x62
#Dim4 50x55
#Área 393:784,1:1920
import cv2
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Dropout
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from keras.preprocessing import image
from keras.models import load_model
import matplotlib.pyplot as plt

classifier = load_model('Red_128_128.h5')

cont=881
cont2=0
flag=1
inia=393
inii=1
path = '.\\Frames\\'
path2 = '.\\Img_video\\'
while(cont<=1794):
    imagen = cv2.imread(path+'IMG_%04d.jpg' % cont)
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
            test_image = image.img_to_array(cv2.resize(cuadrito, dsize=(256, 256)))
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
"""  
    
# Salvar la arquitectura de la red y los pesos   
from keras.models import model_from_json
# serialize model to JSON
netCatDog_V2_json = classifier.to_json()
with open("redGatosPerros.json", "w") as json_file:
    json_file.write(netCatDog_V2_json)
# serialize weights to HDF5
classifier.save_weights("netCatDog_V2_json.h5")
print("Saved red to disk")

"""

