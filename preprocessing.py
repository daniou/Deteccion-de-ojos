from turtle import left
import numpy as np
import cv2
import pandas as pd
import os

finalImageSize = (32,48)

#PATHS DESTINO
destFacesPath = './Preprocesado/Ojos/'
destNoEyesPath = './Preprocesado/No_ojos/'

#CREANDO ENTORNO
os.mkdir("Preprocesado")
os.mkdir(destFacesPath)
os.mkdir(destNoEyesPath)


#CARGAR NOMBRES DE LAS IMAGENES
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
    leftEye = imgray[413:413+finalImageSize[1]*4, 284:284+4*finalImageSize[0]]
    rightEye = imgray[413:413+finalImageSize[1]*4, 550:550+4*finalImageSize[0]]
    leftEye = cv2.resize(leftEye,finalImageSize)
    rightEye = cv2.resize(rightEye,finalImageSize)
    cv2.imwrite(destFacesPath+str(i)+'L.jpg', leftEye)
    cv2.imwrite(destFacesPath+str(i)+'R.jpg', rightEye)
    i+=1

#PREPROCESSING POR CADA IMAGEN SIN OJOS
for name in NoEyesImages:
    img = cv2.imread(noEyesPath+name)
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    maxY=int(imgray.shape[0]/finalImageSize[0])
    maxX=int(imgray.shape[1]/finalImageSize[1])
    for stepY in range(maxY):
        for stepX in range(maxX):
            cropped = imgray[stepY*finalImageSize[0]:(stepY+1)*finalImageSize[0], 
                            stepX*finalImageSize[1]:(stepX+1)*finalImageSize[1]]
            cv2.imwrite(destNoEyesPath+str(i)+'.jpg', cropped)
            i+=1
    