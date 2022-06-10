import numpy as np
import cv2
import pandas as pd

finalImageSize = (32,48)


img = cv2.imread("noojo.jpg")
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
maxY=int(imgray.shape[0]/finalImageSize[0])
maxX=int(imgray.shape[1]/finalImageSize[1])

i=0
for stepY in range(maxY):
    for stepX in range(maxX):
        cropped = imgray[stepY*finalImageSize[0]:(stepY+1)*finalImageSize[0], 
                        stepX*finalImageSize[1]:(stepX+1)*finalImageSize[1]]
        cv2.imwrite(str(i)+'.jpg', cropped)
        i+=1