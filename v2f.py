# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 15:32:12 2021

@author: Jordy Andres
"""

import cv2

capture = cv2.VideoCapture('Home2School_1.mp4')
cont = 0
path = '.\\Frames\\'

while (capture.isOpened()):
    ret, frame = capture.read()
    if (ret == True):
        cv2.imwrite(path + 'IMG_%04d.jpg' % cont, frame)    
        cont += 1
        if (cv2.waitKey(1) == ord('s')):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()