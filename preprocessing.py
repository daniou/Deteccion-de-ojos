import numpy as np
import cv2
import pandas as pd
import os

#CREANDO ENTORNO
os.mkdir("Preprocesado")
os.mkdir("Preprocesado/Caras/")
os.mkdir("Preprocesado/Sin_Ojos/")

# PATHS DESTINO
destfacesPath = './Preprocesado/Caras/'
destNoEyesPath = './Preprocesado/Sin_ojos/'

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
    imgray = cv2.resize(imgray,(48,32))
    cv2.imwrite(destfacesPath+str(i)+'.jpg', imgray)
    i+=1

#PREPROCESSING POR CADA IMAGEN SIN OJOS
for name in NoEyesImages:
    img = cv2.imread(noEyesPath+name)
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgray = cv2.resize(imgray,(48,32))
    cv2.imwrite(destNoEyesPath+str(i)+'.jpg', imgray)
    i+=1