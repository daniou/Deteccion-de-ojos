from statistics import variance
from turtle import left
import numpy as np
import cv2
import pandas as pd
import os
import shutil
from matplotlib import pyplot as plt

#Restablecer en caso de que sea necesario
try:
    shutil.rmtree('./Histogramas')
except:
    print("No se ha encontrado la carpeta de Histogramas")

#PATHS DESTINO
histsPath = './Histogramas/'

#CREANDO ENTORNO
os.mkdir(histsPath)


#CARGAR NOMBRES DE LAS IMAGENES
eyesPath =  './Preprocesado/Ojos/'
eyeImages = os.listdir(eyesPath)

i=0

#PREPROCESSING POR CADA IMAGEN DE CARAS
for name in eyeImages:
    img = cv2.imread(eyesPath+name)
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    histeye = cv2.calcHist([imgray],[0],None,[256],[0,256]).flatten()
    
    print(histeye)
    print(i," ------------------")
    print(np.var(histeye))
    if i ==0: break
    i+=1
