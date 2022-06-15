from statistics import variance
from traceback import print_tb
from turtle import left
from cv2 import sqrBoxFilter, sqrt
import numpy as np
import cv2
import pandas as pd
import os
import shutil
from matplotlib import pyplot as plt

#Restablecer en caso de que sea necesario
try:
    shutil.rmtree('./Border_images/')
except:
    print("No se ha encontrado la Border_images")

#PATHS DESTINO
borderImagesPath = './Border_images/'

#CREANDO ENTORNO
os.mkdir(borderImagesPath)
os.mkdir(borderImagesPath+'Ojos/')
os.mkdir(borderImagesPath+'No_ojos/')

#CARGAR NOMBRES DE LAS IMAGENES
eyesPath =  'Preprocesado/Ojos/'
eyeImages = os.listdir(eyesPath)
noEyesPath =   'Preprocesado/No_ojos/'
noEyeImages = os.listdir(noEyesPath)

def extractBorders(img, mode):
    if mode == 'canny':
        edges = cv2.Canny(img, 100, 200)
    elif mode == 'laplacian':
        edges = cv2.Laplacian(img, cv2.CV_64F)
    else:
        edgex = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)  # x
        edgey = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)  # y
        edges = (edgex + edgey) / 2
    return edges
i=0

#PREPROCESSING POR CADA IMAGEN DE CARAS
for name in eyeImages:
    img = cv2.imread(eyesPath+name)
    imgray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    res = extractBorders(imgray,'canny')
    cv2.imwrite(borderImagesPath+'Ojos/'+name+'.jpg', res)
    i+=1

#PREPROCESSING POR CADA IMAGEN DE CARAS
for name in noEyeImages:
    img = cv2.imread(noEyesPath+name)
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    res = extractBorders(imgray,'canny')
    cv2.imwrite(borderImagesPath+'No_ojos/'+name+'.jpg', res)
    i+=1
