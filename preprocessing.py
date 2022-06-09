from turtle import left
import numpy as np
import cv2
import pandas as pd
import os

# PATHS DESTINO
destFacesPath = './Preprocesado/Ojos/'
destNoEyesPath = './Preprocesado/No_ojos/'

#CREANDO ENTORNO
os.mkdir("Preprocesado")
os.mkdir(destFacesPath)
os.mkdir(destNoEyesPath)


# CARGAR NOMBRES DE LAS IMAGENES
facesPath = './Cares/'
noEyesPath = './No_ulls/'
faceImages = os.listdir(facesPath)
NoEyesImages = os.listdir(noEyesPath)

print("CARAS:\n",faceImages)
print("SIN OJOS:\n",noEyesPath)
i=0
#PREPROCESSING POR CADA IMAGEN DE CARAS
for name in faceImages:
    img = cv2.imread(facesPath+name)
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    leftEye = imgray[413:413+32*4, 284:284+4*48]
    rightEye = imgray[413:413+32*4, 550:550+4*48]
    leftEye = cv2.resize(leftEye,(48,32))
    rightEye = cv2.resize(rightEye,(48,32))
    cv2.imwrite(destFacesPath+str(i)+'L.jpg', leftEye)
    cv2.imwrite(destFacesPath+str(i)+'R.jpg', rightEye)
    i+=1

#PREPROCESSING POR CADA IMAGEN SIN OJOS
for name in NoEyesImages:
    img = cv2.imread(noEyesPath+name)
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgray = cv2.resize(imgray,(48,32))
    cv2.imwrite(destNoEyesPath+str(i)+'.jpg', imgray)
    i+=1