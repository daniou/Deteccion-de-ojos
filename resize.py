import numpy as np
import cv2
			

img = cv2.imread("sample.jpg")
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgray=cv2.resize(imgray,(48,32))
cv2.imshow("Imagen",imgray)
cv2.imwrite('sample.jpg', imgray)