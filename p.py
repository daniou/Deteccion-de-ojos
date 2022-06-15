
# Python program to compute and visualize the
# histogram of Blue channel of image

  
# importing libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt


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


img = cv2.imread("sample.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = extractBorders(img, 'laplacian')
cv2.imwrite('bordes.jpg', img)
cv2.imshow('imagen de bordes', img)
cv2.waitKey(0)