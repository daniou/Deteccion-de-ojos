
# Python program to compute and visualize the
# histogram of Blue channel of image

  
# importing libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt
  
# reading the input image
ley = np.zeros((48,32))
im = np.zeros((1024,1024))
img = cv2.imread('sample.jpg',cv2.IMREAD_GRAYSCALE)
Leye = cv2.imread('./Preprocesado/Ojos/0L.jpg',cv2.IMREAD_GRAYSCALE)
# img = cv2.normalize(img,im,0,255,cv2.NORM_MINMAX)
# Leye = cv2.normalize(Leye,ley,0,255,cv2.NORM_MINMAX)

# d
# computing the histogram of the blue channel of the image
hist = cv2.calcHist([img],[0],None,[256],[0,256])
histeye = cv2.calcHist([Leye],[0],None,[256],[0,256])
  
  
# plot the above computed histogram
plt.plot(hist/(img.shape[0]*img.shape[1]), color='b')
plt.plot(histeye/(Leye.shape[0]*Leye.shape[1]), color='r')
plt.title('Image Histogram For Blue Channel GFG')
plt.show()