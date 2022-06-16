from statistics import variance
from traceback import print_tb
from turtle import left
import numpy as np
import cv2
import pandas as pd
import os
import shutil
from matplotlib import pyplot as plt

#Restablecer en caso de que sea necesario
try:
    shutil.rmtree('./Features/')
except:
    print("No se ha encontrado la carpeta de Features")

#PATHS DESTINO
featuresPath = './Features/'

#CREANDO ENTORNO
os.mkdir(featuresPath)


features = pd.DataFrame()

#CARGAR NOMBRES DE LAS IMAGENES
eyesPath =  './Preprocesado/Ojos/'
eyeImages = os.listdir(eyesPath)
noEyesPath =  './Preprocesado/No_ojos/'
noEyeImages = os.listdir(noEyesPath)


def extractFeatures(hist,isEye):
    return [[i,isEye,np.var(hist)]]


i=0
#PREPROCESSING POR CADA IMAGEN DE CARAS
for name in eyeImages:
    img = cv2.imread(eyesPath+name)
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    histeye = cv2.calcHist([imgray],[0],None,[256],[0,256]).flatten()
    features = features.append(extractFeatures(histeye,1))
    i+=1

#PREPROCESSING POR CADA IMAGEN DE CARAS
for name in noEyeImages:
    img = cv2.imread(noEyesPath+name)
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([imgray],[0],None,[256],[0,256]).flatten()
    features = features.append(extractFeatures(hist,0))
    i+=1
    if i==2000: break

features.columns =['id','isEye','variance','cx','cy']
features.to_csv(featuresPath+'features.csv',index=False)
