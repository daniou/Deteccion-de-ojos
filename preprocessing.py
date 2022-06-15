from turtle import left
import numpy as np
import cv2
import pandas as pd
import os
import shutil

finalImageSize = (32,48)

#Restablecer en caso de que sea necesario
try:
    shutil.rmtree('./Preprocesado')
except:
    print("No se ha encontrado la carpeta de Preprocesado")

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

# print("CARAS:\n",faceImages)
# print("SIN OJOS:\n",noEyesPath)
i=0

#PREPROCESSING POR CADA IMAGEN DE CARAS
for name in faceImages:
    img = cv2.imread(facesPath+name)
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    leftEye = imgray[413:413+4*finalImageSize[0], 284:284+4*finalImageSize[1]]
    rightEye = imgray[413:413+4*finalImageSize[0], 550:550+4*finalImageSize[1]]
    leftEye = cv2.resize(leftEye,(finalImageSize[1],finalImageSize[0]))
    rightEye = cv2.resize(rightEye,(finalImageSize[1],finalImageSize[0]))
    cv2.imwrite(destFacesPath+str(i)+'L.jpg', leftEye)
    cv2.imwrite(destFacesPath+str(i)+'R.jpg', rightEye)
    i+=1

#PREPROCESSING POR CADA IMAGEN SIN OJOS
for name in NoEyesImages:
    img = cv2.imread(noEyesPath+name)
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    maxX=int(imgray.shape[1]/finalImageSize[1])
    maxY=int(imgray.shape[0]/finalImageSize[0])
    print(maxY,maxX)
    for stepY in range(maxY-1):
        for stepX in range(maxX-1):
            cropped = imgray[stepY*finalImageSize[0]:(stepY+1)*finalImageSize[0], 
                            stepX*finalImageSize[1]:(stepX+1)*finalImageSize[1]]
            cv2.imwrite(destNoEyesPath+str(i)+'.jpg', cropped)
            i+=1
    